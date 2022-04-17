//LEET CODE 332.Reconstruct Itinerary

class Solution {
    func findItinerary(_ tickets: [[String]]) -> [String] {
        func dfs(_ from: String, _ path: inout [String], _ ticket: inout [[String]]) {
            if path.count == tickets.count + 1 {
                return
            }

            var candidate: [String] = []

            for t in ticket {
                if from == t[0] {
                    candidate.append(t[1])
                }
            }

            candidate = candidate.sorted()
            path.append(candidate[0])
            ticket.remove(at: ticket.firstIndex(of: [from, candidate[0]])!)
            dfs(candidate[0], &path, &ticket)

        }
        var path: [String] = ["JFK"]
        var ticket = tickets

        dfs("JFK", &path, &ticket)

        return path
    }
}