import pandas as pd
import numpy as np

# ---- Exercises ----

def exercise_1():
    """Create a Pandas Series with values 1 to 10."""
    return pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def exercise_2():
    """Create a Pandas Series with custom indices from 'a' to 'j'."""
    return pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

def exercise_3():
    """Create a Pandas Series from a dictionary with country names as index and population numbers as values."""
    data = {'USA': 331, 'India': 1380, 'China': 1441, 'Brazil': 213, 'Nigeria': 206}
    return pd.Series(data)

def exercise_4():
    """Create a Pandas Series with 15 equally spaced values between 1 and 100."""
    return pd.Series(np.linspace(1, 100, 15))

def exercise_5():
    """Create a DataFrame for people with name, age, and profession."""
    return pd.DataFrame([['Alice', 24, 'Engineer'], ['Bob', 27, 'Doctor'], ['Charlie', 22, 'Artist']], 
                        columns=['Name', 'Age', 'Profession'])

def exercise_6():
    """Create a DataFrame from a dictionary."""
    data = {
        'Student': ['Jake', 'John', 'Emma', 'Sophia'],
        'Grade': ['A', 'B', 'A', 'C'],
        'Age': [20, 21, 19, 22]
    }
    return pd.DataFrame(data)

def exercise_7():
    """Return the first 5 rows of a DataFrame."""
    df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
    return df.head()

def exercise_8():
    """Select a column from a DataFrame."""
    df = pd.DataFrame({
        'Name': ['Jake', 'John', 'Emma', 'Sophia'],
        'Age': [20, 21, 19, 22],
        'Grade': ['A', 'B', 'A', 'C']
    })
    return df['Age']

def exercise_9():
    """Filter rows in a DataFrame where age is greater than 20."""
    df = pd.DataFrame({
        'Name': ['Jake', 'John', 'Emma', 'Sophia'],
        'Age': [20, 21, 19, 22],
        'Grade': ['A', 'B', 'A', 'C']
    })
    return df[df['Age'] > 20]

def exercise_10():
    """Sort a DataFrame by a column (Age) and reset index."""
    df = pd.DataFrame({
        'Name': ['Jake', 'John', 'Emma', 'Sophia'],
        'Age': [20, 21, 19, 22],
        'Grade': ['A', 'B', 'A', 'C']
    })
    return df.sort_values(by='Age', ignore_index=True)


# ---- Test Cases ----

def run_tests():
    # Exercise 1 Test Case
    series_default = exercise_1()
    assert series_default.equals(pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), "Exercise 1 Test Case Failed"

    # Exercise 2 Test Case
    series_custom = exercise_2()
    assert series_custom.equals(pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])), "Exercise 2 Test Case Failed"

    # Exercise 3 Test Case
    series_population = exercise_3()
    assert series_population.equals(pd.Series({
        'USA': 331,
        'India': 1380,
        'China': 1441,
        'Brazil': 213,
        'Nigeria': 206
    })), "Exercise 3 Test Case Failed"

    # Exercise 4 Test Case
    linspace_series = exercise_4()
    assert len(linspace_series) == 15, "Exercise 4 Test Case Failed"
    assert linspace_series.iloc[-1] == 100, "Exercise 4 Test Case Failed"

    # Exercise 5 Test Case
    df_people = exercise_5()
    expected_df_people = pd.DataFrame([
        ['Alice', 24, 'Engineer'],
        ['Bob', 27, 'Doctor'],
        ['Charlie', 22, 'Artist']
    ], columns=['Name', 'Age', 'Profession'])
    assert df_people.equals(expected_df_people), "Exercise 5 Test Case Failed"

    # Exercise 6 Test Case
    df_dict = exercise_6()
    expected_df_dict = pd.DataFrame({
        'Student': ['Jake', 'John', 'Emma', 'Sophia'],
        'Grade': ['A', 'B', 'A', 'C'],
        'Age': [20, 21, 19, 22]
    })
    assert df_dict.equals(expected_df_dict), "Exercise 6 Test Case Failed"

    # Exercise 7 Test Case
    df_head = exercise_7()
    assert len(df_head) == 5, "Exercise 7 Test Case Failed"

    # Exercise 8 Test Case
    series_age = exercise_8()
    assert series_age.equals(pd.Series([20, 21, 19, 22], name='Age')), "Exercise 8 Test Case Failed"

    # Exercise 9 Test Case
    df_filtered = exercise_9()
    expected_filtered = pd.DataFrame({
        'Name': ['John', 'Sophia'],
        'Age': [21, 22],
        'Grade': ['B', 'C']
    }, index=[1, 3])
    assert df_filtered.equals(expected_filtered), "Exercise 9 Test Case Failed"

    # Exercise 10 Test Case
    df_sorted = exercise_10()
    expected_sorted = pd.DataFrame({
        'Name': ['Emma', 'Jake', 'John', 'Sophia'],
        'Age': [19, 20, 21, 22],
        'Grade': ['A', 'A', 'B', 'C']
    })
    assert df_sorted.equals(expected_sorted), "Exercise 10 Test Case Failed"

    print("All tests passed!")
# ---- Main ----

if __name__ == "__main__":
    run_tests()
