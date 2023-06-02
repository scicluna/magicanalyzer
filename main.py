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
                    winner_dict[winner][winner] = 0
                else:
                    winner_dict[winner][deck] += 1

    wm = pd.DataFrame(winner_dict)
    wm = wm.transpose()
    wm = wm.fillna(0) 
    wm = wm.sort_index(axis=0)
    wm = wm.sort_index(axis=1)

    # Compute total wins
    wm['Total Wins'] = wm.sum(axis=1)

    # Compute total losses
    wm['Total Losses'] = wm.sum(axis=0)

    # Compute win percentage
    wm['Win Percentage'] = wm['Total Wins'] / (wm['Total Wins'] + wm['Total Losses'])

    # Move 'Total Wins', 'Total Losses', and 'Win Percentage' to the beginning
    cols = ['Total Wins', 'Total Losses', 'Win Percentage']  + [col for col in wm if col not in ['Total Wins', 'Total Losses', 'Win Percentage']]
    wm = wm[cols]

    wm.to_csv('outputs/matrix.csv')

main()
