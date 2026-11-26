# An exact Fourier recurrence for the mixed two-crossing source

The pendant pair with powers \(2,-2\) has a useful exact description
in terms of one polynomial with positive coefficients. This does not
make the entire boundary source positive: recovering that source
requires finite differences and another summation. It does, however,
give a recurrence with a specified forcing term, a unique solution,
and an explicit estimate for transporting errors in that recurrence.

All crossing powers are fixed before the quantum level tends to
infinity. The calculations below concern the original finite
algebra, including derivatives at its repeated roots.

## 1. The mixed boundary polynomial

Fix \(N\ge2\), and write
\[
 D=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 s_a=2\sin(\pi a/N),\qquad
 S_a=\prod_{r=1}^{a}s_r,\quad S_0=1.
 \tag{1}
\]
In particular \(S_D=N\). This follows by evaluating
\((X^N-1)/(X-1)\) at \(X=1\) and taking absolute values.
Let \(M\) be the original crossing matrix, \(J\) coefficient reversal,
and \(e_0,\ldots,e_D\) the normalized real Newton basis of
\(\mathbb C[z]/(2T_N(z/2)+2)\). The conventions are those of the
[finite Newton calculus](../papers/newton-calculus/finite.tex).
The vector \(e_0\) also denotes the coefficient column of the unit.

The boundary element of the pendant word \(T(R^{-2}T(R^2))\) is
\[
 Z_N=JM^{-2}JM^2e_0=(M^2)^*M^2e_0.
 \tag{2}
\]
Here the star is conjugate transpose. Indeed \(M^{-1}=\overline M\)
and \(JM^nJ=(M^n)^T\). The Gram-matrix expression in (2) is exact,
but its pairing with an arbitrary boundary evaluation vector is
not a squared norm.

The [two-crossing identity](research_degree_two_power_two_formula.md)
gives, with \(a=D-k\),
\[
 (M^2)_{k,j}
 =N i^{a+j}
     q^{((a-j)^2-a-j)/2}
       \frac{S_{a+j}}{S_a^2S_j^2},\qquad 0\le j\le k.
 \tag{3}
\]
Multiplying its conjugate by the zeroth column gives the \(j\)th
Newton coefficient of (2):
\[
 [Z_N]_j
 =\frac{N^2 i^{-j}q^{-j(j-1)/2}}{S_j^2}
       \sum_{a=0}^{D-j}q^{aj}\frac{S_{a+j}}{S_a^3}.
 \tag{4}
\]
Thus (4) determines the entire canonical polynomial, rather than
only its values at distinct spectral roots.

Define the ordinary polynomial
\[
 B_N(X)=\sum_{a=0}^{D}\frac{X^a}{S_a^2},
 \qquad (Ef)(X)=f(QX).
 \tag{5}
\]
For a nonnegative integer \(j\), let
\[
 (QE;Q)_j=\prod_{r=1}^{j}(1-Q^rE),
 \qquad G_{j,N}=\bigl((QE;Q)_jB_N\bigr)(1).
 \tag{6}
\]
The empty product is the identity. Since
\[
 q^{aj}\frac{S_{a+j}}{S_a}
       =i^j q^{-j(j+1)/2}(Q^{a+1};Q)_j,
\]
equation (4) becomes
\[
 \boxed{\displaystyle
 Z_N(z)=N^2\sum_{j=0}^{D}
       \frac{q^{-j^2}}{S_j^2}\,G_{j,N}\,e_j(z).}
 \tag{7}
\]
One may sum over all \(0\le a<N\) in (6): when \(a+j\ge N\),
the factor \((Q^{a+1};Q)_j\) is zero. No denominator vanishes.
In particular
\[
 [Z_N]_0=N^2B_N(1)>0.
 \tag{8}
\]
Neither (8) nor positive definiteness of the Gram matrix implies
positivity of (7) at a general boundary angle.

## 2. A forced recurrence and its unique solution

The elementary factorial recurrence is
\[
 (1-Q^a)^2S_a^{-2}=-Q^aS_{a-1}^{-2},
                 \qquad 1\le a<N.
 \tag{9}
\]
Taking coefficients in (5) therefore proves the polynomial identity
\[
 \boxed{\displaystyle
 B_N(X)+(QX-2)B_N(QX)+B_N(Q^2X)=\frac{X^N}{N^2}.}
 \tag{10}
\]
The right side is the last term of the finite sum. It would be lost
by replacing the polynomial with a formal infinite solution of the
homogeneous recurrence.

Set \(h_j=B_N(Q^j)\). These are precisely the discrete Fourier
coefficients of the positive sequence \(S_a^{-2}\), with the
displayed choice of sign and no factor \(N^{-1}\). They satisfy
\[
 h_{j+N}=h_j,\qquad
 h_j+(Q^{j+1}-2)h_{j+1}+h_{j+2}=N^{-2}.
 \tag{11}
\]
Thus the recurrence uses both the forcing and periodic boundary
conditions.

There is a particularly simple uniqueness proof. On
\(\mathcal V_N=\mathbb C[X]/(X^N-1)\), define
\[
 L_N=(1-E)^2+QXE.
 \tag{12}
\]
If \(v=\sum_{a=0}^{D}v_aX^a\) and \(f=L_Nv\), then
\[
 f_0=v_D,\qquad
 f_a=Q^a(v_{a-1}-s_a^2v_a),\quad 1\le a\le D.
 \tag{13}
\]
Starting from \(v_D=f_0\), these equations determine all coefficients
successively. In the monomial basis the determinant is exactly one:
the diagonal entry in row zero is zero, so the only nonzero
permutation in the determinant uses the entire cyclic off-diagonal.
Its sign and phase give
\[
 \det L_N=(-1)^{N-1}Q^{N(N+1)/2}=1.
 \tag{14}
\]
Consequently \(B_N\) is the unique element of \(\mathcal V_N\)
satisfying \(L_NB_N=N^{-2}\). The ordinary identity (10) fixes its
degree-less-than-\(N\) representative.

## 3. Exact transport of a general forcing term

Solving (13) backwards yields
\[
 \boxed{\displaystyle
 v_a=\frac1{S_a^2}
       \left(N^2f_0+
          \sum_{b=a+1}^{D}Q^{-b}S_{b-1}^2f_b\right),
       \qquad 0\le a\le D.}
 \tag{15}
\]
For \(a=D\) this uses \(S_D=N\) and gives \(v_D=f_0\).
Substituting (15) in every other row proves the formula directly.
After multiplication by \(S_a^2\), transport is just a finite
one-sided sum.

For example, the explicit bound is
\[
 \max_a S_a^2|v_a|
 \le N^2|f_0|+\sum_{b=1}^{D}S_{b-1}^2|f_b|.
 \tag{16}
\]
If \(f_0=0\) and \(|f_b|\le A_N/S_{b-1}^2\), the right side is at
most \(NA_N\). This is a stability estimate in specified factorial
weights. It is not a stability estimate for arbitrary unweighted
errors in a different representation of the boundary source.

For the original forcing, \(f_0=N^{-2}\), \(f_b=0\) for \(b>0\),
formula (15) gives exactly \(v_a=S_a^{-2}\). The original solution
and its normalization have therefore been recovered without choosing
a solution of an unforced recurrence.

## 4. Exponential scales of the period and the inverse operator

Let
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 v_3=-2\pi J(1/6)>0.
 \tag{17}
\]
The constant \(v_3\) is also the volume of a regular ideal
tetrahedron. Only its integral definition is needed here.
The uniform factorial estimate is
\[
 \log S_a=NJ(a/N)+O(\log N),\qquad 0\le a<N,
 \tag{18}
\]
with an absolute implied constant. It follows by separating the
logarithmic endpoint singularities and comparing the remaining
Riemann sums; the estimate is included in the
[uniform factorial proof](research_uniform_factorial_and_boundary_decay.md).

On \([0,1]\), \(J\) has its unique global minimum at \(1/6\), and
its unique global maximum at \(5/6\), with
\[
 J(1/6)=-v_3/(2\pi),\qquad J(5/6)=v_3/(2\pi).
 \tag{19}
\]
These assertions follow from \(J'(x)=\log(2\sin\pi x)\),
\(J(1-x)=-J(x)\), and \(J(0)=J(1)=0\).
Bounding a positive sum by its largest term and \(N\) times that
term now proves
\[
 \lim_{N\to\infty}\frac1N\log B_N(1)=\frac{v_3}{\pi}.
 \tag{20}
\]
The same argument, or the exact Parseval identity, gives
\[
 \frac1{2\pi}\int_0^{2\pi}|B_N(e^{it})|^2\,dt
        =\sum_{a=0}^{D}S_a^{-4},
 \qquad
 \lim_{N\to\infty}\frac1{2N}
       \log\sum_{a=0}^{D}S_a^{-4}=\frac{v_3}{\pi}.
 \tag{21}
\]

The norm of the full inverse operator is larger. Use the coefficient
maximum norm on \(\mathcal V_N\). Formula (15) shows that its entries,
apart from the first column, have absolute values
\[
 \frac{S_{b-1}^2}{S_a^2}
       =\prod_{r=a+1}^{b-1}s_r^2,\qquad a<b.
 \tag{22}
\]
The first column has entries \(N^2/S_a^2\). The largest possible
increase of \(J\) along an ordered interval is
\(J(5/6)-J(1/6)=v_3/\pi\). Choosing \(a/N\to1/6\) and
\((b-1)/N\to5/6\) gives the matching lower bound. Since the
maximum row sum differs from the largest entry by at most a
factor \(N\), (18) proves
\[
 \boxed{\displaystyle
 \lim_{N\to\infty}\frac1N
          \log\|L_N^{-1}\|_{\infty\to\infty}
                   =\frac{2v_3}{\pi}.}
 \tag{23}
\]
Thus determinant one and uniqueness of the forced algebraic solution
do not imply a small norm for its transport. Formula (16) supplies
the weights in which this particular recurrence is controlled.

## 5. What the recurrence proves about the boundary problem

Equations (7), (10), and (15) are identities for the original finite
source. They preserve the forcing, the Fourier phases, and every
Newton coefficient. They are useful for an approach based on
transporting estimates from a boundary condition.

The volume statement needs more than the positive-period limit (20).
In (7), the operators \((QE;Q)_j\) have orders as large as \(N-1\),
and the final Newton reconstruction is oscillatory. The factorial
weights in (16) must be compared with the errors produced by those
two operations. No such comparison, noncancellation theorem, or
whole-boundary asymptotic is inferred here from uniqueness of (10).
The separate [mixed boundary theorem](research_mixed_two_crossing_boundary_theorem.md)
now supplies a nonzero leading term and the whole-boundary estimate
by an exact contour argument. Thus those analytic conclusions no
longer remain open for this word. They do not follow from uniqueness
of (10); the weighted recurrence is an alternative description of
the same finite source, whose usefulness for more general words
still needs to be established.

## 6. A recurrence for the full transformed coefficients

The finite differences in (6) also satisfy a closed recurrence. This
recurrence determines the actual coefficients in (7), including their
normalization. It does not require a choice among solutions of a
homogeneous equation.

For this section write \(G_j=G_{j,N}\), and set
\[
 A_j=Q^{j+1},\qquad s_Q=1+Q^{-1}+Q^{-2}.
 \tag{24}
\]
Then, for every integer \(j\ge0\),
\[
 \begin{split}
 0={}&Q^{-3}G_{j+3}
  +\left[-A_j^2+Q^{-1}(3A_j-s_Q)\right]G_{j+2}\\
 &+\left[4A_j^2-3(1+Q^{-1})A_j+s_Q\right]G_{j+1}
  +(A_j-1)^3G_j.
 \end{split}
 \tag{25}
\]
Its terminal conditions are
\[
 G_{N-1}=N,\qquad G_j=0\quad(j\ge N).
 \tag{26}
\]
In particular, (25), together with \(G_{N-1}=N\) and
\(G_N=G_{N+1}=0\), uniquely determines \(G_0,\ldots,G_{N-1}\).
Indeed \(A_j-1\ne0\) for \(0\le j\le N-2\), so (25) can be
solved backwards. No division by a vanishing coefficient is used.

Here is a direct proof of (25). For a polynomial \(f\), define
\[
 \mu_N[f]=\sum_{a=0}^{N-1}S_a^{-2}f(Q^a).
 \tag{27}
\]
The weight recurrence (9), with the wrap from \(a=N-1\) to
\(a=0\) retained, gives
\[
 \mu_N\left[(1-z)^2f(z)+Qz f(Qz)\right]
       =N^{-2}f(1).
 \tag{28}
\]
For clarity, the first summand on the left is
\(-\sum_{a=1}^{N-1}Q^aS_{a-1}^{-2}f(Q^a)\). The second is
the same sum with the opposite sign, together with
\(Q^NS_{N-1}^{-2}f(Q^N)=N^{-2}f(1)\).

Put \(P_j(z)=(Qz;Q)_j\) and apply (28) to
\(f(z)=(1-z)P_j(z)\). The right side vanishes, and
\((1-Qz)P_j(Qz)=(1-A_jz)P_j(z)\). Thus
\[
 \mu_N\left[
    \{1+(Q-3)z+(3-QA_j)z^2-z^3\}P_j(z)
             \right]=0.
 \tag{29}
\]
The elementary Newton-basis identities are
\[
 \begin{aligned}
 zP_j&=A_j^{-1}(P_j-P_{j+1}),\\
 z^2P_j&=A_j^{-2}
   \left[P_j-(1+Q^{-1})P_{j+1}+Q^{-1}P_{j+2}\right],\\
 z^3P_j&=A_j^{-3}
   \left[P_j-s_QP_{j+1}+Q^{-1}s_QP_{j+2}-Q^{-3}P_{j+3}\right].
 \end{aligned}
 \tag{30}
\]
Substituting (30) in (29), multiplying by \(A_j^3\), and using
\(\mu_N[P_j]=G_j\) proves (25). The conditions (26) follow
directly from the products: for \(j\ge N\), every summand
contains \(1-Q^N\); for \(j=N-1\), only \(a=0\) survives,
and its product is \((Q;Q)_{N-1}=N\).

The coefficient sequence of the original canonical boundary
polynomial is recovered from this recurrence by the explicit gauge
\(N^2q^{-j^2}S_j^{-2}\) in (7). In particular, (25) is an exact
quantum recurrence for this source. This statement does not identify
it with a normalized knot A-polynomial: the variable here is the
Newton index, and the gauge and terminal conditions are part of the
construction.

## 7. The characteristic curve and the original stationary equation

In the commutative limit of (25), replace \(Q\) by \(1\), keep
\(A\) as an independent variable, and replace the forward shift in
\(j\) by a variable \(r\). The resulting polynomial is
\[
 \mathcal P(A,r)=r^3+(-A^2+3A-3)r^2
                 +(4A^2-6A+3)r+(A-1)^3.
 \tag{31}
\]
This algebraic operation specifies the characteristic curve; it does
not assert an asymptotic approximation to any solution of (25).

There is a direct connection to the stationary equations of the
original mixed sum. With \(X=e^{2\pi ix}\) and
\(Y=e^{2\pi iy}\), the part of its phase depending on the first
summation variable has derivative
\[
 W_x=\log(2\sin\pi(x+y))-3\log(2\sin\pi x)+i\pi y.
 \tag{32}
\]
The logarithms in (32) are continued on a zero-free phase chart.
Exponentiating \(W_x=0\), and using
\(2\sin\pi x=i e^{-i\pi x}(1-X)\), gives
\[
 X^2Y-X=(1-X)^3.
 \tag{33}
\]
At the summand level in (6), increasing \(j\) by one multiplies
the product by \(1-Q^{a+j+1}\). Its classical value is
\(r=1-XY\). The exact polynomial identity
\[
 \mathcal P(Y,1-XY)
      =-Y^3\left[X^2Y-X-(1-X)^3\right]
 \tag{34}
\]
therefore identifies (31) with the exponentiated first stationary
equation under the change of variables
\[
 A=Y,\qquad r=1-XY,\qquad X=(1-r)/Y.
 \tag{35}
\]
The inverse requires \(Y\ne0\), as is already true for the
exponential variable. One rational parametrization of this curve is
\[
 A=\frac{(1-X)^3+X}{X^2},\qquad
 r=-\frac{(1-X)^3}{X},\qquad X\ne0.
 \tag{36}
\]
For the stationary interpretation one also excludes the factorial
zeros \(X=1\) and \(XY=1\). Exponentiating loses the logarithmic
branch condition: a solution of (33) alone need not satisfy the
chosen equation \(W_x=0\). The second stationary equation and the
boundary marking are also still required.

The discriminant of (31), taken in \(r\), is
\[
 \operatorname{disc}_r\mathcal P
     =A^6(4A^3-32A^2+48A-23).
 \tag{37}
\]
It does not vanish on \(|A|=1\). To see this without a numerical
root calculation, write \(A=e^{it}\) and \(c=\cos t\). The
imaginary part of the cubic factor is
\(4\sin t(4c^2-16c+11)\). At \(A=1,-1\), the factor is
respectively \(-3,-107\). Otherwise, vanishing of the imaginary
part gives \(4c^2-16c+11=0\), and substitution in the real part
reduces it to \(9-8c>0\). Thus the three characteristic roots are
distinct on that circle. At \(A=1\), one of them is zero; their
distinctness is not a uniform invertibility assertion for backward
transport near the terminal index.

There is also a modulus degeneracy even where all roots are distinct.
At \(A=-1\), (31) is
\(r^3-7r^2+13r-8\). Its discriminant is \(-107\), so it has
one real root \(R\) and a nonreal conjugate pair. Since its values
at \(4\) and \(5\) are \(-4\) and \(7\), respectively,
\(4<R<5\). The conjugate roots have modulus \(\sqrt{8/R}\),
which is smaller than \(R\). Thus two roots have equal smallest
modulus. Simplicity of the characteristic roots does not even provide
a unique mode of largest modulus for backward transport along the
entire unit circle.

Equations (25) and (34) give an exact finite recurrence whose
characteristic curve is the stationary curve of the original
source. They do not yet control cancellations in its selected
solution. In particular, distinct characteristic roots do not
remove the transport-norm problem exhibited by (23).

## 8. An algebraic curve for the derivative of the boundary action

The [complete mixed boundary theorem](research_mixed_two_crossing_boundary_theorem.md)
now proves a nonzero asymptotic \(Z_N(u)=A(u)e^{NS(u)}(1+O(N^{-1}))\)
for the original polynomial, on a fixed complex disk. Its selected
action is the stationary value of
\[
 W(x,y;u)=J(x+y)-3J(x)-2J(y)+b(y,u)
                      +i\pi(xy-y^2/2-y/2).
 \tag{38}
\]
Here \(b\) is the original Newton phase, and all logarithms have
the branches fixed in that theorem. Put
\[
 X=e^{2\pi ix(u)},\qquad Y=e^{2\pi iy(u)},\qquad w=e^{iu}.
 \tag{39}
\]
The exponentiated critical equations are
\[
 X^3+(Y-3)X^2+2X-1=0,\qquad
 (1-XY)(Y+w)(1+wY)=w(1-Y)^4.
 \tag{40}
\]
At \(u=0\), the selected \(X\) is the upper root of
\(X^3+2X^2+1=0\), and \(Y=1+2X+2X^2\).
Those data, together with the unexponentiated equations, select a
holomorphic branch of (40).

The envelope derivative is \(S'(u)=b_u(y(u),u)\). Integrating the
derivative of the Newton phase explicitly gives
\[
 b_u(y,u)=-\int_0^y
       \frac{\sin u}{\cos(2\pi t)+\cos u}\,dt
   =-\frac1{2\pi}\log\frac{Y+w}{1+wY}.
 \tag{41}
\]
For example, substitute \(Z=e^{2\pi it}\) and integrate the two
simple fractions with poles at \(-w,-w^{-1}\). The logarithm in
(41) is the one equal to zero at \(u=0\); its apparent special
case there is removable. Consequently
\[
                     P=e^{-2\pi S'(u)}
                        =\frac{Y+w}{1+wY}.             \tag{42}
\]
This is an identity of the selected holomorphic functions, with
the additive logarithmic constant fixed.

Eliminating \(X,Y\) in (40),(42) gives
\[
\begin{split}
 \mathcal Q(w,P)={}&
 w^2(w+1)^4P^5
 -4w^2(w+1)^2(3w+2)P^4\\
 &+4w^2(w^3+14w^2+17w+8)P^3\\
 &-4w(8w^3+17w^2+14w+1)P^2\\
 &+4w(w+1)^2(2w+3)P-(w+1)^4=0.
\end{split}
 \tag{43}
\]
The elimination itself uses only the source-action derivative.
Its original peripheral interpretation is now proved by the
marked collar construction described below.

The discarded resultant factors can be stated exactly. Define
\[
 f=X^3+(Y-3)X^2+2X-1,\qquad
 g=(1-XY)(Y+w)(1+wY)-w(1-Y)^4,
\]
and let
\[
 R(Y,w)=-\frac{\operatorname{Res}_X(f,g)}{Y^3(Y-1)^3}.
 \tag{44}
\]
The quotient in (44) is a polynomial, and
\[
 \operatorname{Res}_Y\bigl(R(Y,w),P(1+wY)-(Y+w)\bigr)
                   =-(w+1)^5\mathcal Q(w,P).
 \tag{45}
\]
At the selected complete point, \(Y\ne0,1\), \(w+1\ne0\), and
\((Y+w)(1+wY)\ne0\). Thus none of these factors vanishes on a
sufficiently small neighborhood of that branch. They have not
been suppressed in a global statement about all characters.

The polynomial by itself still does not select that branch. Indeed
\(\mathcal Q(1,P)=16(P-1)^5\). If
\(w=1+t\) and \(P=1+ct+O(t^2)\), its first nonzero homogeneous
term has coefficient
\[
              (4c^2+2c+1)(4c^3+6c^2+5c+2).
 \tag{46}
\]
The selected tangent satisfies the cubic factor and is explicitly
\[
 c=\frac{1-Y(0)}{1+Y(0)}=2\pi i S''(0).
 \tag{47}
\]
The source normalization and its selected critical point therefore
carry information that (43) alone omits.

The [original collar representation proof](research_mixed_word_collar_representation.md)
identifies the primitive periods, with the retained positive
carrier, as
\[
 U=-2\pi S'(u)-iu,\qquad V=2iu
 \tag{48}
\]
on the actual geometric germ of the two-cusped augmented
complement, with its main meridian parabolic. If
\(m=e^U\) and \(\ell=e^V\) are the meridian and longitude
similarity multipliers, then
\[
                m=P/w,\qquad \ell=w^2,\qquad
                \mathcal Q(w,wm)=0.                 \tag{49}
\]
Similarity multipliers are squares of the corresponding selected
eigenvalues; \(w=e^{V/2}\) retains its chosen branch.
This is a curve for the constrained augmented-link germ.
It is not a claim that (43) is a globally minimal A-polynomial
of a closed knot.

For a fixed odd final power \(c\), set \(p=(1-c)/2\).
The original primitive filling condition is
\(U+pV=-2\pi i\). Its exponential gives
\[
                       P=w^c,\qquad
                       \mathcal Q(w,w^c)=0.          \tag{50}
\]
The actual point is selected by the original logarithmic
equation and its cone path from charge zero to charge one.
In particular \(w=1\) is always a root of the algebraic
equation (50), but it is the unfilled zero-charge point,
not the selected filled saddle.

For every sufficiently large fixed odd \(|c|\), that marked
geometric proof and the original full-source closing theorem
give
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K_c\rangle_N|
 =2\pi\Re\left[S(u_c)+\frac{ic}{4\pi}u_c^2-iu_c\right]
 =\operatorname{Vol}(S^3\setminus K_c),               \tag{51}
\]
where \(u_c\) is the selected logarithmic solution of (50).
An arbitrary algebraic point of the same polynomial has
not been assigned this asymptotic or volume.

## 9. Reproducing the algebraic checks

The accompanying program compares the original crossing matrices
with (7), verifies the forced recurrence and inverse operator, checks
(25) and its terminal reconstruction, and checks (34), (37), the
resultant factors (44)–(45), and the tangent factorization (46)–(47)
by exact symbolic arithmetic. The numerical comparisons use both
parities at levels \(2\le N\le12\). The later growth records
illustrate the proved rates (20) and (23); they are not evidence for
an unproved boundary asymptotic.

Run the [verification script](../experiments/check_mixed_pair_fourier_transport.py)
with the command below. Its saved output is
[research-mixed-pair-fourier-transport.json](../repro/results/research-mixed-pair-fourier-transport.json).

```sh
python3 experiments/check_mixed_pair_fourier_transport.py --precision 120 --output repro/results/research-mixed-pair-fourier-transport.json
```
