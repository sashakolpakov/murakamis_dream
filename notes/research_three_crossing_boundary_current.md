# The full three-crossing boundary kernel and its endpoint current

Research note, 3 November 2026.

The actual three-crossing column admits a two-state polynomial
insertion calculus. Its second state is the original one-crossing
column. After the next three-crossing turn, that current becomes a
two-crossing terminal, and one further bidiagonal operation reduces
it to a single prescribed endpoint. This gives an invertible
six-diagonal equation for the entire pendant source with powers
\((3,3)\), and by conjugation for \((-3,-3)\). A banded determinant
below retains its ordinary free-boundary polynomial, including
first normals.

These are exact source identities. They do not bound the inverse
or prove a boundary asymptotic. In particular the current in the
full kernel formula is retained, rather than estimated from the
uninserted three-crossing column.

## 1. Original matrices and the two-state module

Fix \(N\ge2\), \(D=N-1\), and
\[
 q=e^{\pi i/N},\qquad Q=q^2,\qquad
 \eta=(-1)^D,\qquad \kappa=\exp(\pi iD^2/(2N)).
 \tag{1}
\]
Put
\[
 \begin{split}
 c_j&=qQ^j+q^{-1}Q^{-j},&
 d_j&=2-Q^j-Q^{-j},\\
 S_j&=\prod_{r=1}^j2\sin(\pi r/N),&
 e_j(z)&=S_j^{-2}\prod_{r=0}^{j-1}(c_r-z),\\
 P_N(z)&=2T_N(z/2)+2.&
 \end{split}                                                    \tag{2}
\]
Empty products are one. The original multiplication matrix is
\((Cf)_j=c_jf_j-d_jf_{j-1}\), with the missing row-zero term
equal to zero. Write \(Jf_j=f_{D-j}\), \(L=JCJ=C^T\), and
\(\mathsf X=\operatorname{diag}(Q^j)\).
The crossing matrix \(M\) includes its original scalar \(\kappa\).

Let
\[
 \alpha=M^3\mathbf e_0,\qquad
 \alpha_1=M\mathbf e_0,\qquad b=\kappa^2q^{-1}.
 \tag{3}
\]
The exact [three-crossing source equation](research_three_crossing_full_coefficient_profile.md),
equation (6a), is
\[
 (C-q\mathsf X)\alpha=b\alpha_1,\qquad
 (\alpha_1)_j=\kappa(-q)^j .
 \tag{4}
\]
In particular it includes the first and last color rows.

For a scalar polynomial \(F(X)\), let
\(\mathcal SF(X)=F(Q^{-1}X)\), and define
\[
 \begin{split}
 \mathcal D_3F
   &=qXF+q^{-1}X^{-1}(F-\mathcal SF),\\
 \mathcal D_1F
   &=(qX+q^{-1}X^{-1})F+
               q^{-1}(2-X-X^{-1})\mathcal SF .
 \end{split}                                                    \tag{5}
\]
Both expressions are polynomials: the apparent negative power
multiplies \(F-\mathcal SF\). Their degree increases by at most
one.

**Theorem 1.** At every level, with no restriction on polynomial
degree,
\[
 \begin{split}
 C\{F(\mathsf X)\alpha\}
   &=(\mathcal D_3F)(\mathsf X)\alpha
                          +b(\mathcal SF)(\mathsf X)\alpha_1,\\
 C\{G(\mathsf X)\alpha_1\}
   &=(\mathcal D_1G)(\mathsf X)\alpha_1 .
 \end{split}                                                    \tag{6}
\]
Thus arbitrary insertions are represented by the ordered module
\[
 \begin{pmatrix}\mathcal D_3&0\\ b\mathcal S&\mathcal D_1\end{pmatrix},
 \qquad
 (F,G)\longmapsto F(\mathsf X)\alpha+G(\mathsf X)\alpha_1 .
 \tag{7}
\]

*Proof.* In row \(j>0\), use (4) to eliminate
\(d_j\alpha_{j-1}\). The coefficient of \(\alpha_j\) is
\(c_jF(Q^j)-q^{-1}Q^{-j}F(Q^{j-1})\), which is
\(\mathcal D_3F\). The remaining term is
\(bF(Q^{j-1})(\alpha_1)_j\).
At row zero, \(\alpha_0=\kappa^3\),
\((\alpha_1)_0=\kappa\), and \(b\kappa=q^{-1}\kappa^3\);
the two values involving \(F(Q^{-1})\) cancel exactly.
For the second identity use
\((\alpha_1)_{j-1}=-q^{-1}(\alpha_1)_j\).
Its row-zero shifted term has coefficient \(d_0=0\).
This proves (6) without a fictitious wrap row. Iteration proves
(7). \(\square\)

Define polynomials \(h_\ell,r_\ell\), for \(0\le\ell\le D\), by
\[
 \begin{split}
 h_0&=1,\qquad r_0=0,\\
 d_{\ell+1}h_{\ell+1}&=(c_\ell-\mathcal D_3)h_\ell,\\
 d_{\ell+1}r_{\ell+1}
       &=(c_\ell-\mathcal D_1)r_\ell-\mathcal S h_\ell
                                      \quad(0\le\ell<D).
 \end{split}                                                    \tag{8}
\]
The denominators in this recursion are nonzero.
Then \(\deg h_\ell=\ell\), with leading coefficient
\((-q)^\ell/S_\ell^2\), and \(\deg r_\ell\le\ell-1\).
Theorem 1 gives the exact full-vector identity
\[
 e_\ell(C)\alpha
   =h_\ell(\mathsf X)\alpha+b\,r_\ell(\mathsf X)\alpha_1.
 \tag{9}
\]
In particular no boundary rows are omitted when \(\ell\) is
comparable to \(N\).

## 2. The entire original boundary kernel

Let
\[
 \begin{split}
 K_N(z,w)&=\sum_{\ell=0}^D e_\ell(z)e_\ell(w),\\
 \mathcal H_N(X,w)&=\sum_{\ell=0}^D e_\ell(w)h_\ell(X),\\
 \mathcal R_N(X,w)&=\sum_{\ell=0}^D e_\ell(w)r_\ell(X).
 \end{split}                                                    \tag{10}
\]
Summing (9) gives an ordinary polynomial identity in the free
variable \(w\):
\[
 \boxed{\quad
 K_N(C,w)\alpha
 =\mathcal H_N(\mathsf X,w)\alpha
                    +b\,\mathcal R_N(\mathsf X,w)\alpha_1 .
 \quad}                                                         \tag{11}
\]
Every degree \(0\le\ell<N\) is present.
An arbitrary left row, including a row with additional free
variables, may be applied to (11).

For example put
\[
 f=JM^3JM^3\mathbf e_0=(M^3)^TM^3\mathbf e_0,\qquad
 F_N(w)=\sum_{j=0}^D f_j e_j(w).
 \tag{12}
\]
This is the original pendant with both powers \(+3\).
Since \(M^3e_\ell(C)\mathbf e_0=e_\ell(C)\alpha\), its full
boundary polynomial is
\[
 \begin{split}
 F_N(w)&=\alpha^T K_N(C,w)\alpha\\
 &=\sum_{j=0}^D\alpha_j^2\mathcal H_N(Q^j,w)
       +b\sum_{j=0}^D\alpha_j(\alpha_1)_j
                                      \mathcal R_N(Q^j,w).
 \end{split}                                                    \tag{13}
\]
The transpose in (13) is not a Hermitian adjoint.
The negative pendant is
\(F_{-,N}(w)=\overline{F_N(\overline w)}\).
The same signed convention applies to every identity below by
conjugating \(q,Q,\kappa\) and the coefficients.
This does not conjugate an independent boundary variable.

There is a useful exact top-degree calibration for the first
kernel in (10). Let \(H_m\) be the monic continuous
\(Q^{-1}\)-Hermite polynomial:
\[
 H_0=1,\quad H_1=z,\quad
 H_{m+1}=zH_m-(1-Q^{-m})H_{m-1}.
 \tag{14}
\]
Its classical identification is
[DLMF 18.28.16](https://dlmf.nist.gov/18.28.E16), with
the argument scaled by \(1/2\). The following specialization is
a polynomial calculation, not a singular hypergeometric
substitution. Directly from
\[
 \mathcal D_3X^m=qX^{m+1}
                    +q^{-1}(1-Q^{-m})X^{m-1}
 \tag{15}
\]
one obtains \(H_m(\mathcal D_3)1=q^mX^m\).
The Gaussian-binomial formula for (14), itself verified by its
recursion, gives \(H_N(t+t^{-1})=t^N+t^{-N}\): all interior
Gaussian binomials vanish at primitive \(Q^{-1}\), and their
denominators have indices less than \(N\). Consequently
\[
 H_N(z)=2T_N(z/2),\qquad
                 P_N(\mathcal D_3)1=2-X^N .
 \tag{16}
\]
In particular the central forcing is not zero.

Set
\(\mathcal I_N(X,w)=\sum_{\ell=0}^D e_\ell(w)h_{D-\ell}(X)\).
With \(\mathcal L_w\) the original finite operator \(L\) on
canonical degree-\(<N\) boundary polynomials, one has
\[
 \boxed{\begin{split}
 (w-\mathcal D_3)\mathcal I_N
                &=\frac{\eta}{N^2}\{P_N(w)+X^N-2\},\\
 (\mathcal L_w-\mathcal D_3)\mathcal H_N
                &=\frac{\eta}{N^2}(X^N-2)e_D(w).
 \end{split}}                                                   \tag{17}
\]
These are ordinary identities, before specializing \(X^N=1\)
or reducing the free variable modulo \(P_N\).
To prove them, telescope (8) against
\(we_\ell=c_\ell e_\ell-d_{\ell+1}e_{\ell+1}\) below the
top degree. At the top use
\[
 (w-c_0)e_D(w)=\eta P_N(w)/N^2,\qquad
 (\mathcal D_3-c_0)h_D=\eta(2-X^N)/N^2.
 \tag{18}
\]
The reversed-index identities
\(c_{D-\ell}=c_\ell\), \(d_{D-\ell+1}=d_\ell\)
give the first line. The formula
\(\mathcal L_we_\ell=c_\ell e_\ell-d_\ell e_{\ell-1}\)
gives the second. This also explains why dropping the top
factorial degree would change the free-boundary equation.

### The two spectra and the retained current

The first component of (7) is not itself a representation of the
original boundary algebra. This can be seen exactly at every level.
Let \(V_N=\mathbb C[X]/(X^N-1)\), identified with functions on the
physical clocks \(Q^j\). The operators in (5) act on \(V_N\).
They satisfy
\[
 P_N(\mathcal D_3)=I,\qquad P_N(\mathcal D_1)=0.
 \tag{18a}
\]
Indeed \(1,\mathcal D_3 1,\ldots,\mathcal D_3^{N-1}1\) form
a basis, by their distinct degrees and nonzero leading coefficients.
Equation (16), reduced modulo \(X^N-1\), gives the first identity
on \(1\); commuting with \(\mathcal D_3\) proves it on this basis.
For the second identity, the second line of (6) identifies
\(\mathcal D_1\) with \(C\) conjugated by the invertible diagonal
matrix whose entries are \((\alpha_1)_j\).

Consequently \(\mathcal D_3\) has characteristic polynomial
\(P_N(z)-1=2T_N(z/2)+1\). Its \(N\) roots are simple and real:
they are \(z=2\cos\theta\), \(0<\theta<\pi\), with
\(\cos(N\theta)=-1/2\). They are disjoint from the original
spectrum \(P_N(z)=0\). This spectral displacement does not imply
a norm estimate for either change of basis.

Write \(\mathcal T\) for the block operator in (7) on
\(V_N\oplus V_N\), and write \(\mathrm{ev}\) for its source
evaluation in that equation. Then
\[
 P_N(\mathcal T)^2=P_N(\mathcal T),\qquad
 \operatorname{im} P_N(\mathcal T)=\ker\mathrm{ev}.
 \tag{18b}
\]
To prove this, polynomial evaluation in the lower triangular block
matrix gives \(P_N(\mathcal T)=
\left(\begin{smallmatrix}I&0\\Y&0\end{smallmatrix}\right)\)
for some \(Y\). This is a rank-\(N\) projector. Theorem 1 gives
\(\mathrm{ev}\,P_N(\mathcal T)=P_N(C)\mathrm{ev}=0\).
Since \(\alpha_1\) never vanishes, \(\mathrm{ev}\) is onto,
and its kernel also has dimension \(N\). This proves (18b).

There is an explicit form of the splitting. Let \(A_\alpha\)
be multiplication on the clock values by
\(\alpha_j/(\alpha_1)_j\). Equation (6) gives
\[
 \mathcal D_1 A_\alpha-A_\alpha\mathcal D_3=b\mathcal S,
 \qquad
 \mathcal T=
 \begin{pmatrix}I&0\\-A_\alpha&I\end{pmatrix}
 \begin{pmatrix}\mathcal D_3&0\\0&\mathcal D_1\end{pmatrix}
 \begin{pmatrix}I&0\\A_\alpha&I\end{pmatrix}.
 \tag{18c}
\]
In particular the displaced-spectrum subspace consists of pairs
\((F,-A_\alpha F)\), all of which evaluate to zero in the original
source. The second state in (11) therefore cannot be omitted on the
grounds that the first state has an explicit spectral curve. It
retains the part of the polynomial calculus which survives source
evaluation. Equations (18a)--(18c) make no assertion that either
summand in (13) is asymptotically small.

## 3. A single endpoint current for the adjacent pair

Use the upper bidiagonal coordinate from the
[primitive quantum cap](research_quantum_cap_primitive_source.md):
\[
 B_{jj}=-qQ^j,\qquad B_{j,j+1}=1-Q^{j+1}.
 \tag{19}
\]
All other entries vanish. It is invertible and \(\det B=1\).
Let \(L_1=M^{-1}LM\), whose original entries are
\[
 (L_1)_{jj}=4qQ^j-q(1+Q)Q^{2j},\qquad
 (L_1)_{j,j+1}=(L_1)_{j+1,j}=-(1-Q^{j+1})^2 .
 \tag{20}
\]
Define the following fixed-band matrices directly from
\(C,L,L_1,B\):
\[
 \begin{split}
 A_3&=q^{-2}(L^2-I)L_1+q^{-3}LC-8q^{-2}L+8q^{-1}I,\\
 \mathcal A_N&=B(A_3-L)-I,\qquad
 \zeta_N=\eta\kappa^2q^{-1}.
 \end{split}                                                    \tag{21}
\]

**Theorem 2.** The complete original vector in (12) is the unique
solution of
\[
 \boxed{\qquad \mathcal A_N f=\zeta_N\mathbf e_D,\qquad
                 \det\mathcal A_N=-\eta .\qquad}                 \tag{22}
\]
The matrix has lower bandwidth one and upper bandwidth at most
four. Its two outer diagonals are
\[
 \begin{split}
 (\mathcal A_N)_{j,j-1}&=-q\,d_jQ^{4j}
                                            &&(1\le j<N),\\
 (\mathcal A_N)_{j,j+4}
    &=-q^{-2}(1-Q^{j+1})d_{j+2}d_{j+3}(1-Q^{j+4})^2
                                            &&(j+4<N).
 \end{split}                                                    \tag{23}
\]
Thus both are nonzero wherever they exist. The construction
also applies unchanged at \(N=2,3,4\), with the absent diagonals
simply omitted.

*Proof.* Put \(S=JM^3J\), so \(f=S\alpha\). Write
\(L_n=M^{-n}LM^n\).
The exact original trace recursion
\[
 L_{n+1}+qCL_n+q^2L_{n-1}=8qI,\qquad JL_{-1}J=L_1
 \tag{24}
\]
gives \(SCS^{-1}=JL_{-3}J=A_3\).
For the clock, the exact primitive-coordinate substitutions are
\[
 \operatorname{Ad}_M X=-q^{-1}K^{-1},\qquad
 \operatorname{Ad}_M K=qX-C,\qquad JKJ=B.
 \tag{25}
\]
Therefore
\(\operatorname{Ad}_{M^2}K=-K^{-1}-C\) and
\(\operatorname{Ad}_{M^3}X^{-1}=q(K^{-1}+C)\).
Since \(JXJ=Q^{-1}X^{-1}\), these yield
\[
                         SXS^{-1}=q^{-1}(B^{-1}+L).
 \tag{26}
\]
Conjugate (4) by \(S\). The original cap identity
\(JM\mathbf e_0=M^{-1}\mathbf e_0\) gives
\[
 S\alpha_1=JM^2\mathbf e_0=:H_2.
 \tag{27}
\]
The retained terminal endpoint equation is
\(BH_2=\eta\mathbf e_D\).
Thus multiplication on the left by \(B\) gives (22), with
the stated scalar, rather than a homogeneous equation.

Moreover
\(\mathcal A_N=BS(C-qX)S^{-1}\).
The last factor is lower triangular with diagonal
\(q^{-1}Q^{-j}\). Hence
\(\det\mathcal A_N=q^{-N}\det X^{-1}=-\eta\).
This proves uniqueness without dividing by a source coefficient.
The bandwidth follows from (20)--(21).
For its lower diagonal, direct substitution gives
\((A_3)_{j,j-1}=d_jQ^{3j}\), using
\((1-Q^j)^2=-Q^jd_j\); multiplication by \(B_{jj}\)
proves the first line of (23).
Only the term \(q^{-2}BL^2L_1\) contributes to the last
upper diagonal, giving its second line. \(\square\)

Every entry of (21) is bounded by an absolute constant on the
physical clocks, independently of \(N\). For example,
\(\|C\|_\infty,\|L\|_\infty\le6\),
\(\|L_1\|_\infty\le14\), and \(\|B\|_\infty\le3\).
The determinant in (22) does not give a bound on the inverse.

## 4. The ordinary boundary polynomial as a banded determinant

For an \(N\times N\) matrix \(Y\), write \(Y^{[D]}\) for its
leading \(D\times D\) principal submatrix; the empty determinant
convention is not needed since \(N\ge2\).

**Corollary 3.** The entire polynomial (12) is
\[
 \boxed{\quad
 F_N(w)=-\frac{\eta\kappa^2}{qN^2}
        \det\!\left([\mathcal A_N(wI-C)]^{[D]}\right).
 \quad}                                                         \tag{28}
\]
The determinant core has lower bandwidth at most two and upper
bandwidth at most four. Its entries are affine in the actual
free variable \(w\).
Equation (28) is valid at the repeated physical roots as an
ordinary polynomial identity; it retains their first normals.
Both signs are obtained by the conjugation specified after (13).

*Proof.* For \(v(w)=(e_0(w),\ldots,e_D(w))^T\), the original
Newton recurrence, including its last row, gives
\[
 v(w)^T(wI-C)=\eta P_N(w)\mathbf e_D^T/N^2.
 \tag{29}
\]
For \(P_N(w)\ne0\), equations (22) and (29) imply
\[
 F_N(w)=\frac{\eta\zeta_N P_N(w)}{N^2}\,
         \mathbf e_D^T[\mathcal A_N(wI-C)]^{-1}\mathbf e_D .
 \tag{30}
\]
The indicated inverse entry is the principal cofactor divided by
\(\det\mathcal A_N\,\det(wI-C)=-\eta P_N(w)\).
This proves (28) off the spectrum; cancellation and polynomial
continuation prove it at every \(w\). In particular no derivative
of \(P_N\) was discarded. \(\square\)

There is also a simple scalar continuant for the original closing
coefficient. Put \(\Delta_0=1\) and
\(\Delta_n=\det\mathcal A_N^{[n]}\).
With \(\ell_j=(\mathcal A_N)_{j,j-1}\), the upper-Hessenberg
expansion gives, for \(1\le n\le N\),
\[
 \Delta_n=(\mathcal A_N)_{n-1,n-1}\Delta_{n-1}
  +\sum_{r=1}^{\min(4,n-1)}(-1)^r
    (\mathcal A_N)_{n-1-r,n-1}
    \left(\prod_{j=n-r}^{n-1}\ell_j\right)\Delta_{n-r-1}.
 \tag{31}
\]
Indeed the entry in row \(n-1-r\) of the last column forces
the consecutive \(r\) subdiagonal entries in its determinant
cycle. The remaining permutation is the leading principal
determinant in (31).
The full normalization is
\[
 \Delta_N=-\eta,\qquad
 \phi_N(F_N)=f_D=-\kappa^2q^{-1}\Delta_D.
 \tag{32}
\]
Equation (31) alone computes this closing coefficient, not the
free-boundary polynomial. The latter is (28). Equivalently, for
\(N\ge5\), the nonzero upper diagonal in (23) makes the first
\(N-4\) rows of (22) a forward recurrence determining the vector
from its first four entries, with the left endpoint row retained.
The interior stencil has order five, with indices \(j-1\)
through \(j+4\). The last four rows are its actual endpoint
conditions. Their solution is unique by (22).

## 5. Frozen symbol in the original rational chart

There is a concrete classical curve associated with (22), without
selecting a determinant asymptotic. Let \(X,E\) be nonzero commuting
variables, with \(E\) corresponding to the coefficient shift
\(f_j\mapsto f_{j-1}\). The frozen \(q\to1\) symbols of the actual
entries above are
\[
 \begin{split}
 d&=2-X-X^{-1},\\
 C&=X+X^{-1}-dE,& L&=X+X^{-1}-dE^{-1},\\
 B&=-X+(1-X)E^{-1},&
 L_1&=4X-2X^2-(1-X)^2(E+E^{-1}).
 \end{split}                                                    \tag{33}
\]
In particular \(L_1\) uses the convention \(M^{-1}LM\), not
the opposite crossing conjugation.
The two determinant symbols are respectively
\[
 \begin{split}
 a(X,E)&=B\{(L^2-1)L_1+LC-9L+8\}-1,\\
 p_w(X,E)&=a(X,E)(w-C).
 \end{split}                                                    \tag{34}
\]
The coefficient of \(E\) in \(a\) is
\(X^3(X-1)^2=-dX^4\), agreeing with the exact subdiagonal (23).
The coefficient of \(E^{-4}\) is \((X-1)^7/X^2\).

The cap part \(a=0\) is the literal rational transport of
the base three-crossing curve \(C-X=0\).
To make the claim precise, work on the common open chart where
the following birational maps and their inverses are defined.
Use \(K=-X^{-1}+(1-X^{-1})E\); then
\[
 \begin{split}
 C&=X+1+(X-1)K,\\
 \mathfrak m^{-1}(X,K)&=(X+XK+1,-X^{-1}),\\
 \mathfrak j(X,E)&=(X^{-1},E^{-1}).
 \end{split}                                                    \tag{35}
\]
These are the \(q=1\) limits of the exact inverse crossing and
turn substitutions, retaining their original coordinate order.
The classical conjugation \(\Phi_S\), \(S=JM^3J\), obeys
\[
 \Phi_S C=(L^2-1)L_1+LC-8L+8,\qquad
 \Phi_S X=L+B^{-1},\qquad
                  a=B\,\Phi_S(C-X).
 \tag{36}
\]
Thus apply the inverse chart map of \(S\) to the base curve
\[
             X=t,\qquad K=-1/(t-1),\qquad E=-1/(t-1)^2.
 \tag{37}
\]
Writing
\[
 z(t)=4-5t+4t^2-t^3,\qquad r(t)=t^2-3t+3,
 \tag{38}
\]
the result is the explicit parameterization
\[
 \boxed{\qquad
 X=\frac{r(t)}{z(t)r(t)-1},\qquad
 E=-\frac{(t-2)^3(t^2-2t+2)^2}{(t-1)^2}.
 \qquad}                                                        \tag{39}
\]
Indeed, after the initial turn the clock is \(x_0=1/t\),
and the Casimir held fixed by the next three inverse crossings
is \(z(t)\). Their successive clocks are
\[
 x_1=r(t),\qquad x_2=z(t)-t,\qquad
 x_3=z(t)-1/r(t).
 \tag{40}
\]
The final turn gives \(X=1/x_3\) and
\(E=x_2(x_3-1)/(x_2-x_3)\). Factoring this expression gives
(39). This proves \(a(X(t),E(t))=0\) on the common chart by
the original substitutions, rather than by guessing a root
of the degree-five Laurent equation.

Substitution also gives
\[
 \begin{split}
 L(t)&=z(t),&
 B(t)&=\frac1{(t-2)(t^2-2t+2)},\\
 C(t)&=2+v(t)^2,&
 v(t)&=(t-2)^2(t^2-2t+2).
 \end{split}                                                    \tag{41}
\]
Consequently the intersections with the ordinary free-boundary
factor \(w-C\), when \(w=-2\cos u\), are exactly
\[
                    v(t)=\pm2i\cos(u/2)
 \tag{42}
\]
within this chart. These quartics give possible classical
intersection points. The identities do not choose a geometric
branch or prove that its cycle has nonzero coefficient in the
original determinant.

## 6. Analytic scope

The two-state kernel formula (11) and the forced banded equation
(22) are two forms of the same retained original current.
They supply a prepared-source boundary problem for the short
adjacent pair, with a source scalar and all endpoint rows fixed.
They do not assert that its determinant or inverse is positive,
or that the second term in (13) has a smaller exponential rate.
The uninserted high-color approximation in the three-crossing
profile cannot by itself estimate that term when all
\(\ell<N\) are present.

The new question is quantitative control of (28), or of the
two explicit terms in (13), on a fixed complex boundary disk.
Until such control is proved, these identities do not yield
the \((-3,-3)\) boundary packet or a new volume-conjecture
consequence.

## 7. Reproduction

The focused checker is
[check_three_crossing_boundary_current.py](../experiments/check_three_crossing_boundary_current.py).
It builds the original crossing matrix independently from its
sine-factorial coefficients and builds (21) directly from the
banded entries. The
[120-digit result](../repro/results/research-three-crossing-boundary-current.json)
covers \(N=2,\ldots,10\), both signs, and all Newton insertion
degrees. Its 1,508 numerical identities include the full kernel,
the endpoint current, the conjugated clock, both outer diagonals,
all leading continuants, and the ordinary boundary determinant
and its first derivative at every physical root and a nonreal
point. The maximum relative residual is less than
\(4.26\cdot10^{-114}\).

The same checker verifies six frozen-symbol and chart identities
by exact rational simplification. Neither part tests or asserts
an asymptotic source contribution. The record contains the script
hash and the arithmetic-library versions. To reproduce it:

    python experiments/check_three_crossing_boundary_current.py --precision 120

A [separate 140-digit replay](../repro/results/research-three-crossing-boundary-current-review.json)
passed the same identities with maximum relative residual less than
\(4.60\cdot10^{-133}\). The determinant routine uses explicit
row-pivot elimination and permits singular derivative cofactors;
such a cofactor is not an invertibility assumption in the proof.

