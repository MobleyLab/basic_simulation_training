x=1.0:0.1:3.5;

y = 1./x;
h=figure
plot(x,y,'b*')
hold on;
ylj=1./(x.^6);
plot(x,ylj,'r-.')
plot(x,erfc(x),'k-');
hold off
xlabel('distance')
ylabel('function value')
title('Comparison of 1/r, erfc(r) and 1/(r^6)')

set(h,'Units','Inches');
pos = get(h,'Position');
set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])

print(h,'decay_comparison.pdf','-dpdf')