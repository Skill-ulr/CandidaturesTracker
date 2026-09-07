Je développe cette application web pour m’aider à suivre toutes mes candidatures d’alternance et d’emploi.
L’idée est simple : avoir un espace clair, organisé et centralisé où je peux gérer mes envois, mes relances, mes entretiens et mes notes.
C’est un outil personnel, mais aussi un excellent moyen pour moi d’apprendre et progresser en Django.

1. Ce que je veux faire avec l’application

- J’enregistre chaque candidature : entreprise, poste visé, date d’envoi, lien vers l’annonce, statut actuel.

- Je mets à jour le statut au fur et à mesure (Envoyée → Relancée → Entretien → Acceptée / Refusée).

- Je visualise toutes mes candidatures sous forme de liste ou de tableau, avec des filtres (statut, entreprise, date).

- J’ajoute des notes pour garder une trace de mes échanges ou impressions (ex : “Entretien RH le 15/09, bon feeling, en attente de retour”).

Ce projet m’aide concrètement dans ma recherche, tout en me permettant de pratiquer les bases essentielles de Django : modèles, relations, formulaires, vues, templates et authentification.

2. Fonctionnalités prévues
a.. Tableau de bord avec statistiques et relances automatiques
Je prévois d’ajouter une page d’accueil qui affiche :

- le nombre total de candidatures,

- la répartition par statut (via Chart.js),

- le taux de réponse,

- et une alerte automatique du type :
“Tu n’as pas eu de nouvelles de [Entreprise X] depuis 10 jours, pense à relancer.”


b.. Extraction automatique d’informations depuis une offre d’emploi
Je veux intégrer un champ où je colle le texte d’une annonce (LinkedIn, Indeed…).
L’application détectera automatiquement certains éléments (entreprise, intitulé du poste) pour pré-remplir le formulaire.

C’est une fonctionnalité plus avancée que j’ajouterai une fois les fondations terminées.
