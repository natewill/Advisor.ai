import os
from llama_parse import LlamaParse
from llama_index.core import Settings
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import MarkdownElementNodeParser
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.kdbai import KDBAIVectorStore
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.readers.file import CSVReader
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings


from getpass import getpass
import kdbai_client as kdbai
import nest_asyncio

nest_asyncio.apply()

from llama_parse import LlamaParse

#print(os.getenv('LLAMA_CLOUD_API_KEY'))

# sync
KDBAI_ENDPOINT = (
    os.environ["KDBAI_ENDPOINT"]
    if "KDBAI_ENDPOINT" in os.environ
    else input("KDB.AI endpoint: ")
)
KDBAI_API_KEY = (
    os.environ["KDBAI_API_KEY"]
    if "KDBAI_API_KEY" in os.environ
    else getpass("KDB.AI API key: ")
)

#connect to KDB.AI
session = kdbai.Session(api_key=KDBAI_API_KEY, endpoint=KDBAI_ENDPOINT)

# The schema contains two metadata columns (document_id, text) and one embeddings column
# Index type, search metric (Euclidean distance), and dimensions are specified in the embedding column
schema = dict(
    columns=[
        dict(name="document_id", pytype="bytes"),
        dict(name="text", pytype="bytes"),
        dict(
            name="embedding",
            vectorIndex=dict(type="flat", metric="L2", dims=1536),
        ),
    ]
)

KDBAI_TABLE_NAME = "LlamaParse_Table"

# First ensure the table does not already exist
if KDBAI_TABLE_NAME in session.list():
    session.table(KDBAI_TABLE_NAME).drop()

#Create the table
table = session.create_table(KDBAI_TABLE_NAME, schema)

prompt_text = "this pdf is a checksheet for college students to which classes they need to take for their major while also displaying how many credits each course is\
    . it has a pathways section telling you which pathways classes\
you need to take, it then shows all the courses you are required to take to graduate. "
parser = LlamaParse(
    api_key=os.getenv('LLAMA_CLOUD_API_KEY'),  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    verbose=True,
    parsing_instructions=prompt_text,
)
data = SimpleDirectoryReader(input_dir="data/").load_data(show_progress=True)


documents = []
for a, b, c in os.walk("pdfs"):
    for i in range(3):
        print(c[i])
        documents += parser.load_data("pdfs/"+c[i])
documents += parser.load_data("pdfs/cos_cmda_cmdp_22_23.pdf")
documents += parser.load_data("pdfs/minor_fin_22_23.pdf")


documents += data

GENERATION_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL  = "text-embedding-3-small"
llm = OpenAI(model=GENERATION_MODEL)
embed_model = OpenAIEmbedding(model=EMBEDDING_MODEL)
llm.api_key = os.getenv('OPENAI_API_KEY')

Settings.llm = llm
Settings.embed_model = embed_model

node_parser = MarkdownElementNodeParser(llm=llm, num_workers=32).from_defaults()

# Retrieve nodes (text) and objects (table)
nodes = node_parser.get_nodes_from_documents(documents)

base_nodes, objects = node_parser.get_nodes_and_objects(nodes)

vector_store = KDBAIVectorStore(table)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

#Create the index, inserts base_nodes and objects into KDB.AI
recursive_index = VectorStoreIndex(
    nodes= base_nodes + objects, storage_context=storage_context
)

# Query KDB.AI to ensure the nodes were inserted
table.query()

### Define reranker
cohere_rerank = CohereRerank(top_n=10)

### Create the query_engine to execute RAG pipeline using LlamaIndex, KDB.AI, and Cohere reranker
query_engine = recursive_index.as_query_engine(similarity_top_k=15, node_postprocessors=[cohere_rerank])

query_1 = "I am a CMDA Major Minoring in Finance. I am wondering if I need to take  BIT 2405 or if cmda 2005 and cmda 2006. I see online that stats 3006 and stats 3005  can be a subtitue for that class but can CMDA 2005 and 2006 be a substitue?"

response_1 = query_engine.query(query_1)

print(str(response_1))