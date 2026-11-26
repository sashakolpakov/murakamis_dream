# A polynomial bound for one full microscopic endpoint under a unit turn

Private written proof, 16 November 2026.

The original signed unit-leaf operator sends one full microscopic
endpoint kernel to a polynomially bounded ordinary representative
on the entire real spectral interval. The proof uses its exact
forced Askey--Wilson equation and retains the complete first
spectral normals. It does not bound that operator on arbitrary
polynomials or on products of endpoint kernels.

## 1. Statement and original normalization

Put
\[
 N\ge2,\quad D=N-1,\quad \theta=\pi/N,\quad
 q=e^{i\theta},\quad \eta=(-1)^D,\quad \kappa=q^{D^2/2},
\]
\[
 s_j=2\sin(j\theta),\quad S_j=\prod_{\ell=1}^j s_\ell,\quad
 c_j=2\cos((2j+1)\theta),
\]
\[
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),\quad
 P_N(Z)=2T_N(Z/2)+2,\quad
 K_N(w,Z)=\sum_{j=0}^D e_j(w)e_j(Z).
 \tag{1}
\]
The algebra is \(\mathcal A_N=\mathbb C[Z]/(P_N)\), with its
original Frobenius functional, physical turn, and crossing:
\[
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\qquad Te_j=e_{D-j},\qquad
 U_\sigma=\kappa^\sigma T R^{-\sigma}T,\quad \sigma=\pm1.
 \tag{2}
\]
Products in this algebra are represented by their ordinary
remainders of degree at most \(D\), denoted \(\operatorname{can}\).
This convention is essential at an ordinary free endpoint.

For \(A<\infty\), define
\[
 w_N(\alpha)=2\cosh(\alpha/N),\qquad
 F_{N,\sigma,\alpha}(Z)
       =(U_\sigma^{(Z)}K_N)(w_N(\alpha),Z),\qquad |\alpha|\le A.
 \tag{3}
\]
Here \(\alpha\) may be complex.

**Theorem 1.** There are finite constants \(C_A,p_A\), independent
of \(N,\sigma,\alpha\), such that
\[
 \boxed{\quad
 \sup_{Z\in[-2,2]}|F_{N,\sigma,\alpha}(Z)|\le C_A N^{p_A}.
 \quad}                                                     \tag{4}
\]
For every fixed pair of nonnegative integers \(a,b\), the same
conclusion holds for
\(\partial_\alpha^a\partial_Z^bF\), with a possibly larger
constant and power. In particular every physical value and
every first spectral normal is retained, at both parities.

The powers in (4) are deliberately not optimized. They may depend
on the fixed parameter bound \(A\). No assertion concerns a
parameter bound growing with \(N\).

## 2. Stable full-Hermite interpolation and the two initial jets

For an ordinary polynomial \(p\) of degree at most \(D\), write
\[
 p(-2\cos t)=\sum_{|m|\le D}b_m e^{imt},\qquad b_{-m}=b_m,
 \qquad \tau_j=(D-2j)\pi/N,\quad 0\le j<N.
 \tag{5}
\]
Then \(-2\cos\tau_j=c_j\) and \(e^{iN\tau_j}=\eta\).
Let \(v_j=p(c_j)\) and
\(d_j=\partial_t[p(-2\cos t)]_{t=\tau_j}\), and set
\[
 V_m=N^{-1}\sum_jv_j e^{-im\tau_j},\qquad
 W_m=N^{-1}\sum_j(d_j/i)e^{-im\tau_j}.
\]
The finite Fourier orthogonality gives, for \(1\le m<N\),
\[
 V_m=b_m+\eta b_{m-N},\qquad
 W_m=m b_m+(m-N)\eta b_{m-N},
\]
\[
 b_m=\frac{W_m+(N-m)V_m}{N},\qquad b_0=V_0.
 \tag{6}
\]
Consequently the canonical full-Hermite polynomial determined by
compatible data obeys
\[
 \sum_{|m|\le D}|b_m|
 \le (2N-1)\max_j|v_j|+2\max_j|d_j|.
 \tag{7}
\]
Compatibility means the values agree at the paired angular lifts
and the angular derivatives have opposite signs. The odd simple
node has \(t=0\) and derivative zero by evenness; no spectral
normal is imposed there. Thus (6)--(7) apply at every level,
including \(N=2\).

If \(p\) is this representative, then
\[
 |p(w_N(\alpha))|\le e^A\sum_{|m|\le D}|b_m|.
 \tag{8}
\]
Indeed \(w_N(\alpha)=-2\cos(\pi+i\alpha/N)\), and
\(|e^{im(\pi+i\alpha/N)}|\le e^A\).

The original crossing satisfies
\[
 |R^\sigma(c_j)|=1,\qquad
 \left|\partial_t R^\sigma(-2\cos t)|_{\tau_j}\right|
       \le N/2.
 \tag{9}
\]
These are the original Gaussian values and first normals, not
values of a chosen off-spectrum exponential. Equivalently, at
a double root,
\[
 (R^\sigma)'(c_j)/R^\sigma(c_j)
       =i\sigma\,\frac{N-2j-1}{4\sin((2j+1)\theta)}.
 \tag{10}
\]
The odd simple value also has modulus one.

Let
\[
 Q_N(Z)=\partial_wK_N(c_0,Z).
\]
The full normal source proves
\[
 \|Q_N\|_{[-2,2]}\le N^4/4.                                 \tag{11}
\]
Ordinary Markov on \([-2,2]\) therefore bounds \(Q_N'\) by
\(C N^6\), and the angular derivative of \(Q_N(-2\cos t)\)
by the same coarse power. Equations (7)--(10), applied to the
full data of the products, give
\[
 \|\operatorname{can}(R^{-\sigma})\|_{\mathrm{Fourier},1}
       \le C N,\qquad
 \|\operatorname{can}(R^{-\sigma}Q_N)\|_{\mathrm{Fourier},1}
       \le C N^6.
 \tag{12}
\]
Multiplication retains its actual product-rule normals.

The exact endpoint-side adapter is
\[
 F_{N,\sigma,\alpha}(Z)
  =\kappa^\sigma
   [\operatorname{can}_w(R(w)^{-\sigma}K_N(w,Z))]
                                      _{w=w_N(\alpha)}.
 \tag{13}
\]
Since \(K_N(c_0,w)=1\), differentiating this finite polynomial
identity in \(Z\) gives both anchors:
\[
 |F(c_0)|\le C_A N,\qquad |F'(c_0)|\le C_A N^6.
 \tag{14}
\]
The second anchor uses (11); it is not inferred from the first
anchor or from a value-only row recurrence.

## 3. The exact forced equation

Let \(C\) denote multiplication by \(Z\) and put \(J=TCT\).
Because crossing multiplication commutes with \(C\),
\[
                         J U_\sigma=U_\sigma J.              \tag{15}
\]
The exact ordinary reproducer
\[
 TK_N(w,\cdot)
     =\frac{P_N(Z)-P_N(w)}{\eta N^2(Z-w)}
\]
implies in the full algebra
\[
 (w-J)K_N(w,\cdot)=\eta P_N(w)e_D/N^2.
\]
Also \(U_\sigma e_D=\kappa^\sigma R^\sigma\), from
\(T(R^{-\sigma})=R^\sigma\). Hence
\[
 \boxed{\quad
 (w-J)F=\eta P_N(w)\kappa^\sigma R^\sigma/N^2.
 \quad}                                                     \tag{16}
\]
Every expression in (16) has its canonical ordinary
representative.

For the index variable \(r\), put
\[
 c(r)=2\cos((2r+1)\theta),\qquad
 A(r)=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 C(r)=\frac{s_r^4}{s_{2r}s_{2r+1}}.
 \tag{17}
\]
The removable values are \(C(0)=C'(0)=0\).
The original off-grid kernel difference identity identifies the
action of \(J\) on every canonical polynomial:
\[
 (JF)(c(r))=(c_0+A(r)+C(r))F(c(r))
                   -A(r)F(c(r+1))-C(r)F(c(r-1)).
 \tag{18}
\]
One can check the identification on \(K_N(w,\cdot)\): its
coefficients \(e_j(w)\) span the polynomial space, and its exact
source is precisely the preceding reproducer equation.
Thus (16)--(18) are ordinary rational identities in \(r\), not
merely equations for the values.

Set \(J_N=\lfloor(N-1)/2\rfloor\). Only rows
\(0\le j<J_N\) will be used. They are all regular. At even
levels \(J_N\) is the last double root; at odd levels it is
the last distinct root, which is simple. We never use the
singular next row at even levels.

Write \(h_j=F(c_j)\), and in this range define
\[
 q_j=C(j)/A(j),\quad d_j=(c_0-w)/A(j),\quad
 f_j=\frac{\eta P_N(w)\kappa^\sigma R^\sigma(c_j)}
                                      {N^2 A(j)}.
 \tag{19}
\]
Equation (16) becomes exactly
\[
 h_{j+1}=(1+q_j+d_j)h_j-q_jh_{j-1}+f_j.                       \tag{20}
\]
At \(j=0\), the \(q_0h_{-1}\) term is absent.

## 4. Polynomial propagation through the entire value grid

For all regular positive rows,
\[
 q_j=
 \left(\frac{\sin(j\theta)}{\sin((j+1)\theta)}\right)^3
                  \frac{\cos((j+1)\theta)}{\cos(j\theta)}
                     \in(0,1),\qquad q_0=0.
 \tag{21}
\]
Both ratios are in \((0,1)\), since \((j+1)\theta<\pi/2\).
Also
\[
 A(j)\ge\frac{16}{\pi^2}\frac{(j+1)^2}{N^2}.
 \tag{22}
\]
Indeed \(s_{j+1}\ge4(j+1)/N\), whereas
\(s_{2j+1}s_{2j+2}\le16\pi^2(j+1)^2/N^2\).
For bounded complex \(\alpha\),
\[
 |c_0-w_N(\alpha)|\le C_A/N^2,\qquad
 P_N(w_N(\alpha))=2\cosh\alpha+2.
 \tag{23}
\]
Consequently
\[
             |d_j|+|f_j|\le C_A/(j+1)^2.                    \tag{24}
\]

For \(j\ge1\), balance the difference rather than diagonalizing
the transfer:
\[
 X_j=\binom{h_j}{(j+1)(h_j-h_{j-1})}.
\]
Writing \(r=j+1\), its exact step is
\[
 X_{j+1}=
 \begin{pmatrix}
  1+d_j&q_j/r\\
  (r+1)d_j&(1+1/r)q_j
 \end{pmatrix}X_j+\binom{f_j}{(r+1)f_j}.
 \tag{25}
\]
For the maximum row-sum norm, (21),(24) imply
\[
 \|M_j\|\le1+B_A/(j+1),\qquad
 \left\|\binom{f_j}{(j+2)f_j}\right\|
                           \le B_A/(j+1).                  \tag{26}
\]
Here \(B_A\) is a fixed finite constant. In particular every
forward product obeys
\[
 \|M_{k-1}\cdots M_j\|
 \le \exp\!\left(B_A\sum_{\ell=j}^{k-1}\frac1{\ell+1}\right)
 \le C_A N^{B_A}.                                          \tag{27}
\]
No lower bound on a transfer determinant or on \(h_j\) is used.

At the first row \(h_1=(1+d_0)h_0+f_0\). The anchor (14)
therefore bounds \(X_1\) polynomially. Variation of constants
in (25), with at most \(N\) terms and (27), proves
\[
                    \max_{0\le j\le J_N}|h_j|
                                      \le C_A N^{p_A^{(0)}}.
 \tag{28}
\]
For \(N=2\) there is only the anchor value. This also explains
why a coalescing final pair or the odd simple root causes no
instability: the proof reaches it from regular rows.

## 5. The original spectral normals

Use the index derivative
\[
 y_j=c'(j)F'(c_j),\qquad
 c'(j)=-4\theta\sin((2j+1)\theta).
 \tag{29}
\]
Differentiate the ordinary identity (20), with \(q,d,f\)
regarded as their functions of \(r\). At each regular row,
\[
 y_{j+1}=(1+q_j+d_j)y_j-q_jy_{j-1}+g_j,
\]
\[
       g_j=(q_j'+d_j')h_j-q_j'h_{j-1}+f_j'.                 \tag{30}
\]
Primes on these coefficients mean the index derivative, not
a spectral derivative. The source derivative in \(f_j'\)
is the derivative of the actual canonical \(R^\sigma(c(r))\).
By (9), \(|\partial_rR^\sigma(c(r))|_{r=j}\le\pi\).

All coefficient derivatives in (30) have a uniform polynomial
bound in \(N\). For clarity, a coarse bound sufficient here is
\[
                 |q_j'|+|d_j'|+|f_j'|\le C_A N^{10}.
 \tag{31}
\]
For \(j\ge1\), every nonzero sine in (17) is at least \(2/N\)
in absolute value. Differentiation costs at most a factor
\(C/N\) in each numerator or denominator sine; the quotient
rule, (22), and (23) therefore give (31).
At zero, remove \(C(0)\) first; \(C'(0)=q'(0)=0\), while
the other denominators are nonzero. The same bound holds.
This elementary estimate intentionally ignores cancellations.

The anchor \(y_0=c'(0)F'(c_0)\) is polynomial by (14).
The derivative of the first row gives
\[
                y_1=(1+d_0)y_0+d_0'h_0+f_0',
 \tag{32}
\]
since \(q_0=q_0'=0\). Thus \(y_1\) is polynomial also.
To propagate only the required double-root normals, use (30)
through the row preceding the last double root. Balancing
\((y_j,(j+1)(y_j-y_{j-1}))\) gives exactly the same matrices
\(M_j\) as in (25). The added vector is
\((g_j,(j+2)g_j)\), which is polynomial by (28),(31).
Forward variation of constants and (27) now give
\[
                   \max_{\text{double }c_j}|y_j|
                                       \le C_A N^{p_A^{(1)}}.
 \tag{33}
\]
There is no inverse fundamental-matrix estimate in this argument.
At a double root,
\[
                        |c'(j)|\ge8\pi/N^2.
 \tag{34}
\]
Therefore every \(F'(c_j)\) is polynomially bounded.
At the odd simple node its value was already included in (28);
no normal there is needed or supplied by this argument.
The lone \(N=2\) normal is the initial anchor itself.

Insert these values and normals into (7). This proves the real
interval bound (4). Markov supplies every fixed ordinary spectral
derivative. Finally \(F\) is entire in \(\alpha\); repeating (4)
on \(|\alpha|\le A+1\) and applying Cauchy's formula supplies every
fixed \(\alpha\)-derivative, jointly with the spectral derivatives.
This proves Theorem 1.

## 6. Exact source consequence and limits

For a leaf with original power \(\sigma=\pm1\) and precisely the
one full endpoint factor in (3), its original contraction is
\[
 \phi_N^{(Z)}
   [R^\sigma(Z)K_N(w_N(\alpha),Z)K_N(Z,X)]
           =T(R^\sigma K_{w_N(\alpha)})(X)
           =R^{-\sigma}(X)F_{N,\sigma,\alpha}(X)
                                                      \quad\text{in }\mathcal A_N.
 \tag{35}
\]
At a traced neighbor this changes its power by \(-\sigma\)
and inserts the polynomially bounded full coupon \(F\).
All its other factors and joint normal operations remain.
At a free neighbor the product on the right must first be
taken in its canonical ordinary representative.
The actual Gaussian physical jets and (7) show that this
representative is polynomially bounded too.

The argument establishes one such turn, including all physical
jets. It does not identify \(F\) with a product of microscopic
endpoint kernels, and gives no closure theorem for repeated turns
after branching. In particular it does not assert a polynomial
norm for \(U_\sigma\) on every polynomial with polynomial real
norm. A product input has a different forced equation; it is not
covered merely because each factor satisfies (16).
No scalar lower bound, filled-action estimate, or whole-current
gap follows from (4).

The archived exact unit-turn note already gives the full
triangular matrix, finite hypergeometric sums, and adapter (13).
The archived all-color normal theorem supplies the original
difference equation and the nontrivial endpoint normal bound (11).
The added result here is the polynomial full-grid propagation for
the exact forced problem, and its single-factor leaf consequence.

Both complete direct sources were read at these versions, with
the directly used implications and hashes checked:

* [Exact full endpoint unit-turn identities](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8:
  original operators, Frobenius reproducer, turn normalization
  and the endpoint-side canonical adapter.
* [Full physical normal source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_all_color_path_normal_bound.md),
  SHA256 08f8932c2cdee4c7afadbb4db3cd85480603f8adb4c936ce29a5517b2d4799c7:
  off-grid difference identity, Gaussian values and normals,
  removable first row, and the real-interval \(Q_N\) estimate.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical test or build was run.
Existing private notes and public manuscripts were unchanged.
