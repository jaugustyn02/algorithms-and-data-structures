while j < E:
    if check_connectivity(adj_ls, V):  # O(2*V)
                min_time = min(min_time, ED[j][0] - ED[i][0])
                adj_ls[ED[i][1]].popleft()
                adj_ls[ED[i][2]].popleft()
                # adj_ls[ED[i][1]].remove(ED[i][2])
                # adj_ls[ED[i][2]].remove(ED[i][1])
                i += 1
            else:
                j += 1
                if j < E:
                    adj_ls[ED[j][1]].append(ED[j][2])
                    adj_ls[ED[j][2]].append(ED[j][1])