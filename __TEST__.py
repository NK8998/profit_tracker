        def edit_user(_):
            id = table.item(table.selection())["values"][0]
            user_arr = []
            selectedUser_arr = []
            for val in User.show_user():
                # print(val)
                if val[0] == loggedInUserID:
                    user_arr = val
                if val[0] == id:
                    selectedUser_arr = val

            def update():
                pword = pwInput.get()
                # print(pword,user_arr[5])
                if pword == user_arr[5]:
                    User.update_user(
                        id,
                        empIDInput.get(),
                        fnameInput.get(),
                        lnameInput.get(),
                        salaryInput.get(),
                        natIDInput.get(),
                    )
                    desturi("User edited", "User successfully edited")
                else:
                    desturi("Wrong password", "Wrong password entered")
                return