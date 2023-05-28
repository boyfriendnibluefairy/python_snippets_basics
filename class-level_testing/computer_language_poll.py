from poll import AnonymousPoll

# Define a query to create an instance of the class
query = "What computer language did you first learn to use?"
my_poll = AnonymousPoll(query)

# Show query and then save the answers to the query
my_poll.display_question()
print("Enter 'q' at any time to quit.\n")
while True:
    answer = input("computer language: ")
    if answer == 'q': break
    my_poll.save_response(answer)

# Display poll results
print("\nThank you for participating in the survey.")
my_poll.display_results()