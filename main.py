import pandas as pd

def main():
    magicanalyze()


def magicanalyze():
    magic_data = pd.read_csv("inputs/gamelog.csv")
    winner_dict = {}

    #populate all active decks
    for _, row in magic_data.iterrows():
        for deck in row:

            winner = row["Winner"]

            if winner not in winner_dict:
                winner_dict[winner] = {}

            if deck not in winner_dict:
                winner_dict[deck] = {}

            if deck != winner and not pd.isna(deck):
                if deck not in winner_dict[winner]:
                    winner_dict[winner][deck] = 1
                else:
                    winner_dict[winner][deck] += 1

    winner_matrix = pd.DataFrame(winner_dict)
    winner_matrix = winner_matrix.transpose()
    winner_matrix = winner_matrix.fillna(0) 
    winner_matrix.to_csv('outputs/matrix.csv')

main()
