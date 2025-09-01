// platform: {platform}
// id: {id}
// title: {title}
// url: {url}
// tags: {tags}
// date: {date}
// language: C++
// time: {time}
// space: {space}
// status: {status}

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line, all;
    while (getline(cin, line)) {
        all += line;
        if (!cin.eof()) all += "\n";
    }
    // TODO: implement solution
    if (!all.empty()) cout << all;
    return 0;
}
