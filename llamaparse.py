from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings, Document
from llama_index.core import StorageContext
from llama_index.llms.openai import OpenAI
from llama_index.postprocessor.cohere_rerank import CohereRerank
import openai
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SimpleFileNodeParser
from llama_parse import LlamaParse
import pandas as pd
import os

prompt_text = "this pdf is a checksheet for college students to which classes they need to take for their major while also displaying how many credits each course is\
    . it has a pathways section telling you which pathways classes\
you need to take, it then shows all the courses you are required to take to graduate. "

parser = LlamaParse(
    api_key=  os.getenv('LLAMA_CLOUD_API_KEY'),# can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    verbose=True,
    parsing_instructions=prompt_text,
)

documents = []
for a, b, c in os.walk("pdfs"):
    for i in range(3):
        print(c[i])
        documents += parser.load_data("pdfs/"+c[i])

documents += parser.load_data("pdfs/cos_cmda_cmdp_22_23.pdf")
documents += parser.load_data("pdfs/minor_fin_22_23.pdf")
documents += parser.load_data("pdfs/cmda_flowchart.pdf")


for a, b, c in os.walk('data'):
    for file in c:
        if file != ".DS_Store":
            print(file)
            df = pd.read_csv('data/'+file, chunksize=100)
            for chunk in df:
                documents.append(Document(text=chunk.to_string()))

GENERATION_MODEL = "gpt-4o-mini"
Settings.llm = OpenAI(model=GENERATION_MODEL)

parser = SimpleFileNodeParser()
nodes = parser.get_nodes_from_documents(documents)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = VectorStoreIndex(nodes, show_progress=True, storage_context=storage_context)
index.set_index_id("bigdata2")
index.storage_context.persist(show_progress=True)