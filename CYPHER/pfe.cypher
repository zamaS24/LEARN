// les fichiers caracteristiques-2020.csv et lieux.csv et usagers.csv et vehicules.csv
// devront etre dans le import da la base de données! 


//load accidents
LOAD CSV WITH HEADERS  FROM 'file:///caracteristiques-2020.csv' AS row FIELDTERMINATOR ";"
create (accident:ACCIDENT{
    id:toInteger(row.Num_Acc),
    col:toInteger(row.col),
    intersec:toInteger(row.int),
    date_acc:date({year:toInteger(row.an),month:toInteger(row.mois), day:toInteger(row.jour)}),
    heure_acc:time(row.hrmn),
    lat:toFloat(row.lat),
    long:toFloat(row.long)
})

//Insertion de la route
LOAD CSV WITH HEADERS  FROM 'file:///lieux-2020.csv' AS row FIELDTERMINATOR ";"
merge(route:ROUTE{
    voie:row.voie
})


//I have the accidents, I have the routes

//Il faut matcher les accidents avec 
LOAD CSV WITH HEADERS  FROM 'file:///lieux-2020.csv' AS row FIELDTERMINATOR ";"
match(acc:ACCIDENT{id:toInteger(row.Num_Acc)})
match (route:ROUTE{voie:row.voie})
create (acc)-[:EST_LOCALISE]->(route)


// ajouter les attributs de la route
// catr
// cirv
// nbv 
LOAD CSV WITH HEADERS  FROM 'file:///lieux-2020.csv' AS row FIELDTERMINATOR ";"
match(route:ROUTE{voie:row.voie})
set route.catr = toInteger(row.catr), route.circ =toInteger(row.circ),  route.nbv = toInteger(row.nbv)


//Ajouter les vehicules
//ajouter les vehicules seulement
LOAD CSV WITH HEADERS  FROM 'file:///vehicules-2020.csv' AS row FIELDTERMINATOR ";"
merge(vehicule:VEHICULE{
    id:toInteger(row.id_vehicule)
    })
//remplir les attributs
LOAD CSV WITH HEADERS  FROM 'file:///vehicules-2020.csv' AS row FIELDTERMINATOR ";"
match(v:VEHICULE{id:toInteger(row.id_vehicule)})
set v.catv =toInteger(row.catv), v.choc = toInteger(row.choc), v.manv = toInteger(row.manv), v.motor = toInteger(row.motor)

//les relier avec les accidents
LOAD CSV WITH HEADERS  FROM 'file:///vehicules-2020.csv' AS row FIELDTERMINATOR ";"
match(acc:ACCIDENT{id:toInteger(row.Num_Acc)})
match(vehicule:VEHICULE{id:toInteger(row.id_vehicule)})
create (acc)-[:VEHIC_IMP]->(vehicule)


// creer les pietons 
LOAD CSV WITH HEADERS  FROM 'file:///usagers-2020.csv' AS row FIELDTERMINATOR ";"




// Creer les usagers avec catu et idACC et idVehic


LOAD CSV WITH HEADERS  FROM 'file:///usagers-2020.csv' AS row FIELDTERMINATOR ";"
    create(usager:USAGER{
    id_acc:toInteger(row.Num_Acc),
    id_vehic:toInteger(row.id_vehicule),
    catu:toInteger(row.catu),
    sexe:toInteger(row.sexe),
    trajet:toInteger(row.trajet),
    grav:toInteger(row.grav),
    locp:toInteger(row.loc),
    actp:toInteger(row.actp),
    etatp:toInteger(row.etatp),
    place:toInteger(row.place), 
    secu1:toInteger(row.secu1),
    secu2:toInteger(row.secu2)
    })



// match usager where cat = 3  //pieton
// relate it with the accident. 
// renomer le label en pieton 
//enlever place, secu1,secu2 , et les attributs de accident et vehicule

match(usager:USAGER) where usager.catu = 3
match(accident:ACCIDENT) where accident.id = usager.id_acc
create (accident)-[:PIETON_IMP]->(usager)

//verifier que les usager pieton sont vraiment relier
match(usager:USAGER) where usager.catu = 3 
remove usager.place, usager.secu1, usager.secu2, usager.id_acc, usager.id_vehic
remove usager:USAGER
set usager:PIETON   



//match usager wher cat = passager
// relate it with accident 
// relate it with the vehicule
// renomer le label en passager
//enlever locp, actp, etatp

match(usager:USAGER) where usager.catu = 2
match(accident:ACCIDENT) where accident.id = usager.id_acc
match(vehicule:VEHICULE) where vehicule.id = usager.id_vehic

create (accident)-[:PASS_IMP]->(usager)
create (usager)-[:DANS_VEHIC]->(vehicule)

//verifier que les usager pieton sont vraiment relier
match(usager:USAGER) where usager.catu = 2
remove usager.locp, usager.actp, usager.etatp, usager.id_acc, usager.id_vehic
remove usager:USAGER
set usager:PASSAGER  




//match usager where cat = conducteur
// relate it with accident 
// relate it with vehicule 
// renomer le label en conducteur*
// enelever locp, actp, etatp, place

match(usager:USAGER) where usager.catu = 1
match(accident: ACCIDENT) where accident.id = usager.id_acc
match(vehicule:VEHICULE) where vehicule.id = usage.id_vehic

create (accident)-[:COND_IMP]->(usager)
create (usager)-[:CONDUIT]->(vehicule)

match(usager:USAGER) where usager.catu = 1
remove usager.locp, usager.actp, usager.etatp, usager.place, usager.id_acc, usager.id_vehic
remove usager:USAGER
set usager:CONDUCTEUR



//Ajouter etat de la route
// attribut surf est present dans : lieux 
// attribut atm : caracteristiques
// attribut lum : caracteristiques

// creer (atm lum numacc) 
// avec lieux ajouter surf
// relier avec accident
// supprimer les ids accidents

LOAD CSV WITH HEADERS  FROM 'file:///caracteristiques-2020.csv' AS row FIELDTERMINATOR ";"
create(er:ETATROUTE{
    id_acc:toInteger(row.Num_Acc),
    atm:toInteger(row.atm),
    lum:toInteger(row.lum),
})
//
LOAD CSV WITH HEADERS  FROM 'file:///lieux-2020.csv' AS row FIELDTERMINATOR ";"
match(er:ETATROUTE{id_acc:toInteger(row.Num_Acc)})
set er.surf = toInteger(row.surf)
//
match
    (er:ETATROUTE),
    (acc:ACCIDENT)
where 
    er.id_acc = acc.id
create 
    (acc)-[:DANS_ETAT]->(er)

//
match(er:ETATROUTE)
remove er.id_acc


//ajouter les communes
// com dans caracteristiques 
LOAD CSV WITH HEADERS  FROM 'file:///caracteristiques-2020.csv' AS row FIELDTERMINATOR ";"
merge(commune:COMMUNE{
    id:row.com,
    route:row.adr
})

match
    (route:ROUTE), 
    (commune:COMMUNE)
where   
     route.voie = commune.route
create (route)-[:APP_COMMUNE]->(commune)

match(commune:COMMUNE)
remove commune.route



//rendre les grands id petits
// id_acc
// id vehicule seulement
// id_vehic sup = 154742275, id_vehic min = 154658350 
// 

match(vehicule:VEHICULE)
set vehicule.id = vehicule.id - 154000000

match(accident:ACCIDENT)
set accident.id = accident.id - 202000000000

//requete pour avoir un moins de tout. 
match  
(acc:ACCIDENT)-[:PIETON_IMP]->(pieton:PIETON),
(acc)-[:EST_LOCALISE]->(route:ROUTE{voie:'N/A'}),
(acc)-[]->(p:PASSAGER), (acc)-[]->(conducteur:CONDUCTEUR), 
(acc)-[:VEHIC_IMP]->(v:VEHICULE),
(acc)-[:DANS_ETAT]->(er:ETATROUTE), 
(route)-[:APP_COMMUNE]->(c:COMMUNE{id:'07186'})
return
route,acc,pieton,p,conducteur,v,er ,c
limit 320


//les relier les pietons avec les accidents
match(acc:ACCIDENT)-[:PIETON_IMP]->(pieton:PIETON)
where acc.id = pieton.id_acc
create (acc)-[:PIETON_IMP]->(pieton)

//supprimer le id accident
match(pietonl:PIETON)
set pieton.id_


