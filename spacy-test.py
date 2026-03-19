import spacy as spc # type: ignore
# nlp = spc.load("fr_core_news_lg")
# nlp_sm = spc.load("fr_core_news_sm")
nlp = spc.load("C:\\Users\\13065\\Documents\\GitHub\\queering-geographies\\spacy-training\\output\\model-last") #Use this for our TRAINED MODEL

doc = [
    "L’an passé, Paprika, la firme de design graphique et straté- gique qui a concocté les décors de rue d’Aires Libres en 2009 et 2010 – les cordes à linge de 2009 aux couleurs vert et jaune – avait gagné un prix spécial du jury (Coup de cœur) Graphika pour ses installations ori- ginales. Ces mêmes «cordes à linge» se retrouvent mainte- nant dans le nouveau livre sur l’histoire de la rue Sainte-Cathe- rine publié par le Musée de Pointe-à- Callière (Les éditions de l’Homme) dans le cadre de l’exposition sur la rue Sainte- Catherine qui s’y tient jusqu’au 24 avril. En 2011, Paprika rem- porte un autre prix dans la catégorie De- sign événementiel, pour les roses rouges stylisées suspendues et le graphisme des affiches de l’édition 2010 d’Aires Libres. Des honneurs qui s’accumulent ainsi pour Paprika, pour Aires Libres et la Société de développement commercial (SDC) du Village qui chapeaute l’événement de piétonnisation de la rue Sainte-Catherine Est du- rant la période estivale, avec le soutien toujours très apprécié de l’arrondissement Ville-Marie.  À la demande de la SDC, Paprika a conçu de nouvelles oriflammes servant à mieux identifier le quartier gai de Montréal. On reprendra ainsi, de façon ingénieuse, les couleurs du drapeau arc- en-ciel sur une distance de plus d’un kilomètre.    ",
    
    "Le Drugstore, 1366, rue Sainte-Catherine Est, Montréal.",
    
    "FAGGITY ASS FRIDAYS  @ THE PLAYHOUSE  5656, AVENUE DU PARC  FAGGITYASSFRIDAY.BLOGSPOT.COM/ Soirées queer dansantes et de per- formances organisées au The Play- house, sur Avenue du Parc, les 28 janvier, 18 février et 18 mars 2011. Cette soirée finance, en par- tie, le programme www.headand- hands.ca, d’éducation sexuelle.   Queer evenings with shows at The Playhouse, on Park Avenue, on Janu- ary 28th, February 18th and March 18th. These events funds, in part, the www.headandhands.ca sexual education program.  MEC PLUS ULTRA  @ BELMONT 4483, BOUL. SAINT LAURENT MONTREAL, T. 514-845-8443 Soirées bimensuelles pour hommes, organisées le samedi soir au Belmont, boulevard Saint-Lau- rent, à Montréal.   Every two weeks, a Saturday for gay men, at the Belmont on St-Laurent Boulevard, in Montreal.   MEOW MIX  @ SALA ROSSA  4848, BOUL. SAINT LAURENT MONTRÉAL, T. 514-844-4227 Depuis 10 ans déjà, ces soirées cabaret, art, performances queer pour femmes (et leurs amis) sont organisées une fois par mois à la Sala Rossa, boulevard Saint-Lau- rent.   At the Sala Rossa, on St-Laurent Boulevard, a monthly event of cabaret, art and performances for queer women and their friends.  RED LITE  1755, RUE LIERRE, LAVAL.   T. 450-967-3057.  RED-LITE.NET Le populaire after-hours de Laval. Divers espaces. Clientèle mixte (hétéro et gaie) plutôt enjouée. Particulièrement «gai» les di- manches.   Laval popular after-hours. Mixed crowd  on the party. Mostly gay on Sundays. A must see. SOIRÉES LIPSTICK 3.0  @ LA PORTE ROUGE 1834, AVENUE MONT-ROYAL EST, MONTRÉAL BARSALONPORTEROUGE.COM Soirées mêlant mode, design, arts visuels et nouvelles technologies. Tous les dimanches soirs à La Porte Rouge, avenue Mont-Royal.   Lipstick 3.0, every Sundays, is an evening of fashion design, visual arts, and new technologies at the Porte Rouge Bar, on Mont-Royal Av- enue."
]    
        
for text in doc:
    doc = nlp(text)
    print(f"Text: {text}")
    print(f"Entities: {[(ent.text, ent.label_) for ent in doc.ents]}")
    print()

