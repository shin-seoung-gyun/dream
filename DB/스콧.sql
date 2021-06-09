--������ NEW YORK�� ����� �����ȣ, ����̸��� �����ȣ ������ �˻��϶�.
select empno, ename from emp join dept using(deptno)where dept.loc='NEW YORK' order by empno;

--ALLEN ����� �ٹ� ���� �μ��̸��� ������ �˻��϶�(equi join)
SELECT DNAME, LOC FROM EMP,DEPT WHERE emp.deptno=dept.deptno AND ENAME='ALLEN';

--ALLEN ����� �ٹ� ���� �μ��̸��� ������ �˻��϶�(join ~ using)
SELECT DNAME, LOC FROM EMP JOIN DEPT USING(DEPTNO) WHERE ENAME='ALLEN';

--ALLEN ����� �ٹ� ���� �μ��̸��� ������ �˻��϶�(join ~ on)
SELECT DNAME, LOC FROM EMP JOIN DEPT ON DEPT.DEPTNO=EMP.DEPTNO WHERE ENAME='ALLEN';

--ALLEN ����� �ٹ� ���� �μ��̸��� ������ �˻��϶�(natural join)
SELECT DNAME, LOC FROM EMP NATURAL JOIN DEPT WHERE ENAME='ALLEN';

--�޿��� 2000 �̻��� ������� ������ ������ �˻��϶�
SELECT ENAME, LOC FROM DEPT, EMP WHERE DEPT.DEPTNO=emp.deptno AND SAL>= 2000;

--�޿��� 1000 �̻� 2000 ������ ������� �����ȣ, ����̸�, �μ��̸��� �����ȣ������ �˻��϶�.
SELECT ENAME, LOC FROM DEPT, EMP WHERE DEPT.DEPTNO=emp.deptno AND SAL<= 2000 AND SAL>=1000 ORDER BY EMPNO;

--��������� SALESMAN�̸鼭 CHICAGO ������ �ٹ����� ������� �˻��϶�.
SELECT ENAME FROM EMP JOIN DEPT USING(DEPTNO) WHERE LOC='CHICAGO' AND JOB='SALESMAN';

--NEW YORK �̳� DALLAS ������ �ٹ��ϴ� ������� �����ȣ�� ����̸��� �����ȣ ������ �˻��϶�(equi join).
SELECT EMPNO, ENAME FROM EMP JOIN DEPT USING(DEPTNO) WHERE LOC='NEW YORK' OR LOC='DALLAS' ORDER BY EMPNO;

--�μ��̸��� ACCOUNTING�̰ų�, ������ CHICAGO�̴� ����� �����ȣ�� ����̸��� �˻��϶�.
SELECT EMPNO, ENAME FROM EMP JOIN DEPT USING(DEPTNO) WHERE LOC='CHICAGO' OR DNAME='ACCOUNTING';

--NEW YORK�̳� DALLAS ������ �ٹ��ϴ� ������� �����ȣ�� ����̸��� �����ȣ ������ �˻��϶�(natural join)
SELECT EMPNO, ENAME FROM EMP NATURAL JOIN DEPT WHERE LOC = 'NEW YORK' OR LOC = 'DALLAS' ORDER BY EMPNO;

--�μ��̸��� ACCOUNTING�̰ų�, ������ CHICAGO�� ����� �����ȣ�� ����̸��� �˻��϶�(join~using).
SELECT EMPNO, ENAME FROM EMP JOIN DEPT USING(DEPTNO) WHERE LOC = 'CHICAGO' OR DNAME = 'ACCOUNTING';

--�����ȣ, ����̸�, �޿�, �޿������ �޿���޺� �����ȣ ������ �˻��϶�.
SELECT EMPNO, ENAME, SAL, GRADE FROM EMP,salgrade WHERE SAL>= LOSAL AND SAL <=HISAL ORDER BY GRADE, EMPNO;

--�����ȣ, ����̸�, ����ڻ����ȣ, ������̸��� �˻��϶�(equi join)
SELECT A.EMPNO, A.ENAME, B.EMPNO, B.ENAME FROM EMP A ,EMP B WHERE A.MGR=B.EMPNO;

--�����ȣ, ����̸�, ����ڻ����ȣ, ������̸��� �˻��϶�(join ~~ on)
SELECT A.EMPNO, A.ENAME, B.EMPNO, B.ENAME FROM EMP A JOIN EMP B ON A.MGR=B.EMPNO;

--BLAKE ������� ���� �޿��� �޴� ����̸��� �˻��϶�(������)
SELECT ENAME FROM EMP WHERE SAL > (SELECT SAL FROM EMP WHERE ENAME = 'BLAKE');

--BLAKE ������� ���� �޿��� �޴� ����̸��� �˻��϶�(self join)
SELECT A.ENAME FROM EMP A, EMP B WHERE B.ENAME='BLAKE' AND A.SAL>B.SAL;

--FORD ����� ���� �μ��� �ٹ��ϴ� ����̸��� �˻��϶�.
SELECT ENAME FROM EMP WHERE DEPTNO = (SELECT DEPTNO FROM EMP WHERE ENAME = 'FORD')AND NOT ENAME = 'FORD';

--FORD ����� ���� �޿��� �޴� ����� �����ȣ�� �˻��϶�.
SELECT EMPNO FROM EMP WHERE SAL = (SELECT SAL FROM EMP WHERE ENAME = 'FORD')AND NOT ENAME = 'FORD';











