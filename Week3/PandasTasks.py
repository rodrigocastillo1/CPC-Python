import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def swapColumns(df, col1, col2):
    cols = list(df.columns)
    col1_idx, col2_idx = cols.index(col1), cols.index(col2)
    cols[col1_idx], cols[col2_idx] = cols[col2_idx], cols[col1_idx]
    return df[cols]

def PandasTasks():
    # 1. Read CSV file and transfer it into DataFrame
    dataTitanic = pd.read_csv("dataTitanic.csv")
    print("> 1. Imported data\n", dataTitanic)
    
    # 2. Transfer object Series into index column of the dataframe
    dataTitanic = dataTitanic.set_index('PassengerId')
    print("> 2. Use PassengerId as index column\n", dataTitanic)

    # 3. Change the data in the column of DataFrame according to some condition
    dataTitanic2 = dataTitanic
    dataTitanic2['Pclass'] = np.where(dataTitanic2['Survived'] == 1, 1, 3)
    print("> 3. Change Pclass to 1 if survived\n", dataTitanic2)

    # 4. Get names of the DataFrame columns and sum of missed values DF
    print("> 4.1 Name of columns\n", dataTitanic.columns)
    print("> 4.1 Number of empty fields\n", dataTitanic.isnull().sum())

    # 5. Ex-change 2 columns, use function for it. Sort coulumn by name
    dT2 = swapColumns(dataTitanic, 'Survived', 'Pclass')
    print("> 5.1 Swap Survived and Pclass columns\n:", dT2)
    dataTitanic = dataTitanic.reindex(columns=sorted(dataTitanic.columns))
    print("> 5.2 Sorted Columns\n", dataTitanic)

    # 6. Delete upper and lower 5% in object DataFrame
    # I'll do this considering the column Age.
    lower_limit = dataTitanic['Age'].quantile(0.05)
    upper_limit = dataTitanic['Age'].quantile(0.95)
    dataTitanic = dataTitanic[(dataTitanic['Age'] >= lower_limit) & (dataTitanic['Age'] <= upper_limit)]
    print("> 6. Filtered data by Age (excluded: upper and lower 5%)\n", dataTitanic)

    # 7. Replay (Apply) missed values in the Column with average values.
    dataTitanic['Age'] = dataTitanic['Age'].replace(0, np.nan)
    dataTitanic['Age'] = dataTitanic['Age'].fillna(dataTitanic['Age'].mean())
    print("> 7. Using average age to replace missed and 0 values\n", dataTitanic)

    # 8. Create two data frames using the two Dicts.
    #    Merge two data frames, and append the second data frame as a new
    #    column to the first data frame.
    songsDict = {"Song": ["Billie Jean", "Take On Me", "Sweet Child O' Mine", "With or Without You"],
                "Artist": ["Michael Jackson", "A-ha", "Guns N' Roses", "U2"],
                "Album": ["Thriller", "Hunting High and Low", "Appetite for Destruction", "The Joshua Tree"]}
    lengthDict = {"Length": ["4:54", "3:45", "5:55", "4:56"]}
    songsDF = pd.DataFrame(songsDict)
    lengthDF = pd.DataFrame(lengthDict)
    print("> 8.1 Songs DataFrame\n", songsDF)
    print("> 8.1 Length DataFrame\n", lengthDF)
    resultDF = pd.concat([songsDF, lengthDF], axis=1)
    print("> 8.2 Append length DataFrame as new column of songs DataFrame:\n", resultDF)
    
    # 9. For any column create histogram
    print("9. See histogram plot.")
    dataTitanic['Age'].hist(bins=8)
    plt.title('Age distribution of Titanic passengers')
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()
    
    # 10. Create Correlation Matrix for any column
    corr_matrix = dataTitanic[["Age", "Pclass", "Fare"]].corr()
    print("10. Correlation matrix between Age of passengers, Travel class and Fare\n", corr_matrix)
    
    return

def main():
    print("This program will execute the tasks of the Pandas module of CPC course.")
    PandasTasks()

if __name__ == "__main__":
    main()