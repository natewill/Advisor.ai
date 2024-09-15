import csv

data = """Professor Name,Department,University,Quality Rating,Number of Ratings,Would Take Again,Level of Difficulty
Jason Sharp,Accounting,Virginia Tech,4.7,82,94%,2
Kimberly Walker,Accounting,Virginia Tech,1.3,9,0%,4.9
Fulton Galer,Accounting,Virginia Tech,3.1,4,50%,3.1
Dianna Ross,Accounting,Virginia Tech,5.0,2,N/A,2
France Belanger,Accounting,Virginia Tech,5.0,1,N/A,3
Sarah Stein,Accounting,Virginia Tech,4.5,1,N/A,3
Floyd Beams,Accounting,Virginia Tech,0.0,0,N/A,0
Reza Bharki,Accounting,Virginia Tech,0.0,0,N/A,0
Ling Lisic,Accounting,Virginia Tech,0.0,0,N/A,0
Cintia Easterwood,Accounting,Virginia Tech,2.4,63,35%,4.1
Marilyn Griffin,Accounting,Virginia Tech,2.5,12,N/A,4.1
John Brozovsky,Accounting,Virginia Tech,2.5,12,0%,4.5
Gregory Kogan,Accounting,Virginia Tech,4.1,8,88%,3.3
Adam Du Pon,Accounting,Virginia Tech,4.1,5,80%,3.4
Nadia Rogers,Accounting,Virginia Tech,5.0,4,100%,3.3
Jing Huang,Accounting,Virginia Tech,3.0,3,34%,3.8
Michele Meckfessel,Accounting,Virginia Tech,5.0,1,N/A,2
Marshall Vance,Accounting,Virginia Tech,5.0,1,100%,3
Ryan Musselman,Accounting,Virginia Tech,5.0,1,100%,2
Wenqi Shen,Accounting,Virginia Tech,5.0,1,100%,4
Mike Truelsen,Accounting,Virginia Tech,0.0,0,N/A,0
Frank Galer,Accounting,Virginia Tech,0.0,0,N/A,0
Matt Cobabe,Accounting,Virginia Tech,0.0,0,N/A,0
Reza Barkhi,Accounting,Virginia Tech,3.5,2,0%,3.5
Donald Compton,Accounting,Virginia Tech,4.0,2,100%,3
E Scott Johnson,Accounting,Virginia Tech,5.0,2,100%,2
Christie Hayne,Accounting,Virginia Tech,1.0,1,0%,4
Ryan Hamilton,Accounting,Virginia Tech,0.0,0,N/A,0
Noah Ehreth,Accounting,Virginia Tech,0.0,0,N/A,0
Sean Hillison,Accounting,Virginia Tech,0.0,0,N/A,0
Jean Lacoste,Accounting,Virginia Tech,2.7,132,84%,3.2
David Tegarden,Accounting,Virginia Tech,1.4,13,0%,5
Randal Gatzke,Accounting,Virginia Tech,5.0,6,100%,3.6
Matthew Cobabe,Accounting,Virginia Tech,3.5,2,50%,3
Lynn Almond,Accounting,Virginia Tech,4.1,20,73%,3.9
Matthew Erickson,Accounting,Virginia Tech,4.9,17,89%,5
James Yardley,Accounting,Virginia Tech,3.1,12,N/A,3.8
Linda Wallace,Accounting,Virginia Tech,2.9,4,75%,3.8
Michelle Harding,Accounting,Virginia Tech,4.6,4,100%,3.6
Dana Garner,Accounting,Virginia Tech,3.0,3,67%,3.4
Francis Ding,Accounting,Virginia Tech,3.7,3,67%,3.3
Jonathan DiYorio,Accounting,Virginia Tech,1.0,1,0%,5
Greg Jenkins,Accounting,Virginia Tech,5.0,1,N/A,3
Sarah Asebedo,Accounting,Virginia Tech,1.5,1,N/A,4
Owen Hughes,Aerospace Studies,Virginia Tech,4.0,1,N/A,4
Shane Ross,Aerospace Studies,Virginia Tech,5.0,1,100%,2
William Devenport,Aerospace Studies,Virginia Tech,5.0,1,100%,2
Michael Philen,Aerospace Studies,Virginia Tech,3.2,12,59%,2.9
Scott England,Aerospace Studies,Virginia Tech,5.0,4,100%,3.4
Ella Atkins,Aerospace Studies,Virginia Tech,2.0,2,0%,4
Jie Song,Aerospace Studies,Virginia Tech,4.0,2,100%,2
Aurelien Borgoltz,Aerospace Studies,Virginia Tech,3.0,1,0%,3
Mathieu Joerger,Aerospace Studies,Virginia Tech,5.0,1,100%,4
Christine Gilbert,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Gary Seidel,Aerospace Studies,Virginia Tech,5.0,3,100%,3.8
Lili Ma,Aerospace Studies,Virginia Tech,1.5,2,N/A,4
Kevin Wang,Aerospace Studies,Virginia Tech,1.0,2,0%,5
Riley Fitzgerald,Aerospace Studies,Virginia Tech,5.0,1,100%,2
Nanyaporn Intaratep,Aerospace Studies,Virginia Tech,4.0,1,100%,4
Pat Artis,Aerospace Studies,Virginia Tech,3.8,9,67%,4
Eric Paterson,Aerospace Studies,Virginia Tech,2.5,4,25%,4.3
Wayne Neu,Aerospace Studies,Virginia Tech,1.0,1,N/A,4
Pradeep Raj,Aerospace Studies,Virginia Tech,3.0,1,0%,2
Yao Fu,Aerospace Studies,Virginia Tech,4.0,1,100%,3
Stefano Brizzolara,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Christopher Roy,Aerospace Studies,Virginia Tech,5.0,3,100%,2.7
Heng Xiao,Aerospace Studies,Virginia Tech,4.0,2,0%,3.5
Inga Schlier,Aerospace Studies,Virginia Tech,5.0,1,100%,2
Mayuresh Patil,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Michael Fowler,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Colin Adams,Aerospace Studies,Virginia Tech,0.0,0,N/A,0
Cheryl Montgomery,African Studies,Virginia Tech,5.0,1,100%,3
Dennis Halpin,African Studies,Virginia Tech,4.0,1,100%,2
Paula Seniors,African Studies,Virginia Tech,1.9,11,17%,2.6
Komal Dhillon,African Studies,Virginia Tech,3.4,3,67%,2.8
Jariah Strozier,African Studies,Virginia Tech,2.0,1,0%,1
David Schmale,Agriculture,Virginia Tech,5.0,10,100%,3.3
Eric Beers,Agriculture,Virginia Tech,4.0,5,60%,3.4
Jennifer Friedel,Agriculture,Virginia Tech,3.5,4,50%,4.6
Jeffrey Alwang,Agriculture,Virginia Tech,1.0,2,0%,2.5
Eric Kaufman,Agriculture,Virginia Tech,3.5,1,N/A,1
Alex Hessler,Agriculture,Virginia Tech,5.0,1,100%,2
Kayla Harris,Agriculture,Virginia Tech,5.0,1,100%,2
Linda Taylor,Agriculture,Virginia Tech,0.0,0,N/A,0
Megan O'Rourke,Agriculture,Virginia Tech,0.0,0,N/A,0
Natalie Duncan,Agriculture,Virginia Tech,1.4,3,0%,4.4
Jessica Bedore,Agriculture,Virginia Tech,5.0,2,100%,1
Alan McDaniel,Agriculture,Virginia Tech,5.0,1,N/A,1
Mary Marchant,Agriculture,Virginia Tech,2.5,1,N/A,3
Greg Welbaum,Agriculture,Virginia Tech,1.0,1,0%,3
Mark Sumner,Agriculture,Virginia Tech,5.0,1,100%,1
Naveen Abedin,Agriculture,Virginia Tech,1.0,1,0%,4
Ryan Musselman,Agriculture,Virginia Tech,2.0,4,25%,3.5
Kathryn Albright,Agriculture,Virginia Tech,3.3,3,100%,3
Jerald Walz,Agriculture,Virginia Tech,1.0,1,0%,1
Kimberly Morgan,Agriculture,Virginia Tech,4.0,1,100%,2
Joe Guthrie,Agriculture,Virginia Tech,0.0,0,N/A,0
Michael Ellerbrock,Agriculture,Virginia Tech,0.0,0,N/A,0
renee boyer,Agriculture,Virginia Tech,0.0,0,N/A,0
Mark Cline,Agriculture,Virginia Tech,3.2,23,57%,4.5
Sam Doak,Agriculture,Virginia Tech,4.0,6,N/A,3
Katharine Knowlton,Agriculture,Virginia Tech,4.0,5,67%,2.3
Hannah Scherer,Agriculture,Virginia Tech,4.7,3,100%,2
Joshua Kardos,Agriculture,Virginia Tech,5.0,1,100%,2
Jacob Barney,Agriculture,Virginia Tech,5.0,1,100%,3
Catherine Larochelle,Agriculture,Virginia Tech,1.0,2,0%,3
Kim Niewolny,Agriculture,Virginia Tech,5.0,1,100%,4
Katherine Boys,Agriculture,Virginia Tech,2.0,1,N/A,4
Kent Hurley,Agriculture,Virginia Tech,0.0,0,N/A,0
Daniel Sandor,Agriculture,Virginia Tech,0.0,0,N/A,0
Alex Niemiera,Agriculture,Virginia Tech,5.0,20,100%,1.5
Kurt Stephenson,Agriculture,Virginia Tech,4.4,17,29%,2.9
Matt Eick,Agriculture,Virginia Tech,4.1,15,29%,2.9
Carl Zipper,Agriculture,Virginia Tech,2.9,6,N/A,4.5
Richard Rateau,Agriculture,Virginia Tech,3.3,7,58%,2.9
. Geyer,Agriculture,Virginia Tech,3.5,4,N/A,4.3
Ozzie Abaye,Agriculture,Virginia Tech,5.0,4,100%,2.9
Saghai Maroof,Agriculture,Virginia Tech,3.5,1,N/A,2
George Norton,Agriculture,Virginia Tech,5.0,1,100%,3
Clinton Neill,Agriculture,Virginia Tech,3.0,1,100%,2
Alexis Wivell,Agriculture,Virginia Tech,5.0,1,100%,3
Donna Westfall-Rudd,Agriculture,Virginia Tech,1.0,2,0%,2
Tiffany Drape,Agriculture,Virginia Tech,1.0,1,0%,3
Michelle Greaud,Agriculture,Virginia Tech,5.0,1,100%,2
richard plateau,Agriculture,Virginia Tech,0.0,0,N/A,0
Kellie Claflin,Agriculture,Virginia Tech,0.0,0,N/A,0
Dennis Cladis,Agriculture,Virginia Tech,0.0,0,N/A,0
Monica Ponder,Agriculture,Virginia Tech,0.0,0,N/A,0
Nada Tamim,Animal Science,Virginia Tech,2.9,7,43%,4.2
Elizabeth Gilbert,Animal Science,Virginia Tech,5.0,6,100%,4
Shelly Rhoads,Animal Science,Virginia Tech,2.8,5,25%,3.9
Gota Morota,Animal Science,Virginia Tech,5.0,4,100%,2.6
Ron Lewis,Animal Science,Virginia Tech,4.6,4,N/A,3
Dan Eversole,Animal Science,Virginia Tech,1.0,2,0%,5
Scott Greiner,Animal Science,Virginia Tech,0.0,0,N/A,0
Fawzy Elnady,Animal Science,Virginia Tech,0.0,0,N/A,0
Heather Bradford,Animal Science,Virginia Tech,3.7,6,67%,3
Lisa Gunter,Animal Science,Virginia Tech,4.5,2,100%,2
Robert Rhoads,Animal Science,Virginia Tech,0.0,0,N/A,0
Bill Beal,Animal Science,Virginia Tech,4.0,26,N/A,3.5
Luciana Bergamasco,Animal Science,Virginia Tech,4.0,11,63%,2.3
Sally Johnson,Animal Science,Virginia Tech,1.0,1,0%,5
John Maurer,Animal Science,Virginia Tech,1.0,1,0%,1
Cynthia Wood,Animal Science,Virginia Tech,2.0,41,7%,3.9
Emma Helm,Animal Science,Virginia Tech,5.0,23,100%,2.1
Michael Denbow,Animal Science,Virginia Tech,2.9,14,25%,3.8
Julia McCann,Animal Science,Virginia Tech,3.1,5,N/A,2.6
Erica Feuerbacher,Animal Science,Virginia Tech,4.0,2,100%,1.5
Beth Sheely,Animal Science,Virginia Tech,0.0,0,N/A,0
James Knight,Animal Science,Virginia Tech,0.0,0,N/A,0
Mark Schneider,Architecture,Virginia Tech,3.2,6,100%,N/A
Christopher Pritchett,Architecture,Virginia Tech,4.2,6,84%,4
Terry Surjan,Architecture,Virginia Tech,2.0,5,0%,5
Aaron Betsky,Architecture,Virginia Tech,1.8,5,20%,2.6
Miranda Shugars,Architecture,Virginia Tech,1.0,2,0%,4
Bradley Whitney,Architecture,Virginia Tech,2.5,2,50%,4.5
Ben Pennell,Architecture,Virginia Tech,3.7,3,67%,4.7
Dave Dugas,Architecture,Virginia Tech,3.5,1,N/A,1
Jonas Hauptman,Architecture,Virginia Tech,2.0,1,0%,1
Jessica Hernandez,Architecture,Virginia Tech,0.0,0,N/A,0
Markus Breitschmid,Architecture,Virginia Tech,4.8,19,67%,4.1
Shelley Martin,Architecture,Virginia Tech,2.5,9,17%,3
Christopher Pritchett,Architecture,Virginia Tech,4.2,6,84%,4
Terry Surjan,Architecture,Virginia Tech,2.0,5,0%,5
Aaron Betsky,Architecture,Virginia Tech,1.8,5,20%,2.6
Miranda Shugars,Architecture,Virginia Tech,1.0,2,0%,4
Bradley Whitney,Architecture,Virginia Tech,2.5,2,50%,4.5
Ben Pennell,Architecture,Virginia Tech,3.7,3,67%,4.7
Dave Dugas,Architecture,Virginia Tech,3.5,1,N/A,1
Jonas Hauptman,Architecture,Virginia Tech,2.0,1,0%,1
Tamer Radaideh,Architecture,Virginia Tech,1.0,1,0%,4
Andrew Shaver,Architecture,Virginia Tech,5.0,2,100%,3.5
David Haney,Architecture,Virginia Tech,2.0,1,0%,3
Enric Ruiz Geli,Architecture,Virginia Tech,0.0,0,N/A,0
Holly Kasperbauer,Architecture,Virginia Tech,4.8,3,N/A,1.3
Bob Dunay,Architecture,Virginia Tech,0.0,0,N/A,0
Edward Becker,Architecture,Virginia Tech,0.0,0,N/A,0
Clive Vorster,Architecture,Virginia Tech,4.3,9,100%,2.3
Laura McGuire,Architecture,Virginia Tech,5.0,2,N/A,4
Leigh Lally,Architecture,Virginia Tech,4.0,1,N/A,3
Sharone Tomer,Architecture,Virginia Tech,5.0,1,100%,4
Scott Gartner,Architecture,Virginia Tech,3.9,7,67%,2.3
Annie Pearce,Architecture,Virginia Tech,2.8,4,100%,1
Jim Jones,Architecture,Virginia Tech,3.9,3,100%,2.4
Luis Alvarez,Architecture,Virginia Tech,2.3,3,N/A,3.3
Paola Zellner Bassett,Architecture,Virginia Tech,2.7,3,0%,3.3
Wendy Jacobson,Architecture,Virginia Tech,2.0,1,N/A,5
Melanie Faith,Architecture,Virginia Tech,5.0,1,N/A,5
Sal Choudhury,Architecture,Virginia Tech,5.0,1,100%,1
Brad Whitney,Architecture,Virginia Tech,5.0,1,100%,1
Madison Cook,Architecture,Virginia Tech,5.0,1,100%,5
Joseph Wheeler,Architecture,Virginia Tech,0.0,0,N/A,0
Kevin Jones,Architecture,Virginia Tech,0.0,0,N/A,0
William Green,Architecture,Virginia Tech,0.0,0,N/A,0
Hilary Bryon,Architecture,Virginia Tech,1.5,2,0%,5
Bill Galloway,Architecture,Virginia Tech,4.8,2,N/A,2.5
Frank Weiner,Architecture,Virginia Tech,2.3,2,N/A,3
Kay Edge,Architecture,Virginia Tech,3.5,1,N/A,2
Edward Dorsa,Architecture,Virginia Tech,5.0,1,N/A,4
Kim Mintai,Architecture,Virginia Tech,3.0,1,100%,1
Mario Cortes,Architecture,Virginia Tech,5.0,1,100%,4
Aki Ishida,Architecture,Virginia Tech,0.0,0,N/A,0
Kathryn Prigmore,Architecture,Virginia Tech,0.0,0,N/A,0
Henri de Hahn,Architecture,Virginia Tech,0.0,0,N/A,0
Virginia Melnyk,Architecture,Virginia Tech,0.0,0,N/A,0
Deidre Regan,Architecture,Virginia Tech,0.0,0,N/A,0
Jessica Hernandez,Architecture,Virginia Tech,0.0,0,N/A,0
Anne Ronan,Art History,Virginia Tech,5.0,3,100%,3
Rene Sparr,Art History,Virginia Tech,0.0,0,N/A,0
Ann Marie Knoblauch,Art History,Virginia Tech,4.0,22,55%,3.4
Renee Spaar,Art History,Virginia Tech,2.5,6,34%,3.9
Claire Weiss,Art History,Virginia Tech,0.0,0,N/A,0
Lauren DiSalvo,Art History,Virginia Tech,4.5,2,100%,2.5
Michelle Moseley-Christian,Art History,Virginia Tech,2.8,14,25%,4.4
Vasiliki Ampatzi,Art History,Virginia Tech,4.0,1,100%,2
Zachary MacKey,Biochemistry,Virginia Tech,2.8,7,50%,3.3
Richard Helm,Biochemistry,Virginia Tech,3.5,2,50%,1.5
Jennifer Stewart,Biochemistry,Virginia Tech,5.0,1,100%,1
Francis Farrell,Biochemistry,Virginia Tech,0.0,0,N/A,0
Biswarup Mukhopadhyay,Biochemistry,Virginia Tech,0.0,0,N/A,0
Annie Staples,Biochemistry,Virginia Tech,0.0,0,N/A,0
Daniel Slade,Biochemistry,Virginia Tech,3.9,7,72%,3.6
Caitlin Cridland,Biochemistry,Virginia Tech,0.0,0,N/A,0
Sasha Marine,Biochemistry,Virginia Tech,4.0,8,75%,4.1
Amanda Sharp,Biochemistry,Virginia Tech,5.0,1,100%,3
Kristopher Hite,Biochemistry,Virginia Tech,0.0,0,N/A,0
Eugene Gregory,Biochemistry,Virginia Tech,4.1,5,N/A,4.8
Kylie Allen,Biochemistry,Virginia Tech,4.5,2,100%,4.5
Peter Kennelly,Biochemistry,Virginia Tech,0.0,0,N/A,0
Todd Fredericksen,Biology,Virginia Tech,4.1,20,90%,3.0
Brent Opell,Biology,Virginia Tech,4.8,19,74%,3.8
Bruce Turner,Biology,Virginia Tech,2.5,13,N/A,3.8
Joe Falkinham,Biology,Virginia Tech,3.9,11,100%,2.9
Kristen Bretz,Biology,Virginia Tech,4.9,9,100%,3.4
Stephanie Voshell,Biology,Virginia Tech,5.0,6,100%,1.6
Jackson Evans,Biology,Virginia Tech,4.9,6,100%,1.8
David Chambers,Biology,Virginia Tech,5.0,5,N/A,2.4
Sally Paulson,Biology,Virginia Tech,3.6,5,100%,2.6
Sparkle Williams,Biology,Virginia Tech,1.5,4,0%,2.5
Jordan Metzgar,Biology,Virginia Tech,4.0,3,100%,2.4
Fred Benfield,Biology,Virginia Tech,4.3,2,N/A,3.0
Silke Hauf,Biology,Virginia Tech,4.0,2,100%,3.5
Tristan Hayes,Biology,Virginia Tech,1.8,2,N/A,4.5
Elizabeth Dunnington,Biology,Virginia Tech,5.0,1,N/A,3.0
Paul Marek,Biology,Virginia Tech,5.0,1,100%,2.0
Martha Munoz,Biology,Virginia Tech,0.0,0,N/A,0.0
Joh'anna Nugent,Biology,Virginia Tech,0.0,0,N/A,0.0
Lee Wooram,Biology,Virginia Tech,3.9,19,79%,2.8
Shokraii,Biology,Virginia Tech,2.8,18,N/A,3.8
Ignacio Moore,Biology,Virginia Tech,4.4,17,92%,3.4
Aparna Shah,Biology,Virginia Tech,3.4,16,44%,4.3
Joel McGlothlin,Biology,Virginia Tech,2.3,11,28%,4.6
Daniela Cimini,Biology,Virginia Tech,2.1,10,34%,4.8
Rachel Morgante-Richmeier,Biology,Virginia Tech,4.0,1,100%,2.0
Kate Langwig,Biology,Virginia Tech,2.0,1,100%,5.0
EF Benfield,Biology,Virginia Tech,4.5,1,N/A,2.0
Nidhi Menon,Biology,Virginia Tech,0.0,0,N/A,0.0
Bryan Hsu,Biology,Virginia Tech,0.0,0,N/A,0.0
Julia Basso,Biology,Virginia Tech,0.0,0,N/A,0.0
Mike Rosenzweig,Biology,Virginia Tech,4.5,103,87%,3.5
Eric Hogan,Biology,Virginia Tech,4.3,36,82%,3.8
Michael Rosenzweig,Biology,Virginia Tech,4.3,12,84%,3.1
Stephen Melville,Biology,Virginia Tech,2.1,9,34%,4.4
Klaus Elgert,Biology,Virginia Tech,3.7,9,N/A,4.8
Florian Schubot,Biology,Virginia Tech,4.9,7,100%,3.6
Rebekah DeToma,Biology,Virginia Tech,3.4,5,40%,1.0
Paul Risteca,Biology,Virginia Tech,4.3,3,100%,2.0
Andrew Muchlinski,Biology,Virginia Tech,4.0,2,100%,2.0
Jeb Barrett,Biology,Virginia Tech,5.0,1,100%,3.0
Melissa Burt,Biology,Virginia Tech,5.0,1,100%,3.0
Kendra Sewall,Biology,Virginia Tech,5.0,1,100%,2.0
Richard Mitchell,Biology,Virginia Tech,0.0,0,N/A,0.0
Brian Hsu,Biology,Virginia Tech,0.0,0,N/A,0.0
Cameron Braswell,Biology,Virginia Tech,4.8,6,84%,2.8
Margaret Couvillon,Biology,Virginia Tech,5.0,5,100%,3.0
Jill Sible,Biology,Virginia Tech,4.1,5,N/A,2.6
Richard Fell,Biology,Virginia Tech,3.8,2,N/A,4.0
John Jelesko,Biology,Virginia Tech,0.0,0,N/A,0.0
Mary Lipscomb,Biology,Virginia Tech,3.3,110,60%,3.4
Jonathan Watkinson,Biology,Virginia Tech,2.6,90,38%,3.9
Megan Emori,Biology,Virginia Tech,3.9,73,72%,3.6
Terri Gillian,Biology,Virginia Tech,2.1,56,21%,4.6
Richard Seyler,Biology,Virginia Tech,3.1,48,27%,4.5
George Simmons,Biology,Virginia Tech,3.4,41,N/A,3.7
Jack Evans,Biology,Virginia Tech,4.2,29,78%,2.6
Roger Sheppard,Biology,Virginia Tech,2.4,24,9%,3.5
Al Buikema,Biology,Virginia Tech,3.4,16,N/A,3.7
Jerry Via,Biology,Virginia Tech,4.3,16,N/A,3.1
Lisa Belden,Biology,Virginia Tech,5.0,14,100%,2.6
Jeremy Draghi,Biology,Virginia Tech,2.8,12,42%,4.3
Richard Walker,Biology,Virginia Tech,3.9,10,75%,3.6
Zhaomin Yang,Biology,Virginia Tech,3.3,5,100%,2.6
Glen Stevens,Biology,Virginia Tech,3.8,2,100%,3.0
Meryl Mims,Biology,Virginia Tech,4.0,2,100%,2.0
Alison Burke,Biology,Virginia Tech,2.0,1,0%,4.0
Jeffrey Kuhn,Biology,Virginia Tech,3.0,1,N/A,5.0
Austin Gray,Biology,Virginia Tech,2.0,1,0%,5.0
Carla Finkielstein,Biology,Virginia Tech,0.0,0,N/A,0.0
Martin Jones,Biotechnology,Virginia Tech,4.5,5,100%,N/A
Kereshmeh Afsari,Building Construction,Virginia Tech,1.9,6,17%,4.1
Ashley Johnson,Building Construction,Virginia Tech,3.0,2,100%,2.0
Josh Iorio,Building Construction,Virginia Tech,3.0,4,50%,1.5
Lindsay Lally,Building Construction,Virginia Tech,5.0,2,100%,1.5
Georg Reichard,Building Construction,Virginia Tech,1.8,6,17%,3.8
Nazila Roofigari,Building Construction,Virginia Tech,4.0,1,100%,3.0
Walid Thabet,Building Construction,Virginia Tech,4.0,1,100%,4.0
Phil Agee,Building Construction,Virginia Tech,5.0,3,100%,3.0
Joe O'Neal,Building Construction,Virginia Tech,3.5,2,0%,2.5
Thomas Mills,Building Construction,Virginia Tech,2.7,9,25%,2.7
Abiola Akanmu,Building Construction,Virginia Tech,3.3,6,67%,4.1
Jonathan Bluey,Building Construction,Virginia Tech,3.3,4,50%,3.3
Yvan Beliveau,Building Construction,Virginia Tech,5.0,1,N/A,3.0
Tanyel Bulbul,Building Construction,Virginia Tech,4.0,1,100%,5.0
Bob Muir,Building Construction,Virginia Tech,1.0,1,0%,5.0
Ruichuan Zhang,Building Construction,Virginia Tech,0.0,0,N/A,0.0
Laura Clark,Business,Virginia Tech,3.4,40,54%,3.4
James Kern,Business,Virginia Tech,4.2,32,94%,3.2
Raman Kumar,Business,Virginia Tech,4.1,8,67%,3.1
Denise Cordova,Business,Virginia Tech,5.0,7,100%,3.3
Nohel Zaman,Business,Virginia Tech,5.0,6,100%,2.3
Bernard Taylor,Business,Virginia Tech,2.3,5,20%,3.8
Andy Travers,Business,Virginia Tech,4.0,3,100%,3.0
Rex Waters,Business,Virginia Tech,4.0,3,100%,2.8
Rajalakshmi Raman,Business,Virginia Tech,3.5,2,50%,2.0
Jason Deane,Business,Virginia Tech,4.0,2,N/A,3.0
Sukhwa Hong,Business,Virginia Tech,3.0,2,50%,3.5
Parviz Ghandforoush,Business,Virginia Tech,1.0,1,0%,3.0
Christopher Zobel,Business,Virginia Tech,2.0,1,0%,3.0
Ramona Ionescu,Business,Virginia Tech,4.0,1,100%,3.0
Alexandre Pecora,Business,Virginia Tech,5.0,1,100%,4.0
Laura Townsend,Business,Virginia Tech,5.0,1,100%,2.0
Roberta Russell,Business,Virginia Tech,0.0,0,N/A,0.0
Raji Raman,Business,Virginia Tech,0.0,0,N/A,0.0
Philip Romero-Masters,Business,Virginia Tech,1.5,11,0%,3.9
Michelle Seref,Business,Virginia Tech,5.0,10,90%,3.1
Chi Tseng,Business,Virginia Tech,4.0,6,84%,1.4
Justin Monday,Business,Virginia Tech,2.6,6,17%,2.9
Don Rieley,Business,Virginia Tech,2.9,5,N/A,4.2
Jay Pokorski,Business,Virginia Tech,2.5,5,N/A,4.4
Lance Matheson,Business,Virginia Tech,2.7,3,34%,2.3
Michael Flora,Business,Virginia Tech,3.8,3,67%,1.8
Hainan Sheng,Business,Virginia Tech,5.0,2,100%,3.0
Angelia Lucas,Business,Virginia Tech,3.0,1,0%,1.0
Joseph Pitt,Business,Virginia Tech,5.0,1,100%,4.0
Ruba Aljafari,Business,Virginia Tech,0.0,0,N/A,0.0
Levern Currie,Business,Virginia Tech,0.0,0,N/A,0.0
Megan Dickhans,Business,Virginia Tech,0.0,0,N/A,0.0
Long Xia,Business,Virginia Tech,0.0,0,N/A,0.0
Reed Kennedy,Business,Virginia Tech,0.0,0,N/A,0.0
Jay Teets,Business,Virginia Tech,3.6,12,82%,2.2
Eli Jamison,Business,Virginia Tech,5.0,8,100%,2.9
Ralph Badinelli,Business,Virginia Tech,1.8,8,0%,4.5
Richard Jones,Business,Virginia Tech,4.5,7,100%,1.6
Broderick Turner,Business,Virginia Tech,3.0,5,40%,2.9
Idris Adjerid,Business,Virginia Tech,4.8,4,100%,2.9
Anastasia Cortes,Business,Virginia Tech,3.5,4,50%,3.6
Jiayi Liu,Business,Virginia Tech,4.1,4,75%,2.6
Anthony Vance,Business,Virginia Tech,3.8,3,34%,3.4
Joey Mccord,Business,Virginia Tech,1.4,3,0%,3.0
Ryan Musselman,Business,Virginia Tech,2.5,2,50%,3.0
Simone Bianco,Business,Virginia Tech,2.0,2,0%,4.0
Jim Dickhans,Business,Virginia Tech,1.0,2,0%,3.5
Kimberly Clark,Business,Virginia Tech,1.5,2,0%,3.5
Nima Zahadat,Business,Virginia Tech,3.5,2,50%,2.0
Duygu Pamukcu,Business,Virginia Tech,5.0,1,100%,3.0
Esmeralda Simpson,Business,Virginia Tech,3.0,1,100%,3.0
Eric Martin,Business,Virginia Tech,4.5,61,63%,3.6
Barbara Fraticelli,Business,Virginia Tech,4.8,23,91%,2.8
Manisha Singal,Business,Virginia Tech,1.6,11,0%,4.4
Chris Courtney,Business,Virginia Tech,3.1,12,42%,2.1
Jacob Shortt,Business,Virginia Tech,5.0,10,100%,3.4
David Bluey,Business,Virginia Tech,4.1,9,89%,2.4
Hailong Zhang,Business,Virginia Tech,4.1,7,58%,3.4
Jonathan Everett,Business,Virginia Tech,4.5,4,75%,3.2
Lindy Cranwell,Business,Virginia Tech,1.6,4,0%,4.4
Behnam Malmir,Business,Virginia Tech,5.0,2,100%,3.5
Wendi Pannell,Business,Virginia Tech,2.7,3,0%,2.3
Terry Rakes,Business,Virginia Tech,4.5,2,100%,3.5
Elise Elam,Business,Virginia Tech,5.0,2,100%,3.0
Mark Michalisin,Business,Virginia Tech,5.0,2,100%,2.5
Byung Kim,Business,Virginia Tech,4.5,1,N/A,2.0
Weiguo Fan,Business,Virginia Tech,5.0,1,N/A,2.0
Marcy Schnitzer,Business,Virginia Tech,1.0,1,0%,1.0
Wade Baker,Business,Virginia Tech,5.0,1,100%,3.0
Alan Abrahams,Business,Virginia Tech,5.0,1,100%,2.0
Dr. Jiayi Liu,Business,Virginia Tech,1.0,1,0%,3.0
Chun-Wei Lin (Kingway),Business,Virginia Tech,2.0,1,0%,3.0
Peter Banks,Business,Virginia Tech,0.0,0,N/A,0.0
Dixie Reaves,Business,Virginia Tech,0.0,0,N/A,0.0
LL Clark,Business,Virginia Tech,0.0,0,N/A,0.0
Janine Finnell,Business,Virginia Tech,0.0,0,N/A,0.0
Quinton Nottingham,Business,Virginia Tech,1.8,33,13%,4.5
Daniel Simundza,Business,Virginia Tech,4.8,23,79%,3.9
Tabitha James,Business,Virginia Tech,1.1,16,8%,4.5
Alice Jang,Business,Virginia Tech,2.0,13,8%,5.0
Lara Khansa,Business,Virginia Tech,4.7,12,100%,3.2
Jeremy Sudweeks,Business,Virginia Tech,3.7,13,85%,3.4
Jeffrey Robert,Business,Virginia Tech,5.0,9,100%,3.1
G. Alan Wang,Business,Virginia Tech,3.6,5,67%,3.1
Jimmie Flores,Business,Virginia Tech,1.3,4,0%,3.2
John Travers,Business,Virginia Tech,3.3,4,50%,3.8
Vitali Mindel,Business,Virginia Tech,4.6,5,80%,1.4
Laura Khanza,Business,Virginia Tech,3.8,2,N/A,3.0
Jack McDonald,Business,Virginia Tech,5.0,2,50%,3.0
Bryan Hertweck,Business,Virginia Tech,4.5,2,100%,1.5
Lisa Fournier,Business,Virginia Tech,4.0,2,100%,2.5
Dawn McEvoy,Business,Virginia Tech,5.0,2,100%,1.5
Cliff Ragsdale,Business,Virginia Tech,5.0,1,100%,3
Onur Seref,Business & Info. Technology,Virginia Tech,2.9,19,56%,N/A
Stephen Martin,Chemical Engineering,Virginia Tech,0.0,0,N/A,0.0
Erdogan Kiran,Chemical Engineering,Virginia Tech,2.5,2,50%,2.5
Richey Davis,Chemical Engineering,Virginia Tech,1.3,3,0%,4.0
Aaron Goldstein,Chemical Engineering,Virginia Tech,0.0,0,N/A,0.0
Hongliang Xin,Chemical Engineering,Virginia Tech,0.0,0,N/A,0.0
Patricia Amateis,Chemistry,Virginia Tech,4.5,93,94%,3.1
Ketan Trivedi,Chemistry,Virginia Tech,3.4,42,N/A,3.2
Brian Hanson,Chemistry,Virginia Tech,1.8,21,25%,4.2
Brian Tissue,Chemistry,Virginia Tech,2.0,15,0%,3.7
Diego Troya,Chemistry,Virginia Tech,3.6,10,58%,4.0
Felicia Etzkorn,Chemistry,Virginia Tech,1.4,7,N/A,3.4
Paul Carlier,Chemistry,Virginia Tech,3.3,6,100%,3.7
Timothy Long,Chemistry,Virginia Tech,4.6,6,100%,2.4
Karen Brewer,Chemistry,Virginia Tech,4.5,5,N/A,3.0
Bruce Orler,Chemistry,Virginia Tech,1.4,3,0%,4.8
Shannon Saluga,Chemistry,Virginia Tech,0.0,0,N/A,0.0
Candace Wall,Chemistry,Virginia Tech,4.5,79,92%,3.4
Maggie Bump,Chemistry,Virginia Tech,4.9,51,66%,5.0
Paul Deck,Chemistry,Virginia Tech,3.4,45,65%,4.0
Michael Berg,Chemistry,Virginia Tech,5.0,40,96%,4.0
Daniel Crawford,Chemistry,Virginia Tech,5.0,17,100%,3.8
Michael Schulz,Chemistry,Virginia Tech,5.0,1,100%,2.0
Fatemeh Tohidi,Chemistry,Virginia Tech,5.0,1,100%,3.0
John Matson,Chemistry,Virginia Tech,0.0,0,N/A,0.0
Shamindri Arachchige,Chemistry,Virginia Tech,4.4,104,92%,3.2
Alec Wagner,Chemistry,Virginia Tech,4.2,77,80%,3.3
Joseph Merola,Chemistry,Virginia Tech,4.5,13,100%,3.1
Rosie Tohidi,Chemistry,Virginia Tech,2.6,10,40%,3.3
Edward Valeyev,Chemistry,Virginia Tech,3.3,6,50%,3.8
John Zobac,Chemistry,Virginia Tech,5.0,4,100%,4.0
Marwa (mar) Abdel Latif,Chemistry,Virginia Tech,2.9,4,0%,3.0
Emily Gentry,Chemistry,Virginia Tech,5.0,2,100%,2.0
Feng Lin,Chemistry,Virginia Tech,5.0,1,100%,3.0
Jeannine Eddleton,Chemistry,Virginia Tech,3.9,84,57%,2.9
Preston Durrill,Chemistry,Virginia Tech,4.5,41,N/A,3.3
Kurt Neidigh,Chemistry,Virginia Tech,3.1,30,44%,3.8
Johnathan Bowen,Chemistry,Virginia Tech,5.0,28,90%,3.8
Aaron Geller,Chemistry,Virginia Tech,5.0,22,96%,3.5
Harry Dorn,Chemistry,Virginia Tech,3.9,11,100%,2.5
Amanda Morris,Chemistry,Virginia Tech,2.9,5,25%,4.4
Jatinder Josan,Chemistry,Virginia Tech,3.5,2,50%,3.0
James Tanko,Chemistry,Virginia Tech,5.0,2,100%,3.5
David Hobart,Chemistry,Virginia Tech,5.0,1,N/A,3.0
David Kingston,Chemistry,Virginia Tech,4.5,1,N/A,1.0
Nick Sapienza,Chemistry,Virginia Tech,0.0,0,N/A,0.0
Victoria Long,Chemistry,Virginia Tech,1.5,120,8%,4.3
Gary Long,Chemistry,Virginia Tech,4.3,24,100%,2.1
Gordon Yee,Chemistry,Virginia Tech,4.4,23,56%,3.5
Cynthia Cribbs,Chemistry,Virginia Tech,2.5,14,N/A,3.9
Claire Santos,Chemistry,Virginia Tech,1.9,12,17%,4.3
Alan Esker,Chemistry,Virginia Tech,3.3,9,67%,4.4
Rich Gandour,Chemistry,Virginia Tech,3.9,8,100%,3.3
John Morris,Chemistry,Virginia Tech,4.3,7,N/A,3.4
Avijita Jain,Chemistry,Virginia Tech,3.3,7,0%,2.6
Philippe Bissel,Chemistry,Virginia Tech,1.1,4,N/A,4.3
Michael Schultz,Chemistry,Virginia Tech,1.0,3,0%,5.0
Neil McAlpine,Chemistry,Virginia Tech,4.8,3,100%,2.0
Mary Olson,Chemistry,Virginia Tech,0.0,0,N/A,0.0
Lina Quan,Chemistry,Virginia Tech,0.0,0,N/A,0.0
Deborah Young-Corbett,Civil Engineering,Virginia Tech,5.0,1,N/A,3.0
Joseph Dove,Civil Engineering,Virginia Tech,5.0,1,100%,3.0
Jingqiu Liao,Civil Engineering,Virginia Tech,0.0,0,N/A,0.0
Mehdi Setareh,Civil Engineering,Virginia Tech,3.9,21,60%,3.4
Dewey Spangler,Civil Engineering,Virginia Tech,2.2,11,0%,4.5
Nina Stark,Civil Engineering,Virginia Tech,4.8,2,N/A,2.5
Kathleen Hancock,Civil Engineering,Virginia Tech,5.0,2,100%,3.0
Monica Arul,Civil Engineering,Virginia Tech,3.0,1,100%,4.0
William Cox,Civil Engineering,Virginia Tech,0.0,0,N/A,0.0
Erich Hester,Civil Engineering,Virginia Tech,0.0,0,N/A,0.0
Reihaneh Hosseini,Civil Engineering,Virginia Tech,0.0,0,N/A,0.0
Kevin Young,Civil Engineering,Virginia Tech,4.9,7,100%,2.8
Bryan Katz,Civil Engineering,Virginia Tech,5.0,6,100%,2.0
Maryam Shakiba,Civil Engineering,Virginia Tech,2.7,3,34%,3.7
Antonio Trani,Civil Engineering,Virginia Tech,5.0,2,100%,2.0
K. B. Rojiani,Civil Engineering,Virginia Tech,4.8,2,N/A,2.0
Rodrigo Sarlo,Civil Engineering,Virginia Tech,5.0,1,100%,2.0
Kyle Strom,Civil Engineering,Virginia Tech,3.0,1,100%,4.0
Guney Olgun,Civil Engineering,Virginia Tech,3.5,1,N/A,2.0
Sogand Hasanzadeh,Civil Engineering,Virginia Tech,0.0,0,N/A,0.0
Celal Olgun,Civil Engineering,Virginia Tech,0.0,0,N/A,0.0
Sherif Abdelaziz,Civil Engineering,Virginia Tech,0.0,0,N/A,0.0
Adil Godrej,Civil Engineering,Virginia Tech,0.0,0,N/A,0.0
Claire White,Civil Engineering,Virginia Tech,3.9,6,67%,2.8
Christine Steer,Classics,Virginia Tech,2.6,14,29%,3.7
Andrew Becker,Classics,Virginia Tech,0.0,0,N/A,0.0
Trudy Becker,Classics,Virginia Tech,4.6,24,91%,2.3
Beth Waggenspack,Communication,Virginia Tech,3.8,30,50%,3.6
Susan Stinson,Communication,Virginia Tech,4.4,13,85%,2.1
Lincoln Costello,Communication,Virginia Tech,4.5,11,82%,2.1
Laura Purcell,Communication,Virginia Tech,2.1,11,28%,3.0
Claire Boor,Communication,Virginia Tech,4.6,6,100%,3.0
Lujean Baab,Communication,Virginia Tech,1.0,4,0%,3.3
Roland Lazenby,Communication,Virginia Tech,3.7,3,N/A,2.3
Dan Tamul,Communication,Virginia Tech,1.0,3,0%,4.0
Bill Roth,Communication,Virginia Tech,4.8,3,100%,1.0
Kelsey Curry,Communication,Virginia Tech,5.0,2,100%,1.0
Brandi Quesenberry,Communication,Virginia Tech,0.0,0,N/A,0.0
Jared Woolly,Communication,Virginia Tech,4.6,6,84%,2.8
Katie Thomas,Communication,Virginia Tech,4.6,5,80%,2.6
Sam Riley,Communication,Virginia Tech,3.9,4,N/A,3.5
Matthew Vandyke,Communication,Virginia Tech,5.0,2,100%,2.0
Derley Booth,Communication,Virginia Tech,4.0,1,N/A,1.0
Jordan Wolf,Communication,Virginia Tech,5.0,1,100%,2.0
Buddy Howell,Communication,Virginia Tech,4.4,64,88%,2.9
Stephen Prince,Communication,Virginia Tech,3.4,22,75%,3.2
Jim Kuypers,Communication,Virginia Tech,3.1,18,25%,4.5
Jennifer MacKay,Communication,Virginia Tech,2.4,8,25%,3.2
Emma Mulvaney,Communication,Virginia Tech,3.3,3,50%,3.8
R Magee,Communication,Virginia Tech,5.0,3,N/A,1.7
Cayce Myers,Communication,Virginia Tech,2.0,2,50%,5.0
Cemone Paul,Communication,Virginia Tech,5.0,1,100%,1.0
Marlene Preston,Communication,Virginia Tech,5.0,1,N/A,2.0
Derley Aguilar Booth,Communication,Virginia Tech,5.0,1,N/A,3.0
Yi-Chun Yvonnes Chen,Communication,Virginia Tech,4.5,1,N/A,3.0
Veronica Giron,Communication,Virginia Tech,5.0,1,100%,2.0
Claire Hudson,Communication,Virginia Tech,0.0,0,N/A,0.0
Dorothy Conner,Communication,Virginia Tech,4.8,25,100%,2.5
Erik Kanter,Communication,Virginia Tech,3.7,23,N/A,3.0
Steve Matuszak,Communication,Virginia Tech,2.5,21,24%,3.8
Zack Sowder,Communication,Virginia Tech,4.8,15,100%,2.3
Hannah Shinualt,Communication,Virginia Tech,4.1,11,63%,2.8
Michael Horning,Communication,Virginia Tech,4.4,10,100%,3.5
Watt Hopkins,Communication,Virginia Tech,2.6,6,0%,4.8
Martin Cassady,Communication,Virginia Tech,5.0,7,100%,2.0
Emilie Tydings,Communication,Virginia Tech,3.8,4,N/A,2.8
Nneka Logan,Communication,Virginia Tech,5.0,1,100%,3.0
Lizzie Mahan,Communication,Virginia Tech,0.0,0,N/A,0.0
Dale Jenkins,Communication,Virginia Tech,4.4,24,67%,3.5
Syrenthia Robinson,Communication,Virginia Tech,1.4,17,13%,4.4
Hannah Shinault,Communication,Virginia Tech,4.3,7,72%,3.4
Kacy McAllister,Communication,Virginia Tech,5.0,6,100%,2.8
Rachel Holloway,Communication,Virginia Tech,3.8,4,N/A,4.5
DH Young,Communication,Virginia Tech,3.6,4,N/A,2.5
Mark Bond,Communication,Virginia Tech,4.2,3,100%,1.7
Olivia Moyer,Communication,Virginia Tech,5.0,3,100%,2.4
Ancheska Parchman,Communication,Virginia Tech,4.8,4,100%,1.8
Douglas Cannon,Communication,Virginia Tech,4.0,2,100%,1.5
Joshua Delung,Communication,Virginia Tech,5.0,2,N/A,3.5
Megan Duncan,Communication,Virginia Tech,4.0,2,100%,3.5
Natalia Mielczarek,Communication,Virginia Tech,5.0,2,100%,3.0
Ann Brown,Communication,Virginia Tech,3.0,2,0%,2.0
Nicole Verdin,Communication,Virginia Tech,5.0,2,100%,2.5
Patrick Dacey,Communication,Virginia Tech,3.0,1,N/A,2.0
Meghan Tice,Communication,Virginia Tech,4.5,1,N/A,3.0
Katherine Haenschen,Communication,Virginia Tech,0.0,0,N/A,0.0
Jean Jadhon,Communication,Virginia Tech,0.0,0,N/A,0.0
Marcus Meyers,Communication,Virginia Tech,0.0,0,N/A,0.0
Godmar Back,Computer Science,Virginia Tech,3.8,21,74%,4.6
Lindah Kotut,Computer Science,Virginia Tech,2.8,16,44%,4.0
Stephen Edwards,Computer Science,Virginia Tech,2.1,16,25%,4.5
Yang Cao,Computer Science,Virginia Tech,2.0,13,19%,4.9
Siwei Cao,Computer Science,Virginia Tech,2.3,9,23%,2.8
Daniel Dunlap,Computer Science,Virginia Tech,5.0,6,100%,1.3
Allyson Senger,Computer Science,Virginia Tech,3.1,5,60%,4.1
Derek Haqq,Computer Science,Virginia Tech,3.6,5,60%,2.5
Bimal Viswanath,Computer Science,Virginia Tech,1.0,4,0%,4.5
Naren Ramakrishnan,Computer Science,Virginia Tech,5.0,3,100%,4.0
Gregory Kulczycki,Computer Science,Virginia Tech,3.0,3,34%,3.4
Patrick Butler,Computer Science,Virginia Tech,1.0,2,0%,3.0
Jesse Harden,Computer Science,Virginia Tech,3.5,2,50%,2.5
Andrey Esakia,Computer Science,Virginia Tech,4.0,2,100%,2.0
B. Aditya Prakash,Computer Science,Virginia Tech,2.0,1,0%,4.0
Young Cao,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Heath Hillman,Computer Science,Virginia Tech,3.3,23,61%,3.1
Kenneth Stevens,Computer Science,Virginia Tech,2.1,13,34%,3.6
Dimitrios Nikolopoulos,Computer Science,Virginia Tech,3.9,8,63%,3.9
Elham Mohammadrezaei,Computer Science,Virginia Tech,1.6,5,20%,4.0
Randy Marchany,Computer Science,Virginia Tech,4.5,3,100%,3.0
Jiepu Jiang,Computer Science,Virginia Tech,3.7,3,67%,2.7
Henry Monti,Computer Science,Virginia Tech,1.2,3,N/A,4.3
Michael Irwin,Computer Science,Virginia Tech,4.5,2,100%,3.5
Xun Jian,Computer Science,Virginia Tech,1.5,2,0%,4.5
Martin Skarzynski,Computer Science,Virginia Tech,4.0,2,50%,1.5
TM Murali,Computer Science,Virginia Tech,1.0,2,0%,5.0
Shaddi Hasan,Computer Science,Virginia Tech,5.0,2,100%,3.0
Yoonjin Kim,Computer Science,Virginia Tech,1.0,1,0%,1.0
Brendan David-John,Computer Science,Virginia Tech,5.0,1,100%,2.0
Francisco Servant,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Muhammad Gulzar,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Amr Hilal,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Noah Barnette,Computer Science,Virginia Tech,2.0,51,28%,4.1
Margaret Ellis,Computer Science,Virginia Tech,2.4,29,36%,3.5
William McQuain,Computer Science,Virginia Tech,2.9,23,47%,4.3
John Wenskovitch,Computer Science,Virginia Tech,4.1,18,78%,2.9
Yalong Yang,Computer Science,Virginia Tech,1.3,14,0%,5.0
Andrew Kulak,Computer Science,Virginia Tech,1.5,8,13%,3.9
Onyeka Emebo,Computer Science,Virginia Tech,5.0,7,100%,2.5
Chris Thomas,Computer Science,Virginia Tech,5.0,6,100%,5.0
Eli Tilevich,Computer Science,Virginia Tech,4.1,4,75%,2.5
Farrokh Jazizadeh,Computer Science,Virginia Tech,3.5,2,50%,3.0
Andria Esakia,Computer Science,Virginia Tech,4.5,2,100%,1.5
Bob Edmison,Computer Science,Virginia Tech,2.5,2,50%,3.0
Shvetha Soundararajan,Computer Science,Virginia Tech,5.0,2,100%,1.5
Alexey Onufriev,Computer Science,Virginia Tech,1.0,1,0%,5.0
Wu-chun Feng,Computer Science,Virginia Tech,5.0,1,100%,2.0
Nikitha Chandrasheka,Computer Science,Virginia Tech,2.0,1,0%,2.0
Adrian Sandu,Computer Science,Virginia Tech,2.0,1,0%,5.0
Zachary Lytle,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Fatemah Sarshartehrani,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Donekal Chandrashekar,Computer Science,Virginia Tech,0.0,0,N/A,0.0
John Lewis,Computer Science,Virginia Tech,5.0,38,82%,3.6
David McPherson,Computer Science,Virginia Tech,4.3,32,84%,2.8
Patrick Sullivan,Computer Science,Virginia Tech,3.0,22,41%,4.1
Steven Edwards,Computer Science,Virginia Tech,1.9,12,0%,3.8
Taha Hassan,Computer Science,Virginia Tech,3.7,6,67%,3.8
Mohammed Farghally,Computer Science,Virginia Tech,4.9,7,100%,3.0
Csaba Egyhazy,Computer Science,Virginia Tech,2.1,4,100%,3.8
Eman Abdelrahman,Computer Science,Virginia Tech,4.4,3,100%,2.0
Poorvesh Dongre,Computer Science,Virginia Tech,2.0,3,0%,4.4
Khadijah Al Safwan,Computer Science,Virginia Tech,5.0,2,100%,1.5
Debswapna Bhattacharya,Computer Science,Virginia Tech,5.0,1,100%,3.0
Christopher Cuozzo,Computer Science,Virginia Tech,5.0,1,100%,1.0
Kirshanthan Sundararajah,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Edward Fox,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Osman Balci,Computer Science,Virginia Tech,2.4,14,17%,4.4
Lifu Huang,Computer Science,Virginia Tech,1.5,9,0%,4.5
Denis Gracanin,Computer Science,Virginia Tech,1.6,7,0%,4.4
Sally Hamouda,Computer Science,Virginia Tech,5.0,5,100%,2.1
Arinjoy Basak,Computer Science,Virginia Tech,2.0,5,20%,3.6
Anuj Karpatne,Computer Science,Virginia Tech,4.5,4,75%,3.5
Dennis Kafura,Computer Science,Virginia Tech,4.7,3,100%,2.7
Pinar Yanardag,Computer Science,Virginia Tech,3.4,3,67%,1.4
Ali Butt,Computer Science,Virginia Tech,4.5,2,100%,4.0
Layne Watson,Computer Science,Virginia Tech,1.0,2,0%,5.0
Sharath Raghvendra,Computer Science,Virginia Tech,3.0,2,50%,4.5
Richard Charles,Computer Science,Virginia Tech,5.0,2,100%,1.5
Srinidhi Varadarajan,Computer Science,Virginia Tech,1.0,1,N/A,5.0
Kurt Luther,Computer Science,Virginia Tech,5.0,1,100%,2.0
Peng Gao,Computer Science,Virginia Tech,1.0,1,0%,4.0
Dongyoon Lee,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Mai Dahshan,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Hoda Eldardiry,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Ahmad Khan,Computer Science,Virginia Tech,0.0,0,N/A,0.0
Tessema Mengistu,Computer Science,Virginia Tech,0.0,0,N/A,0
Onwubiko Agozino,Criminal Justice,Virginia Tech,1.0,12,0%,N/A
William White,Dairy Science,Virginia Tech,3.4,3,34%,2.0
Benjamin Corl,Dairy Science,Virginia Tech,2.0,1,0%,4.0
Isis Mullarky,Dairy Science,Virginia Tech,0.0,0,N/A,0.0
Jessica Pattison,Design,Virginia Tech,1.0,1,0%,4.0
Sarah Wilmot,Design,Virginia Tech,0.0,0,N/A,0.0
Eric Standley,Design,Virginia Tech,4.4,6,75%,3.0
Margaret Carneal,Design,Virginia Tech,2.5,2,0%,3.5
Hina Illahe,Design,Virginia Tech,0.0,0,N/A,0.0
John Cornthwait,Design,Virginia Tech,0.0,0,N/A,0.0
Renee Walsh,Design,Virginia Tech,3.1,14,43%,3.3
Eunju Hwang,Design,Virginia Tech,3.0,4,67%,2.5
Barbara Kraft-Leshyn,Design,Virginia Tech,5.0,2,N/A,1.0
Jeff Joiner,Design,Virginia Tech,3.0,1,100%,4.0
Marilyn Casto,Design,Virginia Tech,0.0,0,N/A,0.0
Deanna Alexander,Criminal Justice,Virginia Tech,4.5,2,100%,2.0
Melanie Kiechle,Criminal Justice,Virginia Tech,0.0,0,N/A,0.0
Gregory Novack,Criminal Justice,Virginia Tech,0.0,0,N/A,0.0
Stacey Clifton,Criminal Justice,Virginia Tech,5.0,3,100%,2.0
Thomas Dearden,Criminal Justice,Virginia Tech,4.0,1,100%,3.0
Constantinos Charalambous,Economics,Virginia Tech,4.8,16,N/A,2.3
Salehi-Isfahani,Economics,Virginia Tech,3.0,14,100%,3.6
Zhou Yang,Economics,Virginia Tech,3.0,9,45%,2.5
Matthew Kovach,Economics,Virginia Tech,3.8,6,84%,2.8
Dongryul Lee,Economics,Virginia Tech,2.3,4,0%,2.5
Michael Wagnon,Economics,Virginia Tech,3.4,5,40%,3.8
Brian D'Orazio,Economics,Virginia Tech,4.0,2,100%,2.0
Julien Cadot,Economics,Virginia Tech,4.0,1,100%,2.0
Hector Tzavellas,Economics,Virginia Tech,5.0,1,100%,2.0
Joshua Beverly,Economics,Virginia Tech,3.0,1,0%,4.0
Xu Lin,Economics,Virginia Tech,0.0,0,N/A,0.0
Yanyang Zou,Economics,Virginia Tech,0.0,0,N/A,0.0
Steve Trost,Economics,Virginia Tech,4.4,68,71%,3.9
Jadrian Wooten,Economics,Virginia Tech,4.5,54,91%,2.6
Nicolaus Tideman,Economics,Virginia Tech,3.9,4,100%,2.9
Arin Shahbazian,Economics,Virginia Tech,5.0,3,100%,3.3
Hans Haller,Economics,Virginia Tech,0.0,0,N/A,0.0
Priyambada Bandyopadhyay,Economics,Virginia Tech,0.0,0,N/A,0.0
Pitchayaporn Tantihkarnchana,Economics,Virginia Tech,2.5,43,33%,3.8
Sheryl Ball,Economics,Virginia Tech,1.9,8,20%,3.3
Karo Solat,Economics,Virginia Tech,1.2,5,0%,4.2
Yasin Arafat,Economics,Virginia Tech,1.7,3,0%,3.3
Thomas Debass,Economics,Virginia Tech,5.0,3,100%,2.4
Byron Tsang,Economics,Virginia Tech,3.3,2,100%,4.0
Suqin Ge,Economics,Virginia Tech,2.0,2,50%,3.0
Elinor Benami,Economics,Virginia Tech,3.0,1,100%,3.0
Zhenyu Yao,Economics,Virginia Tech,3.0,1,0%,3.0
Sergio Barrera,Economics,Virginia Tech,5.0,1,100%,2.0
Mohammad Banasaz,Economics,Virginia Tech,0.0,0,N/A,0.0
Mike Ellerbrock,Economics,Virginia Tech,5.0,80,88%,3.0
Gebremeskel Gebremariam,Economics,Virginia Tech,3.1,41,55%,3.2
Richard Cothren,Economics,Virginia Tech,2.6,19,34%,4.1
Erika Perdue,Economics,Virginia Tech,3.1,9,67%,2.6
Dixie Reaves,Economics,Virginia Tech,3.3,9,N/A,3.0
Pedro Vertino de Quieroz,Economics,Virginia Tech,1.8,3,0%,4.0
Pervesh Anthwal,Economics,Virginia Tech,2.5,2,0%,3.5
Djavad Salehi-Isfahani,Economics,Virginia Tech,4.0,1,N/A,5.0
Patti Fisher,Economics,Virginia Tech,5.0,1,100%,2.0
Byungki Mun,Economics,Virginia Tech,3.0,1,100%,1.0
Mark Liu,Economics,Virginia Tech,1.9,37,11%,4.9
Melanie Fox,Economics,Virginia Tech,3.4,25,44%,4.3
Amoz Kats,Economics,Virginia Tech,3.7,9,N/A,4.6
Azat Nurmukhametov,Economics,Virginia Tech,5.0,7,100%,1.6
Paul Hallmann,Economics,Virginia Tech,4.8,3,N/A,2.0
Richard Ashley,Economics,Virginia Tech,2.0,2,0%,3.5
Jason Zheng,Economics,Virginia Tech,1.0,1,N/A,2.0
Ahsan Ahsanuzzaman,Economics,Virginia Tech,4.5,1,N/A,4.0
Sapna Kaul,Economics,Virginia Tech,5.0,1,N/A,3.0
Abdelaziz Alsharawy,Economics,Virginia Tech,5.0,1,100%,4.0
Niloy Bose,Economics,Virginia Tech,2.0,1,0%,3.0
Wei Zhang,Economics,Virginia Tech,0.0,0,N/A,0.0
Sunjin Kim,Economics,Virginia Tech,0.0,0,N/A,0.0
Chao Chan,Economics,Virginia Tech,0.0,0,N/A,0.0
Sarah Lyon-Hill,Economics,Virginia Tech,0.0,0,N/A,0.0
Rhonda Phillips,Education,Virginia Tech,5.0,1,100%,N/A
Virgilio Centeno,Electrical & Computer Engineering,Virginia Tech,4.0,5,80%,4.0
Ryan Gerdes,Electrical & Computer Engineering,Virginia Tech,1.0,3,0%,4.4
William Adams,Electrical & Computer Engineering,Virginia Tech,0.0,0,N/A,0.0
Ryan Williams,Electrical & Computer Engineering,Virginia Tech,5.0,3,100%,3.0
Changwoo Min,Electrical & Computer Engineering,Virginia Tech,3.0,1,100%,3.0
Dong Dong,Electrical & Computer Engineering,Virginia Tech,1.0,1,0%,5.0
Binoy Ravindran,Electrical & Computer Engineering,Virginia Tech,0.0,0,N/A,0.0
Tyler Milburn,Electrical & Computer Engineering,Virginia Tech,5.0,4,100%,3.0
Haibo Zeng,Electrical & Computer Engineering,Virginia Tech,2.5,2,50%,2.5
Jaime De La Ree,Electrical & Computer Engineering,Virginia Tech,5.0,1,100%,4.0
Dong Ha,Electrical & Computer Engineering,Virginia Tech,2.0,1,0%,4.0
Yaling Yang,Electrical & Computer Engineering,Virginia Tech,1.0,2,0%,2.5
Kendal Giles,Electrical & Computer Engineering,Virginia Tech,0.0,0,N/A,0.0
Leyla Nazhandali,Electrical & Computer Engineering,Virginia Tech,5.0,7,100%,2.4
Yue Wang,Electrical & Computer Engineering,Virginia Tech,1.0,1,0%,5.0
William Baumann,Electrical & Computer Engineering,Virginia Tech,5.0,1,100%,3.0
Dushan Boroyevich,Electrical & Computer Engineering,Virginia Tech,0.0,0,N/A,0.0
David Kniola,Education,Virginia Tech,5.0,1,100%,1.0
Amanda Walters,Education,Virginia Tech,2.0,1,0%,4.0
Tom Williams,Education,Virginia Tech,4.5,2,N/A,3.0
Kusum Singh,Education,Virginia Tech,2.5,2,N/A,4.0
Hande Soysal,Education,Virginia Tech,0.0,0,N/A,0.0
Mido Chang,Education,Virginia Tech,4.3,2,N/A,3.0
Michael Evans,Education,Virginia Tech,1.5,2,N/A,4.5
Laura Welfare,Education,Virginia Tech,4.0,1,100%,1.0
Jamie Little,Education,Virginia Tech,5.0,1,N/A,3.0
Hande Fenerci,Education,Virginia Tech,5.0,1,100%,2.0
Billie Lepczyk,Education,Virginia Tech,5.0,5,100%,1.0
Bonnie Billingsley,Education,Virginia Tech,5.0,1,N/A,2.0
Dannette Gomez Beane,Education,Virginia Tech,4.0,1,100%,1.0
Marcus Weaver-Hightower,Education,Virginia Tech,3.0,1,0%,2.0
Yasuo Miyazaki,Education,Virginia Tech,0.0,0,N/A,0.0
Christine Christianson,Education,Virginia Tech,5.0,1,100%,3.0
Anne Shepherd,Education,Virginia Tech,0.0,0,N/A,0.0
Michael Ruohoniemi,Electrical Engineering,Virginia Tech,3.9,3,100%,2.8
Jordan Budhu,Electrical Engineering,Virginia Tech,3.0,2,50%,3.5
Hardus Odendaal,Electrical Engineering,Virginia Tech,1.5,1,N/A,1.0
Jason Lai,Electrical Engineering,Virginia Tech,5.0,1,N/A,2.0
Yaman Evrenosoglu,Electrical Engineering,Virginia Tech,5.0,1,N/A,4.0
Peter Athanas,Electrical Engineering,Virginia Tech,1.0,1,0%,4.0
Taiga Soejima,Electrical Engineering,Virginia Tech,0.0,0,N/A,0.0
Xiaoyu Zheng,Electrical Engineering,Virginia Tech,0.0,0,N/A,0.0
Tyler Milburn,Electrical Engineering,Virginia Tech,0.0,0,N/A,0.0
Elliott Mitchell-Colgan,Electrical Engineering,Virginia Tech,0.0,0,N/A,0.0
Douglas Nelson,Electrical Engineering,Virginia Tech,0.0,0,N/A,0.0
Arthur Ball,Electrical Engineering,Virginia Tech,4.5,32,82%,4.0
Mantu Hudait,Electrical Engineering,Virginia Tech,4.4,10,90%,3.0
Shuxiang Yu,Electrical Engineering,Virginia Tech,3.0,7,58%,4.4
Tamal Bose,Electrical Engineering,Virginia Tech,3.5,4,100%,3.8
Peter Han,Electrical Engineering,Virginia Tech,1.9,33,19%,4.3
Khai Ngo,Electrical Engineering,Virginia Tech,1.8,5,20%,3.2
Adnan Sarker,Electrical Engineering,Virginia Tech,2.6,5,20%,4.3
Wei Zhou,Electrical Engineering,Virginia Tech,4.0,2,50%,2.5
Luiz Silva,Electrical Engineering,Virginia Tech,3.5,1,N/A,2.0
Ravi Raghunathan,Electrical Engineering,Virginia Tech,1.0,1,0%,5.0
Mark Devito,Electrical Engineering,Virginia Tech,0.0,0,N/A,0.0
Yong Xu,Electrical Engineering,Virginia Tech,1.6,20,6%,4.5
Scott Dunning,Electrical Engineering,Virginia Tech,5.0,15,100%,3.4
Claudio Da Silva,Electrical Engineering,Virginia Tech,4.5,3,N/A,4.7
Robert Matthews,Electrical Engineering,Virginia Tech,1.0,1,0%,3.0
Chao Wang,Electrical Engineering,Virginia Tech,1.5,1,N/A,4.0
Jeff Walling,Electrical Engineering,Virginia Tech,0.0,0,N/A,0.0
Lingjia Liu,Electrical Engineering,Virginia Tech,0.0,0,N/A,0.0
Ting-Chung Poon,Electrical Engineering,Virginia Tech,2.6,7,40%,4.4
Thaddeus Black,Electrical Engineering,Virginia Tech,2.5,4,50%,3.8
Michael Hsiao,Electrical Engineering,Virginia Tech,3.5,4,100%,3.0
Mariusz Orlowski,Electrical Engineering,Virginia Tech,5.0,2,100%,2.5
Joseph Saifur Rahman,Electrical Engineering,Virginia Tech,1.0,1,N/A,4.0
Jia-Bin Huang,Electrical Engineering,Virginia Tech,1.0,1,0%,1.0
Yunhui Zhu,Electrical Engineering,Virginia Tech,4.0,1,100%,3.0
Jenny Lo,Engineering,Virginia Tech,5.0,46,100%,2.3
Benjamin Chambers,Engineering,Virginia Tech,5.0,25,96%,2.4
Ingrid St. Omer,Engineering,Virginia Tech,1.3,14,12%,4.4
Amrinder Nain,Engineering,Virginia Tech,2.3,10,40%,4.9
A Safaai-Jazi,Engineering,Virginia Tech,3.8,8,N/A,2.5
Patrick Devens,Engineering,Virginia Tech,3.1,7,N/A,3.1
Ronald Kriz,Engineering,Virginia Tech,1.7,7,N/A,3.4
Montasir Abbas,Engineering,Virginia Tech,3.6,5,0%,3.2
Nathan Lau,Engineering,Virginia Tech,3.6,5,100%,3
Kacie Hodges,Engineering,Virginia Tech,3.2,5,50%,3
Steve Rowson,Engineering,Virginia Tech,4.9,5,100%,1.3
Arefeh Mohammadi,Engineering,Virginia Tech,4.0,4,100%,2
Shena Davison,Engineering,Virginia Tech,5.0,4,100%,3.1
Gerardo Flintsch,Engineering,Virginia Tech,3.8,4,0%,4.3
Kevin Shinpaugh,Engineering,Virginia Tech,2.0,4,25%,3.6
Richard Goff,Engineering,Virginia Tech,4.3,3,100%,3
A. Lynn Abbott,Engineering,Virginia Tech,3.9,3,50%,3
Patrick Koelling,Engineering,Virginia Tech,3.0,1,0%,4
Larsen Ethan,Engineering,Virginia Tech,5.0,1,N/A,3
Holly Matusovich,Engineering,Virginia Tech,4.0,1,100%,1
Jeffery Mayer,Engineering,Virginia Tech,1.0,1,0%,5
Ryan Senger,Engineering,Virginia Tech,5.0,1,100%,3
Costin Untaroiu,Engineering,Virginia Tech,1.0,1,0%,4
Michael Hicks,Engineering,Virginia Tech,5.0,1,100%,2
Mark Howard,Engineering,Virginia Tech,0.0,0,N/A,0
Christopher Hall,Engineering,Virginia Tech,5.0,2,N/A,2
Jack Lesko,Engineering,Virginia Tech,2.8,2,N/A,3.5
Bevlee Watford,Engineering,Virginia Tech,1.5,1,N/A,5
Vickie Mouras,Engineering,Virginia Tech,5.0,1,N/A,3
Joel Nachlas,Engineering,Virginia Tech,1.0,1,N/A,5
Jonathan Boreyko,Engineering,Virginia Tech,5.0,1,100%,3
Julia Kleponis,Engineering,Virginia Tech,5.0,1,100%,3
Ashtarout Ammar,Engineering,Virginia Tech,5.0,1,100%,3
Sneha Davison,Engineering,Virginia Tech,5.0,26,97%,3.9
Sevak Tahmasian,Engineering,Virginia Tech,4.4,24,67%,4.3
Cassie Wallwey,Engineering,Virginia Tech,5.0,20,100%,2.4
David Gray,Engineering,Virginia Tech,5.0,20,100%,2.5
Sajad Khodadadian,Engineering,Virginia Tech,1.8,20,15%,4.9
Jason Thweatt,Engineering,Virginia Tech,4.8,17,84%,3.5
Nakhiah Goulbourne,Engineering,Virginia Tech,1.5,12,N/A,4.1
Hesham Elmkharram,Engineering,Virginia Tech,1.3,11,0%,4.8
Tom Walker,Engineering,Virginia Tech,2.6,8,N/A,3.3
Joseph Tront,Engineering,Virginia Tech,3.7,7,N/A,3.7
Eunsil Lee,Engineering,Virginia Tech,4.4,7,86%,2.4
Suneel Kodambaka,Engineering,Virginia Tech,1.9,7,15%,4.5
Matthew Rice,Engineering,Virginia Tech,3.0,5,75%,3.8
Joseph Meadows,Engineering,Virginia Tech,4.0,5,60%,3.6
Kichol Lee,Engineering,Virginia Tech,1.0,3,0%,3.7
Scott Case,Engineering,Virginia Tech,4.7,3,100%,3
Adam Barnes,Engineering,Virginia Tech,3.7,3,67%,4.3
Daniel Dudek,Engineering,Virginia Tech,4.5,2,100%,3
Richard Cooper,Engineering,Virginia Tech,4.8,2,100%,3
Rakesh Kapania,Engineering,Virginia Tech,2.5,3,50%,3.7
Scott Sink,Engineering,Virginia Tech,1.0,3,0%,5
Marie Paretti,Engineering,Virginia Tech,4.5,2,100%,3
Laura Savage,Engineering,Virginia Tech,3.5,2,50%,2.5
Mark Huerta,Engineering,Virginia Tech,5.0,2,100%,1
Alejandro Salado,Engineering,Virginia Tech,1.0,2,0%,5
John Little,Engineering,Virginia Tech,1.0,2,0%,4.5
John Cundiff,Engineering,Virginia Tech,4.3,2,N/A,2
Kang Xia,Engineering,Virginia Tech,0.0,0,N/A,0
Zhiwu Wang,Engineering,Virginia Tech,0.0,0,N/A,0
Melissa Kenny,Engineering,Virginia Tech,0.0,0,N/A,0
Po-Jen Shih,Engineering,Virginia Tech,0.0,0,N/A,0
David Grey,Engineering,Virginia Tech,0.0,0,N/A,0
Juhong Chen,Engineering,Virginia Tech,0.0,0,N/A,0
Justin Dubik,Engineering,Virginia Tech,0.0,0,N/A,0
Hanna Kindlund,Engineering,Virginia Tech,0.0,0,N/A,0
Curt Portfield,Engineering,Virginia Tech,0.0,0,N/A,0
Kristie Cooper,Engineering,Virginia Tech,3.3,51,55%,4.4
Hodjat Pendar,Engineering,Virginia Tech,4.4,29,63%,4.6
Brian Vick,Engineering,Virginia Tech,1.7,30,15%,4
Catherine Twyman,Engineering,Virginia Tech,4.4,26,77%,2.1
James Lord,Engineering,Virginia Tech,4.8,13,92%,3.5
Tamara Knott,Engineering,Virginia Tech,2.7,11,N/A,3.6
Maura Borrego,Engineering,Virginia Tech,4.0,8,100%,2.8
Michael Buehrer,Engineering,Virginia Tech,4.6,8,100%,4
Hanif Sherali,Engineering,Virginia Tech,5.0,7,100%,2.8
Kevin Young,Engineering,Virginia Tech,5.0,7,100%,2.9
Conrad Heatwole,Engineering,Virginia Tech,3.5,6,N/A,2.5
Ashish Agrawal,Engineering,Virginia Tech,1.7,6,0%,3.3
Alkan Soysal,Engineering,Virginia Tech,3.8,6,67%,3
Darren Maczka,Engineering,Virginia Tech,5.0,5,100%,2.6
Win Nguyen,Engineering,Virginia Tech,5.0,5,100%,2
Ranga Pitchumani,Engineering,Virginia Tech,2.1,5,0%,4.9
Scott Gallimore,Engineering,Virginia Tech,4.6,4,N/A,2.5
D T Mook,Engineering,Virginia Tech,3.0,4,N/A,3
Tawni Paradise,Engineering,Virginia Tech,5.0,2,100%,N/A
Jr Voshell,Entomology,Virginia Tech,4.2,10,N/A,2.1
Steven Hiner,Entomology,Virginia Tech,4.2,8,N/A,1.8
John Reid,Environment,Virginia Tech,5.0,1,100%,3
Meredith Steele,Environment,Virginia Tech,4.4,7,86%,2.5
Donald Orth,Environment,Virginia Tech,4.0,3,67%,3
Leigh Anne Krometis,Environment,Virginia Tech,2.0,2,50%,3
Heather Abernathy,Environment,Virginia Tech,1.0,2,0%,5
Thomas Galligan,Environment,Virginia Tech,1.0,1,0%,5
Valerie Thomas,Environment,Virginia Tech,4.0,1,100%,3
Holly Kindavater,Environment,Virginia Tech,0.0,0,N/A,0
Alasdair Cohen,Environment,Virginia Tech,5.0,4,100%,2.8
Marc Stern,Environment,Virginia Tech,0.0,0,N/A,0
Brian Strahm,Environment,Virginia Tech,5.0,14,100%,2.1
Kieran Lindsey,Environment,Virginia Tech,5.0,1,100%,3
Daniel Breslau,Environment,Virginia Tech,0.0,0,N/A,0
Hamilton Turner,Engineering,Virginia Tech,5.0,1,100%,3
Prahalada Rao,Engineering,Virginia Tech,4.0,1,100%,3
Emily Dogan,Engineering,Virginia Tech,5.0,1,100%,2
Ozan Sert,Engineering,Virginia Tech,4.0,1,100%,3
Thidapat Chantem,Engineering,Virginia Tech,4.0,1,100%,3
Sreenivasulu Gollapudi,Engineering,Virginia Tech,0.0,0,N/A,0
Kevin Kochersberger,Engineering,Virginia Tech,1.0,1,0%,2
Christian Wernz,Engineering,Virginia Tech,0.0,0,N/A,0
Joseph Schetz,Engineering,Virginia Tech,0.0,0,N/A,0
Qin Zhu,Engineering,Virginia Tech,0.0,0,N/A,0
Tom Powers,Engineering,Virginia Tech,0.0,0,N/A,0
Bart Raeymaekers,Engineering,Virginia Tech,1.0,1,0%,5
Wei-Jer (Peter) Han,Engineering,Virginia Tech,0.0,0,N/A,0
Robert West,Environmental Science,Virginia Tech,3.1,3,0%,N/A
Mae Hey,Ethnic Studies,Virginia Tech,4.6,4,100%,1.6
Paulo Polanah,Ethnic Studies,Virginia Tech,4.5,21,80%,2.5
Justin Perkinson,Film,Virginia Tech,4.0,1,100%,2
Arthur Keown,Finance,Virginia Tech,4.0,24,79%,3.1
Audra Price,Finance,Virginia Tech,4.8,15,87%,4
Shahram Amini,Finance,Virginia Tech,4.8,9,100%,3.9
Sara Easterwood,Finance,Virginia Tech,3.4,4,50%,4.1
Sophia Anong,Finance,Virginia Tech,3.0,3,N/A,2
Christine Damico,Finance,Virginia Tech,5.0,2,100%,4
Yessenia Tellez,Finance,Virginia Tech,1.0,2,0%,5
George Morgan,Finance,Virginia Tech,1.8,2,N/A,4
Gregory Kadlec,Finance,Virginia Tech,0.0,0,N/A,0
Ye Pengfei,Finance,Virginia Tech,0.0,0,N/A,0
Elesha Wikle,Finance,Virginia Tech,4.5,21,91%,2.6
Jacob Powell,Finance,Virginia Tech,2.6,19,37%,3.7
Kevin Sullivan,Finance,Virginia Tech,4.2,7,N/A,3.9
Elizabeth Goldsmith,Finance,Virginia Tech,5.0,1,100%,2
Roger Edelen,Finance,Virginia Tech,5.0,1,100%,4
Emir Hrnjic,Finance,Virginia Tech,5.0,1,N/A,2
Elizabeth Bickmore,Finance,Virginia Tech,0.0,0,N/A,0
Alex White,Finance,Virginia Tech,4.9,24,100%,1.5
Jason Malone,Finance,Virginia Tech,4.9,20,91%,4
Stephen Skripak,Finance,Virginia Tech,4.8,10,100%,2.8
John Easterwood,Finance,Virginia Tech,3.0,10,50%,4.5
Jamie Lynn Byram,Finance,Virginia Tech,3.0,2,50%,3
Pengfei Ye,Finance,Virginia Tech,5.0,1,100%,2
Don Andree,Finance,Virginia Tech,1.0,1,0%,4
Fred Hood,Finance,Virginia Tech,2.0,1,0%,4
Josiah Showalter,Finance,Virginia Tech,5.0,43,100%,2.8
Brian Hart,Finance,Virginia Tech,2.9,36,53%,3.9
Bradley Paye,Finance,Virginia Tech,5.0,11,82%,4
Derek Klock,Finance,Virginia Tech,3.6,10,67%,4.1
Andrew MacKinlay,Finance,Virginia Tech,5.0,8,100%,3.8
Catherine Kennedy,Finance,Virginia Tech,1.5,5,0%,3.6
Mike Fleenor,Finance,Virginia Tech,4.7,3,100%,2.7
John Spicer,Finance,Virginia Tech,5.0,1,100%,3
Randall Billingsley,Finance,Virginia Tech,0.0,0,N/A,0
Cara Spicer,Finance,Virginia Tech,0.0,0,N/A,0
Michael Walsh,Finance,Virginia Tech,0.0,0,N/A,0
Dongsoo Choi,Fine Arts,Virginia Tech,0.0,0,N/A,0
Carol Burch-Brown,Fine Arts,Virginia Tech,3.8,3,N/A,2.3
Joy Rosenthal,Fine Arts,Virginia Tech,4.5,2,100%,2
Alexandra Leonetti,Fine Arts,Virginia Tech,4.8,4,100%,2.3
Travis Head,Fine Arts,Virginia Tech,0.0,0,N/A,0
Alan Weinstein,Fine Arts,Virginia Tech,4.9,19,100%,2
Phat Nguyen,Fine Arts,Virginia Tech,5.0,1,100%,2
Maria Cana Jimenez,Foreign Languages,Virginia Tech,4.9,7,100%,3.2
Aarnes Gudmestad,Foreign Languages,Virginia Tech,4.1,5,100%,2.5
Maria Jimenez,Foreign Languages,Virginia Tech,5.0,1,100%,3
Vinodh Venkatesh,Foreign Languages,Virginia Tech,5.0,1,100%,2
Addison Dalton,Foreign Languages,Virginia Tech,2.2,36,29%,3.9
David Delgado Lopez,Foreign Languages,Virginia Tech,5.0,7,100%,3.3
Elizabeth Shooltz,Foreign Languages,Virginia Tech,4.5,2,N/A,2
Jessica Folkart,Foreign Languages,Virginia Tech,0.0,0,N/A,0
Nancy Lopez-Romero,Foreign Languages,Virginia Tech,4.6,6,100%,2.5
Catalina Andrango-Walker,Foreign Languages,Virginia Tech,1.8,3,0%,3.4
Annie Hesp,Foreign Languages,Virginia Tech,5.0,10,100%,2.9
Julio Opazo,Foreign Languages,Virginia Tech,5.0,3,100%,2.4
Yumiko Younos,Foreign Languages,Virginia Tech,4.3,2,100%,2.5
Elisabeth Austin,Foreign Languages,Virginia Tech,5.0,1,100%,2
Rosa Ponton,Foreign Languages,Virginia Tech,4.0,1,100%,3
Ragheda Nassereddine,Foreign Languages,Virginia Tech,4.5,6,84%,4
Zac Zimmer,Foreign Languages,Virginia Tech,3.5,3,N/A,2.3
Javiera Jaque,Foreign Languages,Virginia Tech,5.0,1,100%,3
Jumana Al Ahmad,Foreign Languages,Virginia Tech,0.0,0,N/A,0
Phil Radtke,Forestry,Virginia Tech,2.8,11,28%,3.5
Rima Joseph,French,Virginia Tech,2.0,1,N/A,5
Sulagna Mishra,French,Virginia Tech,3.9,14,65%,4.3
Sharon Johnson,French,Virginia Tech,4.5,6,80%,3.3
Anthony Abiragi,French,Virginia Tech,4.7,3,N/A,1.7
Alexander Dickow,French,Virginia Tech,5.0,1,100%,1
C Noirot,French,Virginia Tech,3.3,7,50%,3.4
Francoise Mizutani-Rousseau,French,Virginia Tech,3.5,3,N/A,3.7
Richard Shryock,French,Virginia Tech,5.0,5,100%,3.9
M Gueye,French,Virginia Tech,4.0,5,N/A,1.2
Nicole Casto,French,Virginia Tech,4.3,4,75%,2.5
Bailey Filkoski,French,Virginia Tech,5.0,1,100%,3
JP Gannon,Geography,Virginia Tech,5.0,8,100%,2
Andrew Ellis,Geography,Virginia Tech,5.0,6,100%,2.6
Thomas Pingel,Geography,Virginia Tech,5.0,2,100%,2.5
Craig Ramseyer,Geography,Virginia Tech,5.0,7,100%,2
Timothy Baird,Geography,Virginia Tech,4.8,5,100%,2.4
Yang Shao,Geography,Virginia Tech,5.0,1,100%,2
John Boyer,Geography,Virginia Tech,4.6,166,80%,2
Lisa Kennedy,Geography,Virginia Tech,4.8,16,100%,2
Junghwan Kim,Geography,Virginia Tech,4.5,2,50%,2
Mandy Tew,Geography,Virginia Tech,3.0,1,100%,2
Stewart Scales,Geography,Virginia Tech,3.9,13,75%,3.4
David Carroll,Geography,Virginia Tech,5.0,11,100%,2
Luke Juran,Geography,Virginia Tech,0.0,0,N/A,0
Robert Oliver,Geography,Virginia Tech,4.6,28,79%,3.4
David Kramar,Geography,Virginia Tech,2.3,7,100%,4.4
Stephanie Zick,Geography,Virginia Tech,2.4,4,50%,3.6
Tom Hammett,Forestry,Virginia Tech,2.8,6,40%,3.5
Daniel Hindman,Forestry,Virginia Tech,5.0,3,100%,2.8
Joseph Loferski,Forestry,Virginia Tech,4.5,2,100%,2
Stephen Prisley,Forestry,Virginia Tech,5.0,1,N/A,1
Audrey Sharp,Forestry,Virginia Tech,4.0,1,100%,3
John Seiler,Forestry,Virginia Tech,4.5,2,100%,3
Gregory Amacher,Forestry,Virginia Tech,5.0,3,100%,3.3
Shep Zedaker,Forestry,Virginia Tech,5.0,1,N/A,1
Eric Wiseman,Forestry,Virginia Tech,4.0,7,100%,3.4
Randolph Wynne,Forestry,Virginia Tech,2.0,1,0%,3
Carrie Fearer,Forestry,Virginia Tech,0.0,0,N/A,0
John Munsell,Forestry,Virginia Tech,5.0,1,100%,4
James Spotila,Geology,Virginia Tech,4.5,31,65%,3
Shuhai Xiao,Geosciences,Virginia Tech,5.0,1,100%,3
Angela Pressinger,Geosciences,Virginia Tech,0.0,0,N/A,0
Laura Neser,Geosciences,Virginia Tech,4.9,26,97%,1.5
Megan Duncan,Geosciences,Virginia Tech,0.0,0,N/A,0
Robin Reed,Geosciences,Virginia Tech,4.0,1,100%,3
Marc Michel,Geosciences,Virginia Tech,5.0,1,100%,1
Angela Possinger,Geosciences,Virginia Tech,5.0,6,100%,2.6
Manoochehr Shirzaei,Geosciences,Virginia Tech,0.0,0,N/A,0
Richard Law,Geology,Virginia Tech,3.0,23,50%,3.6
John Chermak,Geology,Virginia Tech,4.0,15,80%,2.8
Luca Fedele,Geology,Virginia Tech,3.3,13,25%,2.7
Mark Caddick,Geology,Virginia Tech,0.0,0,N/A,0
Neil Johnson,Geology,Virginia Tech,3.1,57,45%,3.5
Kenneth Eriksson,Geology,Virginia Tech,3.5,10,N/A,3.2
Amanda Albright Olsen,Geology,Virginia Tech,5.0,1,100%,3
John Hole,Geology,Virginia Tech,2.0,14,22%,4.4
Mike Hochella,Geology,Virginia Tech,5.0,11,N/A,1.7
Martin Chapman,Geology,Virginia Tech,3.6,9,N/A,2.4
Philip Prince,Geology,Virginia Tech,3.7,3,N/A,3
Steve Holbrook,Geology,Virginia Tech,0.0,0,N/A,0
John Chermak,Geology,Virginia Tech,4.1,40,100%,2.5
Jennifer Sliko,Geology,Virginia Tech,2.1,6,N/A,3.7
Samuel Haines,Geology,Virginia Tech,4.8,3,100%,2
James Read,Geology,Virginia Tech,3.3,2,N/A,3
Ying Zhou,Geology,Virginia Tech,2.5,2,0%,3
Liesl Allingham,German,Virginia Tech,5.0,1,N/A,0
Audrey Ruple,Graduate Studies,Virginia Tech,1.0,1,0%,5
Andrea Bertke,Graduate Studies,Virginia Tech,0.0,0,N/A,0
Les Duffield,Graphic Arts,Virginia Tech,5.0,1,100%,3
Mariah Jones,Graphic Arts,Virginia Tech,3.8,12,67%,2.8
Ben Hannam,Graphic Arts,Virginia Tech,3.9,9,N/A,3.8
Dajana Nedic,Graphic Arts,Virginia Tech,5.0,1,100%,4
Esther Bauer,German,Virginia Tech,5.0,1,100%,4
Jay Layne,German,Virginia Tech,4.6,10,80%,3.3
Ryan Calder,Health Science,Virginia Tech,3.5,8,63%,0
James Robertson,History,Virginia Tech,3.7,18,100%,2.9
Reagan Shelton,History,Virginia Tech,3.4,8,N/A,3.5
Richard Hirsh,History,Virginia Tech,3.8,6,67%,4.6
A. Roger Ekirch,History,Virginia Tech,4.3,6,100%,2.2
Joshua Brinkman,History,Virginia Tech,4.0,6,84%,2.5
Earl Cherry,History,Virginia Tech,5.0,5,100%,2.4
Dave Zimring,History,Virginia Tech,4.4,4,N/A,2.3
Jessica Taylor,History,Virginia Tech,4.3,4,75%,2.5
Robert Stephens,History,Virginia Tech,4.5,4,100%,3.3
Nicholas Ganson,History,Virginia Tech,3.8,3,N/A,2.3
Linda Arnold,History,Virginia Tech,4.0,2,N/A,3.5
Jenni Gallagher,History,Virginia Tech,5.0,2,100%,2.5
Andrew Sorber,History,Virginia Tech,5.0,1,100%,3
Debra Skiles,History,Virginia Tech,3.9,5,60%,2.5
Warren Milteer,History,Virginia Tech,4.7,3,100%,1.3
Frederic J Baumgartner,History,Virginia Tech,3.8,3,N/A,2.7
Dennis Hidalgo,History,Virginia Tech,4.0,13,N/A,4.3
Taulby Edmondson,History,Virginia Tech,4.1,9,89%,3
David Murphree,History,Virginia Tech,4.2,9,N/A,2.3
NL Shumsky,History,Virginia Tech,1.6,7,N/A,4.1
Thomas Watkins,History,Virginia Tech,3.7,5,N/A,4
April Mayes,History,Virginia Tech,3.3,5,N/A,2.8
Bradley Nichols,History,Virginia Tech,4.8,4,75%,3.7
Edward Polanco,History,Virginia Tech,5.0,3,100%,4
Haywood Farrar,History,Virginia Tech,4.0,3,N/A,2
Drew Wallace,History,Virginia Tech,5.0,1,N/A,3
Heather Gumbert,History,Virginia Tech,3.5,11,40%,3.1
G.R. Bugh,History,Virginia Tech,3.9,10,60%,4.8
Anndal Narayanan,History,Virginia Tech,3.9,10,70%,3.4
Spenser Slough,History,Virginia Tech,4.5,2,100%,1.5
Joseph Bedford,History,Virginia Tech,4.0,2,50%,3.5
Paul Quigley,History,Virginia Tech,3.5,2,50%,2.5
Matt Heaton,History,Virginia Tech,5.0,2,100%,2.5
Helen Schneider,History,Virginia Tech,1.0,1,0%,3
Tom Ewing,History,Virginia Tech,5.0,1,100%,2
Michael Alexander,History,Virginia Tech,4.6,15,72%,2.8
Barbra Reeves,History,Virginia Tech,3.1,15,100%,3.6
Daniel Thorp,History,Virginia Tech,4.3,12,88%,4.1
Brett Shadle,History,Virginia Tech,3.2,6,100%,3.3
Peter Wallenstein,History,Virginia Tech,4.9,4,100%,2.6
Jordan Hill,History,Virginia Tech,5.0,3,N/A,2
Michael Meindl,History,Virginia Tech,2.7,3,34%,3.7
Arthur Ekirch,History,Virginia Tech,4.8,3,100%,3.4
Elizabeth McKagen,History,Virginia Tech,4.4,3,100%,2
Beverly Bunch-Lyons,History,Virginia Tech,5.0,2,100%,4
Michael Parmer,History,Virginia Tech,4.0,1,100%,1
Terry Findley,History,Virginia Tech,4.0,1,100%,2
Patricia Baker,History,Virginia Tech,0.0,0,N/A,0
Monamie Haines,History,Virginia Tech,0.0,0,N/A,0
Cornelia Deagle,Health Science,Virginia Tech,2.5,2,50%,1.5
Kris Osterberg,Health Science,Virginia Tech,4.5,1,N/A,1
Juliet Garrigan,Health Science,Virginia Tech,4.0,1,100%,4
Corrine Ruktanonchai,Health Science,Virginia Tech,5.0,1,100%,3
Boris Vinatzer,Health Science,Virginia Tech,0.0,0,N/A,0
Nicolin Girmes-Grieco,Health Science,Virginia Tech,5.0,14,100%,2.6
Kerry Redican,Health Science,Virginia Tech,4.9,7,100%,1
Angela Anderson,Health Science,Virginia Tech,4.8,10,100%,2.3
Deborah Good,Health Science,Virginia Tech,2.3,6,17%,3.8
Bobby Stephens,Health Science,Virginia Tech,1.0,4,0%,5
Michelle Rockwell,Health Science,Virginia Tech,5.0,4,100%,1.8
Amy Smith,Health Science,Virginia Tech,5.0,1,100%,1
Robert Granger,Health Science,Virginia Tech,0.0,0,N/A,0
Michele Lewis,Health Science,Virginia Tech,3.6,15,38%,2.7
Kristin Phillips,Health Science,Virginia Tech,4.8,12,84%,2.6
Jennie Hill,Health Science,Virginia Tech,3.2,3,N/A,4
Ashley Doyle-Lucas,Health Science,Virginia Tech,5.0,1,N/A,2
Pamela Ray,Health Science,Virginia Tech,1.0,1,0%,3
Ken Gates,Health Science,Virginia Tech,0.0,0,N/A,0
Kevin Wogenrich,Health Science,Virginia Tech,0.0,0,N/A,0
Pam Ray,Health Science,Virginia Tech,3.0,2,50%,4
Nick Ruktanonchai,Health Science,Virginia Tech,4.0,1,100%,3
Abby Fines,Health Science,Virginia Tech,0.0,0,N/A,0
Jake Reynolds,Health Science,Virginia Tech,0.0,0,N/A,0
Jim Tokuhisa,Horticulture,Virginia Tech,2.2,13,19%,0
Kimberly Soulek,Hospitality,Virginia Tech,5.0,2,100%,1
Kristin Lamoureux,Hospitality,Virginia Tech,5.0,1,100%,3
Annette Kangh,Hospitality,Virginia Tech,0.0,0,N/A,0
Candace Fitch,Hospitality,Virginia Tech,4.4,20,90%,2.3
Pierre Couture,Hospitality,Virginia Tech,3.1,4,N/A,1.8
Shaniel Bernard,Hospitality,Virginia Tech,5.0,2,100%,3.5
Stephen Foster,Hospitality,Virginia Tech,3.0,1,100%,2
Tarah Warner,Hospitality,Virginia Tech,3.5,7,58%,3.8
Hyoeun Kim,Hospitality,Virginia Tech,3.0,1,0%,3
HuiHui Zhang,Hospitality,Virginia Tech,0.0,0,N/A,0
Stuart Feigenbaum,Hospitality,Virginia Tech,2.5,34,29%,3.2
Howard Feiertag,Hospitality,Virginia Tech,4.0,4,N/A,1.5
Vincent Magnini,Hospitality,Virginia Tech,0.0,0,N/A,0
Kristen Houston,Hospitality,Virginia Tech,0.0,0,N/A,0
Ju Yeon Shin,Hospitality,Virginia Tech,1.3,9,12%,3.6
Tom Duetsch,Hospitality,Virginia Tech,5.0,2,100%,1
Rosemary Goss,Hospitality,Virginia Tech,0.0,0,N/A,0
Guopeng Cheng,Human Development,Virginia Tech,4.6,8,100%,0
Matthew Gabriele,Humanities,Virginia Tech,4.9,16,89%,3.3
Emily Satterwhite,Humanities,Virginia Tech,3.6,5,0%,2.6
Patrick Salmons,Humanities,Virginia Tech,3.0,3,67%,1.8
Helene Goetz,Humanities,Virginia Tech,4.0,1,100%,1
Kirby Spivey,Humanities,Virginia Tech,0.0,0,N/A,0
Komal Dhillon,Humanities,Virginia Tech,3.5,11,55%,3
Samuel Cook,Humanities,Virginia Tech,4.6,5,100%,2.2
Elizabeth McLain,Humanities,Virginia Tech,4.5,4,100%,2.5
Perry Martin,Humanities,Virginia Tech,5.0,4,100%,1.3
James Collier,Humanities,Virginia Tech,4.5,2,100%,2.5
Robin Kauffman,Humanities,Virginia Tech,4.5,1,N/A,1
Liora Goldensher,Humanities,Virginia Tech,0.0,0,N/A,0
Dominique Polanco,Humanities,Virginia Tech,4.0,5,80%,3
Stevan Jackson,Humanities,Virginia Tech,4.3,3,N/A,2
Dana Cochran,Humanities,Virginia Tech,5.0,3,N/A,1.3
Edward Gabor,Humanities,Virginia Tech,5.0,3,100%,4.4
JC Hennen,Humanities,Virginia Tech,0.0,0,N/A,0
Sky Wilhoit,Humanities,Virginia Tech,0.0,0,N/A,0
Marcia Davitt,Humanities,Virginia Tech,4.1,14,86%,2.4
Michael Saffle,Humanities,Virginia Tech,3.6,11,N/A,3.1
Jane Vance,Humanities,Virginia Tech,4.8,10,N/A,2
Esti Sheinberg,Humanities,Virginia Tech,3.4,9,N/A,3.2
Anita Puckett,Humanities,Virginia Tech,3.0,3,0%,3.3
Elizabeth (Betty) Fine,Humanities,Virginia Tech,3.0,2,N/A,2.5
Meredith Atanasio,Humanities,Virginia Tech,5.0,2,100%,2.5
CJ Roberts,Humanities,Virginia Tech,3.6,9,N/A,2.1
Aline De Souza,Humanities,Virginia Tech,3.9,6,67%,2.4
Jason Bowers,Humanities,Virginia Tech,4.8,5,100%,1.5
Philip Olson,Humanities,Virginia Tech,2.9,4,50%,3
Sam Winter,Humanities,Virginia Tech,5.0,4,100%,1.8
Danille Christensen,Humanities,Virginia Tech,4.4,3,67%,3.8
Lili Guan,Humanities,Virginia Tech,5.0,2,100%,1.5
LTC Carrie Cox,Humanities,Virginia Tech,0.0,0,N/A,0
Janene Roberts,Humanities,Virginia Tech,0.0,0,N/A,0
Sarah Plummer,Humanities,Virginia Tech,0.0,0,N/A,0
Carolyn Shivers,Human Development,Virginia Tech,4.9,7,86%,2.1
Caroline Sanner,Human Development,Virginia Tech,5.0,6,100%,1.6
Crystal Duncan Lane,Human Development,Virginia Tech,5.0,2,100%,1.5
Brandon Bigby,Human Development,Virginia Tech,4.5,1,N/A,3
Megan Dolbin-MacNab,Human Development,Virginia Tech,4.0,1,100%,3
Amy Morgan,Human Development,Virginia Tech,5.0,1,100%,1
Diana Devine,Human Development,Virginia Tech,5.0,1,100%,1
Natasha Cox,Human Development,Virginia Tech,0.0,0,N/A,0
Lauren Pittman,Human Development,Virginia Tech,5.0,1,100%,1
James Tillet,Human Development,Virginia Tech,0.0,0,N/A,0
Madelyn Toman,Human Development,Virginia Tech,0.0,0,N/A,0
Joyce Arditti,Human Development,Virginia Tech,3.8,4,N/A,2.8
Jou-Chen Chen,Human Development,Virginia Tech,2.0,3,N/A,4
Jason Austin,Human Development,Virginia Tech,4.0,1,N/A,1
Victoria Blanchard,Human Development,Virginia Tech,4.0,1,100%,4
Tina Savla,Human Development,Virginia Tech,5.0,1,N/A,5
Candy Beers,Human Development,Virginia Tech,5.0,1,100%,3
Jenene Case Pease,Human Development,Virginia Tech,0.0,0,N/A,0
Koeun Choi,Human Development,Virginia Tech,4.0,11,73%,2.5
Cynthia Smith,Human Development,Virginia Tech,3.6,10,N/A,2.9
Rose Wesche,Human Development,Virginia Tech,4.8,3,100%,1.4
Lea El Helou,Human Development,Virginia Tech,1.5,2,0%,3.5
Christine Kaestle,Human Development,Virginia Tech,5.0,2,100%,1.5
Duncan Lane,Human Development,Virginia Tech,0.0,0,N/A,0
Alexa Gardner,Human Development,Virginia Tech,0.0,0,N/A,0
Katie Barrow,Human Development,Virginia Tech,0.0,0,N/A,0
Shuqi Yu,Human Development,Virginia Tech,0.0,0,N/A,0
Matthew Komelski,Human Development,Virginia Tech,5.0,23,100%,2.1
Victoria Lael,Human Development,Virginia Tech,2.9,18,45%,3.4
Mary Ellen Verdu,Human Development,Virginia Tech,2.0,15,12%,1.9
Mark Benson,Human Development,Virginia Tech,4.5,2,N/A,3
Fred Piercy,Human Development,Virginia Tech,4.8,2,N/A,3.5
Benjamin Katz,Human Development,Virginia Tech,5.0,2,100%,3
Sara Neeves,Human Development,Virginia Tech,5.0,1,N/A,2
Krista Hein,Human Development,Virginia Tech,0.0,0,N/A,0
Matthew Spindler,Human Development,Virginia Tech,0.0,0,N/A,0
Steven Sheetz,Information Science,Virginia Tech,2.8,5,40%,0
Julie Schupp,International Studies,Virginia Tech,0.0,0,N/A,0
Kenneth Stiles,International Studies,Virginia Tech,3.9,10,50%,3.3
Sara Wenger,International Studies,Virginia Tech,4.5,2,100%,2.5
Jason Weidner,International Studies,Virginia Tech,4.5,1,N/A,3
I. Stivachtis,International Studies,Virginia Tech,3.4,23,37%,3.9
Leah Ramnath,International Studies,Virginia Tech,4.5,5,80%,2.5
Claire Apodaca,International Studies,Virginia Tech,2.3,3,34%,3.7
Giselle Datz,International Studies,Virginia Tech,5.0,1,100%,3
Ezgi Seref,International Studies,Virginia Tech,0.0,0,N/A,0
Scott Nelson,International Studies,Virginia Tech,2.5,26,19%,4.3
Sengul Yildiz-Alanbay,International Studies,Virginia Tech,3.9,6,67%,2.5
Nada Berrada,International Studies,Virginia Tech,1.5,2,0%,3
Charmayne Brown,Journalism,Virginia Tech,5.0,4,100%,1.9
Janet Wimmer,Journalism,Virginia Tech,0.0,0,N/A,0
Richard Phillips,Languages,Virginia Tech,5.0,16,100%,0
Janine Hiller,Law,Virginia Tech,3.5,2,50%,4
James Steiner,Law,Virginia Tech,5.0,1,100%,1
Daniel Cockrum,Law,Virginia Tech,4.5,4,100%,1
Elizabeth McClanahan,Law,Virginia Tech,5.0,1,100%,1
Mason Heidt,Law,Virginia Tech,0.0,0,N/A,0
Robert Hooper,Literature,Virginia Tech,4.6,12,84%,2.8
Avery Wiscomb,Literature,Virginia Tech,5.0,4,100%,1.6
Michael Sguerri,Languages,Virginia Tech,5.0,7,100%,2.9
Robert Efird,Languages,Virginia Tech,4.9,6,N/A,2.2
. Panford,Languages,Virginia Tech,3.5,5,N/A,2
Griselle Vargas,Languages,Virginia Tech,4.9,5,100%,3.2
William Bryce,Languages,Virginia Tech,4.5,1,N/A,1
Ana Alvarez Guillen,Languages,Virginia Tech,4.0,1,100%,2
Ahmad Azzam,Languages,Virginia Tech,5.0,1,100%,2
Sylvain Simmerman,Languages,Virginia Tech,5.0,1,100%,2
Tatiana McKagen,Languages,Virginia Tech,4.3,5,100%,2.4
Gonzalo Montero,Languages,Virginia Tech,4.5,2,100%,2
Navdeep Sokhey,Languages,Virginia Tech,4.5,2,100%,4
Masakao Onakado,Languages,Virginia Tech,2.0,2,0%,4
Alejandra Sobrado,Languages,Virginia Tech,5.0,6,100%,1.9
Marina Falasca,Languages,Virginia Tech,4.8,6,N/A,3
Melissa Coburn,Languages,Virginia Tech,5.0,3,100%,3
Caitlin Capone,Languages,Virginia Tech,5.0,1,100%,1
Andy Becker,Languages,Virginia Tech,4.7,8,N/A,2.5
Jacqueline Bixler,Languages,Virginia Tech,4.9,5,N/A,2.4
Elizabeth Calvera,Languages,Virginia Tech,4.9,4,N/A,2.3
June Stubbs,Languages,Virginia Tech,4.7,3,N/A,1
Sarah Sierra,Languages,Virginia Tech,4.6,8,100%,3.5
Charlie Farrington,Languages,Virginia Tech,3.9,8,63%,2.1
Rebecca Chang,Languages,Virginia Tech,5.0,5,100%,3.8
Nancy Lopez,Languages,Virginia Tech,4.8,4,100%,2
Teruyo Mercer,Languages,Virginia Tech,4.0,2,100%,3
Patrick Ridge,Languages,Virginia Tech,5.0,1,100%,4
Tammy Kemp,Management,Virginia Tech,5.0,4,100%,1.3
Charity Boyette,Management,Virginia Tech,4.0,2,50%,2.5
Richard Wokutch,Management,Virginia Tech,2.0,1,0%,3
Katy Cortes,Management,Virginia Tech,1.8,10,20%,3.4
Richard Curtis,Management,Virginia Tech,2.8,5,40%,4.2
David Townsend,Management,Virginia Tech,4.1,4,75%,3
David Williamson,Management,Virginia Tech,5.0,5,100%,1.6
Trey Lewis,Management,Virginia Tech,4.8,3,100%,2.8
Larry Alexander,Management,Virginia Tech,1.0,2,N/A,4.5
Christopher Barnes,Management,Virginia Tech,4.5,1,N/A,1
David Simpson,Management,Virginia Tech,2.0,1,0%,2
Ashley Benley,Management,Virginia Tech,0.0,0,N/A,0
Margaret Deck,Management,Virginia Tech,2.4,60,34%,3.7
Ron Poff,Management,Virginia Tech,4.9,37,100%,2.3
Polly Kiratikosolrak,Management,Virginia Tech,1.9,34,24%,3.9
Christopher Neck,Management,Virginia Tech,4.6,27,100%,2.8
Denise Cordova,Management,Virginia Tech,4.7,14,93%,3.1
Kevin Carlson,Management,Virginia Tech,4.4,10,72%,3.9
Laura Raschke,Management,Virginia Tech,2.8,9,45%,2.6
Elaine Humphrey,Management,Virginia Tech,1.0,7,0%,3.1
AK Ward,Management,Virginia Tech,5.0,4,100%,2.9
Danylle Kunkel,Management,Virginia Tech,4.3,3,N/A,3
Anthony Cobb,Management,Virginia Tech,2.0,2,0%,3.5
Kiran Awate,Management,Virginia Tech,5.0,1,100%,2
Philip Gibbs,Management,Virginia Tech,1.5,1,N/A,1
Dustin Read,Management,Virginia Tech,5.0,1,100%,4
Brandon White,Management,Virginia Tech,0.0,0,N/A,0
Phil Thompson,Management,Virginia Tech,5.0,17,89%,3
Steven Markham,Management,Virginia Tech,3.0,6,N/A,4.3
Jeffrey Arthur,Management,Virginia Tech,2.8,6,67%,3.1
Joseph Simpson,Management,Virginia Tech,3.9,6,50%,3
Dirk Buengel,Management,Virginia Tech,2.5,6,34%,4.2
Craig Hopkins,Management,Virginia Tech,1.0,6,0%,4.7
Kevin Cheng,Management,Virginia Tech,4.8,5,100%,1.8
Lori Anderson,Management,Virginia Tech,1.5,3,0%,4.5
Jerry Flynn,Management,Virginia Tech,3.0,1,100%,1
William Schaudt,Management,Virginia Tech,5.0,1,100%,4
Ashley Beleny,Management,Virginia Tech,2.4,31,26%,3.4
Max Stallkamp,Management,Virginia Tech,4.6,18,95%,2.4
Howard Haines,Management,Virginia Tech,4.9,12,84%,2.4
david lohr,Management,Virginia Tech,2.7,3,34%,2.7
Pakanat (Polly) Kiratikosolrak,Management,Virginia Tech,4.0,3,67%,2.4
Catherine Langford,Management,Virginia Tech,1.0,1,0%,3
Oliver Coutier-Delgosha,Marine Sciences,Virginia Tech,3.5,2,100%,0
Shreyans Goenka,Marketing,Virginia Tech,4.9,6,100%,2.8
Stephen Hood,Marketing,Virginia Tech,5.0,4,100%,2.6
Noreen Klein,Marketing,Virginia Tech,3.0,2,N/A,2
Ryan Horn,Marketing,Virginia Tech,5.0,2,100%,3
Eloise Coupey,Marketing,Virginia Tech,0.0,0,N/A,0
Donald Gresh,Marketing,Virginia Tech,0.0,0,N/A,0
Hari Ravella,Marketing,Virginia Tech,0.0,0,N/A,0
Carolyn Kogan,Marketing,Virginia Tech,0.0,0,N/A,0
Ni Jian,Marketing,Virginia Tech,0.0,0,N/A,0
Abdul Al-Jumaily,Marketing,Virginia Tech,2.8,36,42%,2.6
Paul Herr,Marketing,Virginia Tech,1.5,7,0%,4.9
Tom Reilly,Marketing,Virginia Tech,5.0,1,N/A,1
Shreyan Goenka,Marketing,Virginia Tech,2.0,1,0%,4
Yael Zemack Rugar,Marketing,Virginia Tech,2.8,5,0%,4.3
Frank May,Marketing,Virginia Tech,2.0,3,34%,3.8
Jennifer Hsu,Marketing,Virginia Tech,4.0,1,100%,2
Shilpa Rao,Marketing,Virginia Tech,0.0,0,N/A,0
Charley Swayne,Marketing,Virginia Tech,4.7,7,100%,1.7
Vicky Dierckx,Marketing,Virginia Tech,5.0,4,100%,2.4
Haribabu Ravella,Marketing,Virginia Tech,1.4,4,25%,2.5
Daniel Villanova,Marketing,Virginia Tech,4.0,3,67%,3.3
Randall McCrea,Marketing,Virginia Tech,4.0,2,100%,1.5
Laurel Schirr,Marketing,Virginia Tech,0.0,0,N/A,0
Donna Wertalik,Marketing,Virginia Tech,2.2,47,31%,2.7
Thomas Reilly,Marketing,Virginia Tech,2.3,9,34%,4.1
Monica Hillison,Marketing,Virginia Tech,2.0,5,40%,3
Keith Brophy,Marketing,Virginia Tech,1.6,5,0%,3.5
Rajesh Bagchi,Marketing,Virginia Tech,4.0,1,100%,4
Mario Pandelaere,Marketing,Virginia Tech,5.0,1,100%,4
Angela Yi,Marketing,Virginia Tech,5.0,1,100%,3
Jill Sundie,Marketing,Virginia Tech,0.0,0,N/A,0
Shilpa Madan,Marketing,Virginia Tech,0.0,0,N/A,0
Pankaj Kumar,Marketing,Virginia Tech,0.0,0,N/A,0
Myojoong Kim,Marketing,Virginia Tech,0.0,0,N/A,0
Sanja Pantic,Mathematics,Virginia Tech,1.5,30,7%,4.6
Myungsuk Chung,Mathematics,Virginia Tech,4.9,27,75%,3.6
Diane Agud,Mathematics,Virginia Tech,3.2,26,50%,3.6
Margaret McQuain,Mathematics,Virginia Tech,3.4,22,0%,2.7
Deborah Smith,Mathematics,Virginia Tech,2.0,21,N/A,3.1
Peter Caruso,Mathematics,Virginia Tech,3.8,18,56%,3.9
Carlos Nicolas,Mathematics,Virginia Tech,4.4,16,75%,3.5
Terri Bourden,Mathematics,Virginia Tech,1.7,15,N/A,3.7
John Pratt,Mathematics,Virginia Tech,2.8,11,46%,3.6
Martin Klaus,Mathematics,Virginia Tech,3.6,10,N/A,3.1
Brian Cook,Mathematics,Virginia Tech,3.3,10,50%,4.1
Evgeny Savel'Ev,Mathematics,Virginia Tech,2.1,9,N/A,4.0
Jessica StClair,Mathematics,Virginia Tech,4.5,9,89%,3.0
Pedro Soto,Mathematics,Virginia Tech,1.0,8,0%,5.0
Songul Aslan,Mathematics,Virginia Tech,3.3,7,58%,3.4
Eun Chang,Mathematics,Virginia Tech,4.5,7,100%,1.9
Everett Sullivan,Mathematics,Virginia Tech,1.9,9,34%,4.6
Alexander Elgart,Mathematics,Virginia Tech,3.1,7,50%,3.5
Rebecca McCarter,Mathematics,Virginia Tech,5.0,6,100%,3.5
Richard Sharpe,Mathematics,Virginia Tech,4.4,7,72%,2.6
Greg Riffe,Mathematics,Virginia Tech,4.0,5,N/A,2.6
Marcie Tiraphatna,Mathematics,Virginia Tech,3.0,4,50%,3.5
Josh Clemons,Mathematics,Virginia Tech,5.0,4,100%,2.6
Randall Cone,Mathematics,Virginia Tech,3.5,4,N/A,4.0
Jorge Reyes,Mathematics,Virginia Tech,5.0,4,100%,3.1
Richard Shaplin,Mathematics,Virginia Tech,4.0,4,75%,4.0
Robert Rogers,Mathematics,Virginia Tech,5.0,3,N/A,1.7
Martin Day,Mathematics,Virginia Tech,4.5,3,N/A,3.7
Serkan Gugercin,Mathematics,Virginia Tech,4.8,3,100%,3.4
Varun Scarlett,Mathematics,Virginia Tech,5.0,3,100%,3.0
Naim Dakhli,Mathematics,Virginia Tech,2.8,2,N/A,2.5
Jason Brunson,Mathematics,Virginia Tech,2.8,2,N/A,5.0
Corinne Mitchell,Mathematics,Virginia Tech,5.0,2,100%,2.0
Eyvindur Palsson,Mathematics,Virginia Tech,5.0,2,100%,3.5
Nicole Abaid,Mathematics,Virginia Tech,3.5,2,50%,3.0
Wendi Gao,Mathematics,Virginia Tech,1.0,2,0%,5.0
Wenbo Sun,Mathematics,Virginia Tech,5.0,2,100%,3.0
Jeff Evans,Mathematics,Virginia Tech,5.0,2,100%,2.5
Lida Bentz,Mathematics,Virginia Tech,4.0,1,100%,4.0
Rutuja Kshirsagar,Mathematics,Virginia Tech,2.0,1,0%,4.0
Fangchi Yan,Mathematics,Virginia Tech,5.0,1,100%,3.0
Mark Brandao,Mathematics,Virginia Tech,0.0,0,N/A,0.0
JD Brooks,Mathematics,Virginia Tech,0.0,0,N/A,0.0
Krishna Subedi,Mathematics,Virginia Tech,0.0,0,N/A,0.0
Yun Yang,Mathematics,Virginia Tech,0.0,0,N/A,0.0
Jennifer Smucker,Mathematics,Virginia Tech,0.0,0,N/A,0.0
Heath Hart,Mathematics,Virginia Tech,5.0,33,100%,3.0
Garrett Fowler,Mathematics,Virginia Tech,5.0,31,100%,3.2
Abbie Kohler,Mathematics,Virginia Tech,4.9,13,N/A,1.9
Marlow Lemons,Mathematics,Virginia Tech,3.6,13,50%,2.6
Graciela Cerezo Menegay,Mathematics,Virginia Tech,3.5,11,46%,3.9
Shuai Jiang,Mathematics,Virginia Tech,2.8,10,30%,4.5
Kelli Karcher,Mathematics,Virginia Tech,3.6,10,60%,3.4
Mark Shimozono,Mathematics,Virginia Tech,1.8,10,20%,4.9
Marlene Cothren,Mathematics,Virginia Tech,4.4,9,N/A,2.8
Mehdi Bouhafara,Mathematics,Virginia Tech,1.3,9,0%,4.5
Julianne Chung,Mathematics,Virginia Tech,4.0,3,67%,3.8
Vladislav Kokushkin,Mathematics,Virginia Tech,5.0,3,100%,2.4
Gazi Alam,Mathematics,Virginia Tech,4.4,3,67%,3.0
Hamidullah Farhat,Mathematics,Virginia Tech,2.0,2,0%,4.0
Anderson Norton,Mathematics,Virginia Tech,4.5,2,100%,4.0
Samuel Eastridge,Mathematics,Virginia Tech,5.0,2,100%,3.0
Isis Quinlan,Mathematics,Virginia Tech,4.5,2,100%,3.0
Stanca Ciupe,Mathematics,Virginia Tech,4.0,1,100%,3.0
Chi Nguyen,Mathematics,Virginia Tech,5.0,1,100%,3.0
Fazle Rabby,Mathematics,Virginia Tech,3.9,43,73%,4.4
Susan Anderson,Mathematics,Virginia Tech,4.1,31,80%,3.4
Sohei Yasuda,Mathematics,Virginia Tech,4.4,31,86%,3.8
Ted Juste,Mathematics,Virginia Tech,4.6,28,79%,3.3
Joseph Wells,Mathematics,Virginia Tech,4.7,26,93%,3.0
Sarah Barreto,Mathematics,Virginia Tech,4.0,20,55%,4.0
Numann Malik,Mathematics,Virginia Tech,3.0,19,53%,3.7
Nate Gildersleeve,Mathematics,Virginia Tech,3.3,17,40%,4.0
Susan Hagen,Mathematics,Virginia Tech,2.6,17,13%,3.4
Daniel Valvo,Mathematics,Virginia Tech,4.9,16,94%,3.3
Hussam Abobaker,Mathematics,Virginia Tech,2.3,15,40%,4.1
Peter Wapperom,Mathematics,Virginia Tech,2.6,13,37%,4.3
Jessica Thompson,Mathematics,Virginia Tech,3.4,13,54%,3.6
Eric Ufferman,Mathematics,Virginia Tech,4.6,10,100%,3.1
BenBen Zhu,Mathematics,Virginia Tech,2.8,9,34%,4.3
Kyle Flanagan,Mathematics,Virginia Tech,5.0,9,100%,2.6
Benjamin Goodberry,Mathematics,Virginia Tech,3.8,9,45%,4.1
Weidong Chen,Mathematics,Virginia Tech,1.6,8,13%,3.9
Lihong Zhao,Mathematics,Virginia Tech,1.0,7,0%,4.9
Megan Wawro,Mathematics,Virginia Tech,4.0,7
Robert West,Mechanical Engineering,Virginia Tech,2.4,3,34%,4.0
Jiangtao Cheng,Mechanical Engineering,Virginia Tech,1.0,1,100%,4.0
Emad Masroor,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
Shashank Priya,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
Saied Taheri,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
Scott Huxtable,Mechanical Engineering,Virginia Tech,4.0,4,75%,3.3
Zheng Li,Mechanical Engineering,Virginia Tech,4.4,3,67%,2.4
Christopher Williams,Mechanical Engineering,Virginia Tech,5.0,3,100%,3.3
Jan Helge Bohn,Mechanical Engineering,Virginia Tech,1.0,2,0%,4.5
Keyur Joshi,Mechanical Engineering,Virginia Tech,1.0,1,N/A,5.0
Tomonari Furukawa,Mechanical Engineering,Virginia Tech,1.0,1,N/A,4.0
Thomas Diller,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
Erik Komendera,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
Mark Paul,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
Al Wicks,Mechanical Engineering,Virginia Tech,1.6,5,20%,4.8
Bilel Aidi,Mechanical Engineering,Virginia Tech,3.1,5,40%,2.9
Chang Min Son,Mechanical Engineering,Virginia Tech,2.1,4,25%,4.3
Michael Ellis,Mechanical Engineering,Virginia Tech,4.4,3,100%,3.4
Donatus Ohanehi,Mechanical Engineering,Virginia Tech,2.3,3,67%,2.7
Danesh Tafti,Mechanical Engineering,Virginia Tech,1.0,1,0%,4.0
John Palmore Jr.,Mechanical Engineering,Virginia Tech,2.0,1,0%,5.0
Michael Bartlett,Mechanical Engineering,Virginia Tech,5.0,1,100%,2.0
Kaiyuan Peng,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
Jaisohn Kim,Mechanical Engineering,Virginia Tech,3.8,13,62%,4.1
Michael von Spakovsky,Mechanical Engineering,Virginia Tech,2.1,12,25%,4.9
Alexandrina Untaroiu,Mechanical Engineering,Virginia Tech,3.8,8,63%,3.8
Jan Bohn,Mechanical Engineering,Virginia Tech,1.4,5,0%,3.8
Pinar Acar,Mechanical Engineering,Virginia Tech,5.0,4,100%,3.8
John Barbish,Mechanical Engineering,Virginia Tech,4.9,4,100%,2.6
Shima Shahab,Mechanical Engineering,Virginia Tech,4.8,3,100%,2.4
Oumar Barry,Mechanical Engineering,Virginia Tech,1.0,3,0%,5.0
Kaveh Hamed,Mechanical Engineering,Virginia Tech,3.0,2,50%,3.0
Pablo Tarazaga,Mechanical Engineering,Virginia Tech,5.0,1,100%,3.0
Jeffrey Warfford,Mechanical Engineering,Virginia Tech,1.0,1,0%,3.0
Pavlos Vlachos,Mechanical Engineering,Virginia Tech,4.0,1,N/A,2.0
Lei Zuo,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
Ry Long,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
Clinton Dancey,Mechanical Engineering,Virginia Tech,0.0,0,N/A,0.0
John Aggrey,Medicine,Virginia Tech,5.0,1,100%,3
Gary Simonds,Medicine,Virginia Tech,5.0,1,100%,3
Wallace Easter,Music,Virginia Tech,3.0,3,67%,2
Kimberly Loeffert,Music,Virginia Tech,3.0,3,34%,2.4
Richard Masters,Music,Virginia Tech,5.0,2,100%,4
John Irrera,Music,Virginia Tech,5.0,1,100%,3
Dave McKee,Music,Virginia Tech,5.0,6,N/A,1.7
Charles Nichols,Music,Virginia Tech,4.0,4,75%,3
Juan Berrios,Music,Virginia Tech,4.5,2,100%,1
Juan Rodriguez,Music,Virginia Tech,4.3,3,100%,2
Annie Stevens,Music,Virginia Tech,5.0,1,N/A,4
Dwight Bigler,Music,Virginia Tech,4.5,1,N/A,2
Eric Lyon,Music,Virginia Tech,0.0,0,N/A,0
Amy Gillick,Music,Virginia Tech,0.0,0,N/A,0
Jay Crone,Music,Virginia Tech,1.8,15,20%,3.6
John Howell,Music,Virginia Tech,3.2,9,N/A,2.6
Jana Paglialonga,Music,Virginia Tech,5.0,1,100%,1
Arianna Wyatt,Music,Virginia Tech,1.0,1,0%,4
Ivica Bukvic,Music,Virginia Tech,4.0,1,N/A,3
Alan Weinstein,Music,Virginia Tech,0.0,0,N/A,0
Jeffery Hutchins,Music,Virginia Tech,0.0,0,N/A,0
R Cole,Music,Virginia Tech,3.1,14,N/A,2.4
Chad Reep,Music,Virginia Tech,5.0,8,100%,2
Edward Knoeckel,Music,Virginia Tech,3.9,4,75%,2.5
Lee Heuermann,Music,Virginia Tech,4.5,2,N/A,2.5
John Husser,Music,Virginia Tech,4.0,1,100%,1
Cyrus Pace,Music,Virginia Tech,5.0,1,100%,1
Bryan Thorsett,Music,Virginia Tech,0.0,0,N/A,0
Walter Ott,Philosophy,Virginia Tech,3.7,8,50%,3.6
Karen Kovaka,Philosophy,Virginia Tech,4.0,4,50%,3.3
Katy Shepard,Philosophy,Virginia Tech,2.0,4,25%,3.3
Grace McGee,Philosophy,Virginia Tech,1.5,3,0%,3.3
Mark Bauer,Philosophy,Virginia Tech,3.0,2,N/A,2.5
Douglas Lind,Philosophy,Virginia Tech,5.0,1,100%,2
Jonathon Dixon,Philosophy,Virginia Tech,4.5,1,N/A,2
J C Lau,Philosophy,Virginia Tech,1.0,1,N/A,4
Darren Jackson,Philosophy,Virginia Tech,0.0,0,N/A,0
Joe Pitt,Philosophy,Virginia Tech,4.1,17,100%,2.9
William Jamerson,Philosophy,Virginia Tech,4.3,14,72%,3
Lydia Patton,Philosophy,Virginia Tech,5.0,7,100%,2.1
Justin Horn,Philosophy,Virginia Tech,5.0,6,100%,2.8
Hannah Wildman Short,Philosophy,Virginia Tech,5.0,6,100%,2.6
Marc Lucht,Philosophy,Virginia Tech,4.6,4,N/A,3.8
Christopher Haufe,Philosophy,Virginia Tech,2.5,4,N/A,4
Anthony Harrison,Philosophy,Virginia Tech,4.0,2,100%,1.5
Benjamin Jantzen,Philosophy,Virginia Tech,5.0,2,100%,2
Ivan Guajardo,Philosophy,Virginia Tech,4.0,2,100%,3
Charlie De Souza,Philosophy,Virginia Tech,5.0,1,100%,1
Rohan Sud,Philosophy,Virginia Tech,5.0,1,100%,3
Greg Novack,Philosophy,Virginia Tech,4.0,18,78%,4.1
James Klagge,Philosophy,Virginia Tech,3.0,15,50%,3
Jordan MacKenzie,Philosophy,Virginia Tech,5.0,12,100%,2.3
Timothy Fuller,Philosophy,Virginia Tech,4.6,6,100%,2.8
Jay Burkette,Philosophy,Virginia Tech,4.1,6,67%,3
Sukaina Hirji,Philosophy,Virginia Tech,4.8,4,100%,2.5
Michael Moehler,Philosophy,Virginia Tech,4.2,4,100%,2.5
Ted Parent,Philosophy,Virginia Tech,2.3,3,34%,3.3
Kevin Coffey,Philosophy,Virginia Tech,4.5,2,100%,3.5
Melinda Miller,Philosophy,Virginia Tech,0.0,0,N/A,0
Eric Lewis,Philosophy,Virginia Tech,4.3,14,77%,2.8
Kevin Klipfel,Philosophy,Virginia Tech,4.4,4,N/A,3
Tristram McPherson,Philosophy,Virginia Tech,4.8,2,N/A,2.5
Mary Ryan,Philosophy,Virginia Tech,4.5,2,100%,2
Rachel Keith,Philosophy,Virginia Tech,4.5,2,100%,1.5
Caitlin Parker,Philosophy,Virginia Tech,3.5,1,N/A,4
Daniel Wodak,Philosophy,Virginia Tech,4.0,1,100%,3
Fabian Wendt,Philosophy,Virginia Tech,2.0,1,0%,4
Daniel Hoek,Philosophy,Virginia Tech,5.0,1,100%,1
Samantha Hirshland,Philosophy,Virginia Tech,0.0,0,N/A,0
Claudio D'Amato,Philosophy,Virginia Tech,5.0,26,93%,3.1
Stephen Daskal,Philosophy,Virginia Tech,4.3,6,N/A,2.3
Kelly Trogdon,Philosophy,Virginia Tech,3.9,6,67%,2.9
Daniel Parker,Philosophy,Virginia Tech,1.3,5,N/A,5
Gil Hersch,Philosophy,Virginia Tech,4.0,1,100%,3
Jason Bowers,Philosophy,Virginia Tech,4.0,1,100%,2
David Kraemer,Philosophy,Virginia Tech,0.0,0,N/A,0
Fei Lin,Physics,Virginia Tech,3.5,28,65%,3.5
Brandon Bear,Physics,Virginia Tech,4.2,18,67%,2.7
John Simonetti,Physics,Virginia Tech,5.0,8,100%,2.9
Eugene Halpin,Physics,Virginia Tech,4.0,7,100%,2.7
T. Roger Chang,Physics,Virginia Tech,5.0,4,100%,2.3
James Gray,Physics,Virginia Tech,5.0,3,100%,3
Giti Khodaparast,Physics,Virginia Tech,3.2,3,N/A,3.3
Randy Heflin,Physics,Virginia Tech,5.0,2,N/A,2
Michel Pleimling,Physics,Virginia Tech,4.0,1,N/A,4
Uwe Tauber,Physics,Virginia Tech,4.0,1,0%,4
Daniel Osborne,Physics,Virginia Tech,3.4,44,60%,3.4
Almas Khan,Physics,Virginia Tech,4.5,42,94%,3
Rana Ashkar,Physics,Virginia Tech,2.6,19,37%,4
Duncan Farrah,Physics,Virginia Tech,4.6,7,100%,1.9
Camillo Mariani,Physics,Virginia Tech,5.0,2,100%,3.5
Jeong-Ah Lee,Physics,Virginia Tech,2.2,13,31%,4.3
Satoru Emori,Physics,Virginia Tech,5.0,9,100%,2.6
Christopher J. Ashall,Physics,Virginia Tech,5.0,5,100%,1
Kriton Papavasiliou,Physics,Virginia Tech,2.9,41,14%,5
Nahum Arav,Physics,Virginia Tech,3.6,24,34%,2.5
Travis Merritt,Physics,Virginia Tech,3.9,24,64%,3.4
Alma Robinson,Physics,Virginia Tech,5.0,22,100%,3
Leo Piilonen,Physics,Virginia Tech,3.9,11,50%,3.4
Matthew Joyce,Physics,Virginia Tech,4.2,5,N/A,2.8
Mark Pitt,Physics,Virginia Tech,4.4,4,N/A,3
Rick Sanchez,Physics,Virginia Tech,4.3,2,100%,5
Danielle Lucero,Physics,Virginia Tech,3.0,1,100%,3
Vinh Nguyen,Physics,Virginia Tech,2.0,1,0%,3
Thomas O'Donnell,Physics,Virginia Tech,5.0,16,100%,3
Bruce Vogelaar,Physics,Virginia Tech,3.0,14,34%,3.5
Naraine Persaud,Physics,Virginia Tech,2.4,6,N/A,3.5
Lay Chang,Physics,Virginia Tech,1.8,6,17%,3.5
Victoria Soghomonian,Physics,Virginia Tech,3.5,2,100%,3
Chris Ashall,Physics,Virginia Tech,0.0,0,N/A,0
Andrew Turner,Physics,Virginia Tech,0.0,0,N/A,0
Mauro Caraccioli,Political Science,Virginia Tech,4.0,11,73%,2.6
Wayne Moore,Political Science,Virginia Tech,3.4,9,80%,4.6
Daniel Gibbs,Political Science,Virginia Tech,2.1,9,23%,4.3
Georgeta Pourchot,Political Science,Virginia Tech,2.8,7,50%,4.4
Charles Taylor,Political Science,Virginia Tech,3.9,5,N/A,4.2
June Jones,Political Science,Virginia Tech,3.9,4,50%,2.9
Clara Suong,Political Science,Virginia Tech,4.9,4,100%,2.5
Sabrina Harris,Political Science,Virginia Tech,5.0,3,100%,4
Sarah Surak,Political Science,Virginia Tech,4.8,3,N/A,2
Keith Hollinger,Political Science,Virginia Tech,1.0,1,N/A,5
Jennifer Lawrence,Political Science,Virginia Tech,5.0,1,100%,3
Alex Segura Betancourt,Political Science,Virginia Tech,0.0,0,N/A,0
Bikrum Gill,Political Science,Virginia Tech,0.0,0,N/A,0
Courtney Thomas,Political Science,Virginia Tech,3.4,73,67%,2.8
Richard Shingles,Political Science,Virginia Tech,2.6,8,N/A,3.6
Anthony Szczurek,Political Science,Virginia Tech,4.6,8,88%,3.1
Shaun Respess,Political Science,Virginia Tech,5.0,5,100%,3.3
Linea Cutter,Political Science,Virginia Tech,4.5,4,100%,3
Joe Eifert,Political Science,Virginia Tech,3.0,2,100%,2
Parakh Hoon,Political Science,Virginia Tech,3.8,2,N/A,2.5
Stephanie Davis,Political Science,Virginia Tech,5.0,2,100%,2
Christopher Lawrence,Political Science,Virginia Tech,1.5,1,N/A,4
Ryan Briggs,Political Science,Virginia Tech,4.5,1,N/A,3
Madison Tepper,Political Science,Virginia Tech,5.0,1,100%,3
Audrey Reeves,Political Science,Virginia Tech,0.0,0,N/A,0
Gerard Toal,Political Science,Virginia Tech,0.0,0,N/A,0
Chaz Briscoe,Political Science,Virginia Tech,0.0,0,N/A,0
Edward Weisband,Political Science,Virginia Tech,4.1,52,36%,4
Caitlin Jewitt,Political Science,Virginia Tech,3.1,19,50%,3.8
Charles Walcott,Political Science,Virginia Tech,4.4,18,N/A,2.6
Chad Hankinson,Political Science,Virginia Tech,4.4,13,77%,2.8
Bettina Koch,Political Science,Virginia Tech,2.0,8,25%,3.6
Caroline Alphin,Political Science,Virginia Tech,3.4,8,63%,2
Brandy Faulkner,Political Science,Virginia Tech,4.3,7,34%,3.4
CI Thomas,Political Science,Virginia Tech,4.8,8,86%,2.9
Judson Abraham,Political Science,Virginia Tech,2.0,5,40%,4.4
Jeremy W. Hunsinger,Political Science,Virginia Tech,3.5,4,N/A,3.3
Luke Plotica,Political Science,Virginia Tech,4.7,4,100%,2.2
Lillian Frost,Political Science,Virginia Tech,3.0,4,75%,3.3
Samuel Beckenhauer,Political Science,Virginia Tech,2.0,3,34%,4.4
Robin Taylor,Political Science,Virginia Tech,1.9,3,0%,4
Alana Romanella,Political Science,Virginia Tech,4.7,3,N/A,1.3
KAREN KOVAKA,Political Science,Virginia Tech,3.0,3,34%,3.3
Jordan Fallon,Political Science,Virginia Tech,5.0,2,100%,2
Kent Morris,Political Science,Virginia Tech,4.8,2,N/A,3.5
Dennis Medina,Political Science,Virginia Tech,4.5,1,N/A,2
Eric Malczewski,Political Science,Virginia Tech,0.0,0,N/A,0
Chad Levinson,Political Science,Virginia Tech,0.0,0,N/A,0
Beatriz Barros,Political Science,Virginia Tech,0.0,0,N/A,0
Deborah Milly,Political Science,Virginia Tech,2.6,14,34%,3.4
Craig Brians,Political Science,Virginia Tech,4.5,13,N/A,3.3
Binio Binev,Political Science,Virginia Tech,4.1,10,70%,4
Jong RA,Political Science,Virginia Tech,3.1,10,100%,3.5
Dimitris Tsarouhas,Political Science,Virginia Tech,4.6,7,100%,3.1
Ilja Luciak,Political Science,Virginia Tech,3.5,6,50%,2.5
Christine Luketic,Political Science,Virginia Tech,2.5,2,50%,2
Hannah Gignoux,Political Science,Virginia Tech,5.0,2,100%,2.5
Lawerence Kapp,Political Science,Virginia Tech,4.5,1,N/A,3
Arnold Dupuy,Political Science,Virginia Tech,4.0,1,100%,3
Karen Hult,Political Science,Virginia Tech,0.0,0,N/A,0
Wu Chengqiu,Political Science,Virginia Tech,0.0,0,N/A,0
Courtney Powell,Political Science,Virginia Tech,4.0,5,N/A,4
Luther McPherson,Political Science,Virginia Tech,5.0,4,100%,3.5
Zachariah Wheeler,Political Science,Virginia Tech,5.0,4,100%,2.9
Aaron Brantly,Political Science,Virginia Tech,5.0,3,100%,2.4
Jariah Strozier,Political Science,Virginia Tech,5.0,2,100%,3
Karin Kitchens,Political Science,Virginia Tech,5.0,2,100%,2.5
Robert Hodges,Political Science,Virginia Tech,5.0,1,100%,2
Kurt Hoffman,Psychology,Virginia Tech,4.8,60,98%,2.2
Bruce Friedman,Psychology,Virginia Tech,3.0,10,67%,4.3
Vanessa Diaz,Psychology,Virginia Tech,5.0,8,100%,2.6
Neil Hauenstein,Psychology,Virginia Tech,3.9,5,100%,3.3
Amanda Watson,Psychology,Virginia Tech,5.0,5,N/A,1.2
Katherine Adams,Psychology,Virginia Tech,4.6,4,100%,1.4
Tae-Ho Lee,Psychology,Virginia Tech,4.3,4,75%,1.8
Heather Kissel,Psychology,Virginia Tech,5.0,3,100%,2
Anthony Cate,Psychology,Virginia Tech,5.0,2,100%,2
Bryan Acton,Psychology,Virginia Tech,4.5,2,100%,3
Nathaniel Van Kirk,Psychology,Virginia Tech,4.8,2,N/A,1
Akiho Tanaka,Psychology,Virginia Tech,4.3,2,N/A,2.5
John Marshal,Psychology,Virginia Tech,4.5,2,100%,1
Ning Hsu,Psychology,Virginia Tech,1.5,2,0%,3.5
Michael Knepp,Psychology,Virginia Tech,4.0,1,N/A,1
Jennifer Bertollo,Psychology,Virginia Tech,5.0,1,100%,2
Manasia Sturdivant,Psychology,Virginia Tech,5.0,1,100%,1
Jennifer Phillips,Psychology,Virginia Tech,5.0,1,100%,4
Meagan Brem,Psychology,Virginia Tech,5.0,1,100%,2
Annah Cash,Psychology,Virginia Tech,5.0,1,100%,2
Robert Harvey,Psychology,Virginia Tech,0.0,0,N/A,0
Heather Littleton,Psychology,Virginia Tech,0.0,0,N/A,0
Nicole Kreiser,Psychology,Virginia Tech,0.0,0,N/A,0
Rosanna Breaux,Psychology,Virginia Tech,0.0,0,N/A,0
Brad Kelley,Psychology,Virginia Tech,3.3,2,N/A,1
Tanya Mitropoulos,Psychology,Virginia Tech,4.5,2,100%,3
KL Burns,Psychology,Virginia Tech,2.5,1,N/A,5
Jonathan Waldron,Psychology,Virginia Tech,5.0,1,N/A,2
Jess Versele,Psychology,Virginia Tech,4.5,1,N/A,2
Louis Hickman,Psychology,Virginia Tech,2.0,1,0%,3
Kirby Deater-Deckard,Psychology,Virginia Tech,0.0,0,N/A,0
Patti Harrison,Psychology,Virginia Tech,0.0,0,N/A,0
Matthew Cox,Psychology,Virginia Tech,2.5,1,N/A,3
Andrew Powers,Psychology,Virginia Tech,5.0,1,N/A,3
Erin Kerfoot,Psychology,Virginia Tech,4.0,1,100%,1
Clinton Comer,Psychology,Virginia Tech,1.5,1,N/A,2
Alisa Huskey,Psychology,Virginia Tech,0.0,0,N/A,0
Courtney Swanson,Psychology,Virginia Tech,0.0,0,N/A,0
Emily Rost,Psychology,Virginia Tech,0.0,0,N/A,0
Samantha Garrett,Psychology,Virginia Tech,0.0,0,N/A,0
Mohamed Zerrouk,Psychology,Virginia Tech,4.8,7,100%,1.9
Kwame Harrison,Psychology,Virginia Tech,4.8,6,100%,2
Benjamin DeVore,Psychology,Virginia Tech,4.8,5,100%,3.2
Diana Riser,Psychology,Virginia Tech,5.0,4,N/A,3
Brandon Minton,Psychology,Virginia Tech,5.0,3,100%,2
Gregory Longo,Psychology,Virginia Tech,3.8,3,N/A,3
Patrick Coyle,Psychology,Virginia Tech,4.3,3,N/A,3.3
Rachel Diana,Psychology,Virginia Tech,4.0,2,50%,4
Doug Harrison,Psychology,Virginia Tech,0.0,0,N/A,0
Scott Geller,Psychology,Virginia Tech,3.2,97,36%,3
Anjolii Diaz,Psychology,Virginia Tech,4.5,6,N/A,1.8
Eileen Anderson,Psychology,Virginia Tech,4.4,4,N/A,2.3
Vinaya Raj,Psychology,Virginia Tech,4.9,4,N/A,1.8
Kasey Stanton,Psychology,Virginia Tech,5.0,2,100%,2
Kristin Peviani,Psychology,Virginia Tech,5.0,1,100%,2
Brittany Nackley,Psychology,Virginia Tech,5.0,1,100%,3
Derek Spangler,Psychology,Virginia Tech,3.5,1,N/A,3
Jack Wardale,Psychology,Virginia Tech,5.0,1,100%,2
Robert Stephens,Psychology,Virginia Tech,0.0,0,N/A,0
Adrienne Means-Christensen,Psychology,Virginia Tech,0.0,0,N/A,0
David Harrison,Psychology,Virginia Tech,4.3,36,82%,2.8
Russell Jones,Psychology,Virginia Tech,4.4,18,84%,3
Robert J. Harvey,Psychology,Virginia Tech,3.2,12,0%,1.7
Martha Bell,Psychology,Virginia Tech,3.5,10,0%,3.1
Connor Sullivan,Psychology,Virginia Tech,3.0,2,50%,2
Mark David Scott,Psychology,Virginia Tech,5.0,2,N/A,1
Bradley White,Psychology,Virginia Tech,5.0,2,N/A,2
Sehmuz Akalin,Psychology,Virginia Tech,5.0,2,100%,4
Adam Raines,Psychology,Virginia Tech,5.0,2,100%,3
Lily Seah,Psychology,Virginia Tech,2.0,2,0%,3.5
Lance Bush,Psychology,Virginia Tech,4.0,1,100%,2
Zhange Ni,Religion,Virginia Tech,4.0,3,67%,2.6
Kevin Hamed,Resource Management,Virginia Tech,5.0,11,100%,3
John Seiler,Resource Management,Virginia Tech,4.6,5,100%,3.4
Ronald Gibbs,Resource Management,Virginia Tech,4.0,1,N/A,3
Daniel Marcucci,Resource Management,Virginia Tech,5.0,1,100%,2
Nicholas Caruso,Resource Management,Virginia Tech,0.0,0,N/A,0
Kathleen Parrott,Resource Management,Virginia Tech,4.4,4,100%,3.2
Patricia Fisher,Resource Management,Virginia Tech,0.0,0,N/A,0
Gulzat Matekova,Russian,Virginia Tech,0.0,0,N/A,0
Kirsten Rutsala,Russian,Virginia Tech,4.9,5,80%,4
Nyusya Milman-Miller,Russian,Virginia Tech,2.3,2,N/A,4.5
Yuliya Minkova,Russian,Virginia Tech,3.7,3,100%,3.7
Temperance Rowell,Science,Virginia Tech,2.3,28,25%,2.8
Cora Olson,Science,Virginia Tech,5.0,3,100%,2.4
Bill Eigel,Science,Virginia Tech,5.0,2,N/A,3.5
Vivek Shastry,Science,Virginia Tech,4.0,1,0%,1
Pearl Chiu,Science,Virginia Tech,0.0,0,N/A,0
Young Kim,Science,Virginia Tech,0.0,0,N/A,0
Matthew Goodrum,Science,Virginia Tech,4.9,13,100%,2.9
D Sarah Stamps,Science,Virginia Tech,4.8,8,100%,1.9
Saul Halfon,Science,Virginia Tech,2.9,5,100%,4
Jennifer Rainville,Science,Virginia Tech,5.0,4,100%,3
Seohyun Park,Science,Virginia Tech,3.3,4,75%,2.1
Mike Bowers,Science,Virginia Tech,3.0,2,50%,4
Chris Thompson,Science,Virginia Tech,3.0,2,0%,4
Matthew Buczynski,Science,Virginia Tech,5.0,2,100%,3
Brian Badgley,Science,Virginia Tech,5.0,1,100%,3
Rebekah Miller,Science,Virginia Tech,5.0,1,100%,1
Melanie Sontheimer,Science,Virginia Tech,0.0,0,N/A,0
Brian Wiersema,Science,Virginia Tech,0.0,0,N/A,0
Brian Romans,Science,Virginia Tech,0.0,0,N/A,0
Neil Johnson,Science,Virginia Tech,2.0,7,29%,4.1
Alicia Pickrell,Science,Virginia Tech,1.0,2,0%,4
John Chermak,Science,Virginia Tech,2.0,1,100%,2
Matthew Wisnioski,Science,Virginia Tech,3.0,1,N/A,3
Stephen Smith,Science,Virginia Tech,0.0,0,N/A,0
Kathy Ara,Science,Virginia Tech,1.0,4,0%,3.9
Joel McGlothlin,Science,Virginia Tech,1.5,3,0%,4.8
Laszlo Horvath,Science,Virginia Tech,0.0,0,N/A,0
Amy Smith,Science,Virginia Tech,0.0,0,N/A,0
Georgia Hodes,Science,Virginia Tech,0.0,0,N/A,0
Sarah Clinton,Science,Virginia Tech,5.0,4,100%,1.3
Scott King,Science,Virginia Tech,3.6,5,80%,2
Ying Zhou,Science,Virginia Tech,3.5,2,50%,3
Dylan McDaniel,Science,Virginia Tech,1.5,2,0%,4
Steven Rideout,Science,Virginia Tech,5.0,1,100%,2
Rachel Byer,Science,Virginia Tech,0.0,0,N/A,0
Philip Prince,Science,Virginia Tech,0.0,0,N/A,0
Jennifer Zambriski,Science,Virginia Tech,0.0,0,N/A,0
Jeremy Carter,Religion,Virginia Tech,3.5,2,N/A,3
Samuel Kessler,Religion,Virginia Tech,5.0,1,100%,4
Aaron Ansell,Religion,Virginia Tech,0.0,0,N/A,0
James Jewitt,Religion,Virginia Tech,3.4,5,60%,2.8
Rachel Scott,Religion,Virginia Tech,3.8,3,100%,3.4
David Skelton,Religion,Virginia Tech,1.3,3,0%,1
Najm Yousefi,Religion,Virginia Tech,5.0,2,N/A,4
Ananda Abeysekara,Religion,Virginia Tech,3.1,10,50%,3.3
Elizabeth Malbon,Religion,Virginia Tech,2.7,5,N/A,3.4
David Litwa,Religion,Virginia Tech,2.8,4,50%,2.5
BM Britt,Religion,Virginia Tech,3.1,3,100%,3
Bestami Bilgic,Religion,Virginia Tech,5.0,2,100%,1.5
Emma Rifai,Religion,Virginia Tech,5.0,1,100%,2
Mohammed Pervaiz,Religion,Virginia Tech,0.0,0,N/A,0
Jack Bernardi,Religion,Virginia Tech,2.0,3,34%,2
Shaily Patel,Religion,Virginia Tech,3.5,2,50%,3
Peter Schmitthenner,Religion,Virginia Tech,5.0,1,100%,2
Raji Soni,Religion,Virginia Tech,4.3,3,100%,3
Benjamin Sax,Religion,Virginia Tech,4.5,2,N/A,1
Holly Jordan,Religion,Virginia Tech,0.0,0,N/A,0
Kevin Hamed,Resource Management,Virginia Tech,5.0,11,100%,3
Oscar Solis,Social Science,Virginia Tech,5.0,4,100%,2.8
Yanka Kirilova Petkova,Social Science,Virginia Tech,2.0,1,N/A,3
Austin Council,Social Science,Virginia Tech,3.0,1,0%,4
Ashley Dayer,Social Science,Virginia Tech,0.0,0,N/A,0
Savannah Mandel,Social Science,Virginia Tech,3.3,11,55%,2.8
Austin Council,Social Science,Virginia Tech,4.6,5,80%,3
Isabel Bradburn,Social Science,Virginia Tech,2.0,1,0%,4
Fabian Prieto-Nanez,Social Science,Virginia Tech,5.0,1,100%,1
Christine Labuski,Social Science,Virginia Tech,0.0,0,N/A,0
Jordan Laney,Social Science,Virginia Tech,3.0,4,34%,3
John Seiler,Resource Management,Virginia Tech,4.6,5,100%,3.4
Ronald Gibbs,Resource Management,Virginia Tech,4.0,1,N/A,3
Daniel Marcucci,Resource Management,Virginia Tech,5.0,1,100%,2
Nicholas Caruso,Resource Management,Virginia Tech,0.0,0,N/A,0
Kathleen Parrott,Resource Management,Virginia Tech,4.4,4,100%,3.2
Patricia Fisher,Resource Management,Virginia Tech,0.0,0,N/A,0
Justin Loda,Statistics,Virginia Tech,4.9,20,90%,3
Thomas Staley,Technology,Virginia Tech,3.0,2,100%,5
Zeb Bowden,Technology,Virginia Tech,4.6,15,87%,3.3
Lee Vinsel,Technology,Virginia Tech,5.0,3,100%,3
Leonard Smith,Technology,Virginia Tech,0.0,0,N/A,0
Carmen Tavera,Statistics,Virginia Tech,3.9,15,74%,2.5
George Terrell,Statistics,Virginia Tech,1.9,14,10%,4.9
Rachel Keller,Statistics,Virginia Tech,1.6,5,0%,4.6
Austin Rhodes,Statistics,Virginia Tech,2.5,1,N/A,4
Dave Higdon,Statistics,Virginia Tech,5.0,1,100%,3
Sierra Merkes,Statistics,Virginia Tech,0.0,0,N/A,0
Zhiyang Zhang,Statistics,Virginia Tech,3.3,16,50%,2.8
Christian Lucero,Statistics,Virginia Tech,3.5,12,59%,4.1
Gordon Vining,Statistics,Virginia Tech,0.0,0,N/A,0
Boya Zhang,Statistics,Virginia Tech,0.0,0,N/A,0
Andrew Cooper,Statistics,Virginia Tech,0.0,0,N/A,0
David Edwards,Statistics,Virginia Tech,0.0,0,N/A,0
Hamdy Mahmoud,Statistics,Virginia Tech,4.8,25,100%,2.3
Christopher Franck,Statistics,Virginia Tech,4.8,4,100%,2.8
Leah Johnson,Statistics,Virginia Tech,3.8,3,67%,3.4
Wenyu Gao,Statistics,Virginia Tech,2.5,2,0%,2.5
Tom Ewing,Statistics,Virginia Tech,0.0,0,N/A,0
John Russell,Statistics,Virginia Tech,2.5,34,24%,3.6
Anne Driscoll,Statistics,Virginia Tech,5.0,2,100%,2
Jie Min,Statistics,Virginia Tech,1.0,1,0%,4
Meimei Liu,Statistics,Virginia Tech,2.0,2,50%,2.5
Han Chen,Statistics,Virginia Tech,1.0,1,0%,5
Marco Ferreira,Statistics,Virginia Tech,0.0,0,N/A,0
Susanna Rhineheart,Theater,Virginia Tech,4.4,25,100%,1.6
Susanna Rinehart,Theater,Virginia Tech,5.0,24,100%,1.9
Susanna Reinhart,Theater,Virginia Tech,4.8,4,100%,2.3
Jennifer Goff,Theater,Virginia Tech,3.7,3,67%,2.3
Rebekah Hall,Theater,Virginia Tech,2.0,1,0%,3
Amanda Nelson,Theater,Virginia Tech,5.0,1,N/A,1
Taylor Wood,Theater,Virginia Tech,0.0,0,N/A,0
Tatiana Vintu,Theater,Virginia Tech,0.0,0,N/A,0
Natasha Staley,Theater,Virginia Tech,0.0,0,N/A,0
Cara Rawlings,Theater,Virginia Tech,3.0,9,40%,3.6
Allen Sanders,Theater,Virginia Tech,4.5,2,100%,1.5
Michael Alvarez,Theater,Virginia Tech,2.0,1,0%,5
David Gammons,Theater,Virginia Tech,4.0,1,100%,3
Melody Zobel,Theater,Virginia Tech,0.0,0,N/A,0
Gregory Justice,Theater,Virginia Tech,5.0,3,100%,2
Sarah Yorke,Theater,Virginia Tech,5.0,1,100%,1
Thomas Murray,Theater,Virginia Tech,0.0,0,N/A,0
Kenly Fenio,Theater,Virginia Tech,2.8,4,N/A,3.3
Brittney Harris,Theater,Virginia Tech,5.0,1,100%,1
Daniel Tobin,Theater,Virginia Tech,0.0,0,N/A,0
Paroma Wagle,Urban Planning,Virginia Tech,2.5,2,50%,1.5
John Randolph,Urban Planning,Virginia Tech,1.0,1,N/A,5
Wenwen Zhang,Urban Planning,Virginia Tech,0.0,0,N/A,0
Diane Zahm,Urban Planning,Virginia Tech,2.5,28,0%,3.6
David Bieri,Urban Planning,Virginia Tech,3.9,6,67%,2.6
Shalini Misra,Urban Planning,Virginia Tech,1.0,1,0%,4
JS Clements,Urban Planning,Virginia Tech,0.0,0,N/A,0
Theodore Lim,Urban Planning,Virginia Tech,5.0,3,100%,2.4
Ted Koebel,Urban Planning,Virginia Tech,4.8,2,N/A,3.5
Amy Ashworth,Urban Planning,Virginia Tech,0.0,0,N/A,0
Joseph Scarpaci,Urban Planning,Virginia Tech,0.0,0,N/A,0
Damian Pitt,Urban Planning,Virginia Tech,4.5,1,N/A,2
Doris Kincade,Visual Arts,Virginia Tech,2.9,6,50%,3.8
M Kim,Women's Studies,Virginia Tech,2.3,3,N/A,4.3
Catalina Hernandez-Cabal,Women's Studies,Virginia Tech,3.4,3,34%,2
Barbara Smith,Women's Studies,Virginia Tech,4.3,2,N/A,3
Casey Brinmer,Women's Studies,Virginia Tech,4.5,2,100%,2
Zarah Quinn,Women's Studies,Virginia Tech,5.0,2,100%,1.5
Suchitra Samanta,Women's Studies,Virginia Tech,4.8,13,100%,2.1
Jennifer Bondy,Women's Studies,Virginia Tech,4.4,4,100%,1.3
Laura Gillman,Women's Studies,Virginia Tech,4.0,1,N/A,3
Leslie Pendleton,Women's Studies,Virginia Tech,1.0,1,N/A,5
Sharon Elber,Women's Studies,Virginia Tech,5.0,1,100%,2
Silas Cassinelli,Women's Studies,Virginia Tech,5.0,2,100%,2.5
Katherine Ayers,Women's Studies,Virginia Tech,5.0,1,N/A,1
Bonnie Zare,Women's Studies,Virginia Tech,0.0,0,N/A,0
Lyla Byers,Women's Studies,Virginia Tech,4.8,3,67%,3
Catalina Cabal,Women's Studies,Virginia Tech,2.8,3,0%,2.4
Jennifer Turner,Women's Studies,Virginia Tech,3.5,2,100%,3
Leslie Toney,Women's Studies,Virginia Tech,5.0,2,100%,3.5
Claire Traveline,Women's Studies,Virginia Tech,4.0,1,N/A,2
Amelia Salisbury,Visual Arts,Virginia Tech,4.3,4,75%,2.3
Nate King,Visual Arts,Virginia Tech,4.0,3,100%,3.9
Joshua Okoro,Visual Arts,Virginia Tech,0.0,0,N/A,0
Michael Borowski,Visual Arts,Virginia Tech,0.0,0,N/A,0
Trevor Finney,Visual Arts,Virginia Tech,5.0,1,100%,3
Robin Scully,Visual Arts,Virginia Tech,0.0,0,N/A,0
Hiromi Okamura,Visual Arts,Virginia Tech,4.6,6,84%,2.4
Wallace Santos Lages,Visual Arts,Virginia Tech,2.3,3,34%,3.3
Travis Head,Visual Arts,Virginia Tech,5.0,2,100%,2.5
Dustin Dennis,Visual Arts,Virginia Tech,5.0,2,100%,2.5
Renee Spaar,Visual Arts,Virginia Tech,1.6,5,0%,4.4
Mitchell Miller,Visual Arts,Virginia Tech,5.0,4,100%,3.6
Timothy Lockridge,Writing,Virginia Tech,4.9,4,N/A,2.3
Christopher Vaughan,Writing,Virginia Tech,0.0,0,N/A,0
Kira Morse,Writing,Virginia Tech,4.3,8,88%,2.8
Anne-Lise Velez,Writing,Virginia Tech,1.0,1,0%,3
Monique Dufour,Writing,Virginia Tech,4.2,4,50%,3
 

"""

# Specify the file path
file_path = 'professor_ratings.csv'

# Write data to CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    file.write(data)

print(f"Data has been written to {file_path}")
