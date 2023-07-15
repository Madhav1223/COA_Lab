def fifo(frame_size):
    page_faults = 0
    frame = []
    while True:
        page = input("Enter the page number (press 'q' to stop): ")
        if page == 'q':
            break
        page = int(page)
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1
        print(f"Page {page} -> Frame: {frame}")
    return page_faults



def lru(frame_size):
    page_faults = 0
    frame = []
    time_stamp = []
    
    while True:
        page = input("Enter the page number (press 'q' to stop): ")
        if page == 'q':
            break
        page = int(page)
        
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
                time_stamp.append(page)
            else:
                oldest_page = time_stamp.pop(0)
                frame.remove(oldest_page)
                frame.append(page)
                time_stamp.append(page)
            page_faults += 1
        else:
            time_stamp.remove(page)
            time_stamp.append(page)
        
        print(f"Page {page} -> Frame: {frame}")
        
    return page_faults



def menu(size):
    while True:
        print("\n------- Cache Algorithm Menu -------")
        print("1. LRU (Least Recently Used)")
        print("2. FIFO (First-In, First-Out)")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            faults =fifo(frame_size=size)
            print(f"Total page faults: {faults}")
            exit
        elif choice == "2":
            faults=lru(frame_size=size)
            print(f"Total page faults: {faults}")
            exit
        elif choice == "0":
            print("Exiting the program...")
            exit(0)
        else:
            print("Invalid choice. Please try again.")



frame_size = int(input("Enter the size of the page frame: "))
menu(frame_size)
