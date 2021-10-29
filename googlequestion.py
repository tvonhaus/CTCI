def solution(A):
    rows = []
    
    for person in A:
        # if rows empty: create new list within rows
        
        # if not empty: add them to appropriate row
        # # Appropriate row:
        student_added = False
        for current_row in rows:
        # if new person < last person in row:
            if person < current_row[-1]:
                current_row.append(person)
                student_added = True
                break
            # else if new person > last person in row:
        
        if student_added == False:
        # create new row and put new person in new row 
            new_row = []
            new_row.append(person)
            rows.append(new_row)
            # rows.append([person])
        # put new person in same row
    
    print(rows)
    return len(rows)
    
test_list = [5,4,3,6,1]
test_list_2 = [5,3,10,6,11,12,1]

print(solution(test_list))
print(solution(test_list_2))