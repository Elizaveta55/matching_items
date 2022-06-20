# Matching items task

This is a short description of scripts and its functionality written in the order how it can be launched:

1. ```ksr_to_csv.py``` forms .csv file from huge ksr.doc file for the sake of convenience.
2. ```excel_to_csv.py``` forms .csv file from file with orders and requests.
3. ```match_items_from_excel_and_ksr.py``` search for similar items in KSR and Orders file. It analyses intersection of words in names between two items and in case the similarity level is higher than chosen similarity level - two items are considered to be very similar (identical in the best case).

Final answers are presented in file ```final.xslx```

The solution is quite elemental - it was the first assumption to check. The following sections represent how to improve the approach or how to consider another approach in order to improve performance.

## Updates were made:

These changes are presented in folder ```second```. The main changes are
1. Results were divided into two files - found and not found.
2. About matching - there was added new condition of similarity of leading words. Leading word - the first word in the name which identifies the object (in most cases this word is the first one). Example of leading word in name "Молоток 500гр дер.ручка" is "Молоток".
3. For not found items reasons (possible explanations) were added.

Final answers are presented in file ```final_found.xslx```and ```final_not_found.xslx```

## Updates to be done:

This section represent possible approached to add in order to improve the model
1. [Existing approach] - write script for identification of leading word because in some cases leading word might not be on the first place in the name.
2. [Another approach] - train representation model with contrastive loss. Contrastive loss could help to focus on similarity of attributes efficiently.
