clear all;
clc

nNode = 10;
nodes = [(1:nNode); [25 15 25 35 15 25 35 15 25 35]; 
                    [5 15 15 15 25 25 25 35 35 35]]';
nSeg  = 19;
segments = [(1:nSeg); 
            [1 1 1 2 2 2 5 5 3 3 8 6 6 6 6 6  7  9  6]; 
            [2 3 5 3 5 6 8 6 4 6 6 5 3 4 7 10 10 10 9]]';
figure; 
plot(nodes(:,2), nodes(:,3),'k.');
hold on;

for s = 1:nSeg
    if (s <= nNode) 
        text(nodes(s,2),nodes(s,3),[' ' num2str(s)]); 
    end
    plot(nodes(segments(s,2:3)',2),nodes(segments(s,2:3)',3),'k');
    grid on;
    pause(0.1);
end
[d, p] = dijkstra(nodes, segments, 1, 10)
for n = 2:length(p)
    plot(nodes(p(n-1:n),2),nodes(p(n-1:n),3),'r-.','linewidth',2);
end
hold off;