--FORD ����� ���� �޿��� �޴� ����� �����ȣ�� �˻��϶�.
SELECT EMPNO FROM EMP WHERE SAL = (SELECT SAL FROM EMP WHERE ENAME = 'FORD')AND NOT ENAME = 'FORD';

--�μ��� �ο����� �μ��̸��� �Բ� ����� ���� �μ� ������ �˻��϶�.
select COUNT(*), dname from emp join dept on emp.deptno=dept.deptno GROUP by dname order by COUNT(*) desc;

--�����ȣ, ����̸��� ���� ������������ ���� ������ �˻��϶�.
select a.empno, a.ename from emp a, emp b where a.empno = b.mgr group by a.empno,a.ename order by count(*) desc;

--�μ��̸��� ��SALES���̸鼭 ��������� ��MANAGER���� ����� �����ȣ, ����̸��� ����̸� ������ �˻��϶�.
select empno, ename from emp join dept using(deptno) where dname = 'SALES' AND JOB='MANAGER' ORDER BY ENAME;

--FORD ������� ���� �޿��� �޴� ��� ������ �˻��϶�.
SELECT * FROM EMP WHERE SAL > (SELECT SAL FROM EMP WHERE ENAME = 'FORD');

--ALLEN ������� ���� �޿��� �޴� ��� ������ �˻��϶�.
SELECT * FROM EMP WHERE SAL < (SELECT SAL FROM EMP WHERE ENAME = 'ALLEN');

--20�� �μ� ����� ��������� ���� ��������� �ٸ� �μ��� ��� ������ �˻��϶�.
SELECT * FROM EMP WHERE JOB IN (SELECT JOB FROM EMP WHERE DEPTNO = 20);

--��ü ����� ��� �޿����� �޿��� ���� ��� ������ �˻��϶�.
SELECT * FROM EMP WHERE SAL > (SELECT AVG(SAL) FROM EMP);

--�޿��� ��� �μ����� ��� �޿����� ���� ��� ������ �˻��϶�.
SELECT * FROM EMP WHERE SAL > ALL(SELECT AVG(SAL) FROM EMP GROUP BY DEPTNO);

--20�� �μ��� �ִ� �޿����� �ִ� �޿��� ū �μ��� ��ȣ�� �ִ� �޿��� �˻��϶�.
SELECT DEPTNO, SAL FROM EMP WHERE SAL=(SELECT MAX(SAL) FROM EMP WHERE SAL > (SELECT MAX(SAL) FROM EMP WHERE DEPTNO = '20'));

--CHICAGO ������ ��ġ�ϴ� �μ��� �ٹ��ϴ� ��� ������ �˻��϶�. ��, �� ���Ǹ� �̿��Ѵ�.
SELECT * FROM EMP WHERE DEPTNO=(SELECT DEPTNO FROM DEPT WHERE LOC = 'CHICAGO');







