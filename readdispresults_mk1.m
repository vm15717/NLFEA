[steve,diagKs]=mtxread_mk2;
len1=1:1:3636;
w1=~ismember(len1,diagKs);
finalmodaldispl=[];
finalmodalforce=[];
p=0;
for k=1:10
allmodaldispl=[];
allmodalforce=[];
for i=1:10
 p=p+1;
filename = strcat('force',num2str(p),'.csv');
disp1 = csvread(filename,1,0);
disp1=disp1.';
disp1=disp1(:);
disp1=disp1(w1);
modaldispl=real(steve\disp1);
modalforce=zeros(length(modaldispl),1);
modalforce(1)=(-1.4+(i-1)*(0.3))*(0.001+(k-1)*(0.001));
allmodaldispl=horzcat(allmodaldispl,modaldispl);
allmodalforce=horzcat(allmodalforce,modalforce);
end
finalmodaldispl(:,:,k)=allmodaldispl;
finalmodalforce(:,:,k)=allmodalforce;
end
thetaf=[];
for k=1:10
q1=finalmodaldispl(1,:,k);
fq1=finalmodalforce(1,:,k);
fq1=fq1.';
q1=q1.';
A=[q1 q1.^2 q1.^3 q1.^4 q1.^5 q1.^6 q1.^7 q1.^8 q1.^9];
w=rms(A);
Aw=bsxfun(@rdivide,A,w);
bw=Aw\fq1;
theta11=bw./w';
thetaf=horzcat(thetaf,theta11);
end