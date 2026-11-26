# What cyclic doubling controls for the actual open Newton source

Written deduction, 10 November 2026. No mathematical numerical
evaluation is used. The positive three/four cyclic theorem does give
an exact doubling statement for an open matrix word, but its squares
are bilinear squares. The positive Hermitian double reverses the
crossings in one half. This distinction persists in the literal
full-Hermite boundary sewing and already gives a strict discrepancy
for one original block. The corrected rank-one boundary pairing
below retains the original open scalar exactly; its calibrated
geometric estimate is not supplied by the positive cyclic theorem.

## 1. Fixed source and full boundary pairing

Keep the complete original algebra
\[
 \mathcal H_N=\mathbb C[z]/P_N,\quad
 P_N(z)=2T_N(z/2)+2,\quad D=N-1,\quad q=e^{\pi i/N},
\]
and the real Newton basis
\[
 e_j(z)=\frac{\prod_{\ell<j}(c_\ell-z)}{s_j^2},
 \qquad c_j=q^{2j+1}+q^{-2j-1},\qquad
 s_j=\prod_{\ell=1}^j2\sin(\pi\ell/N).
 \tag{1}
\]
Here \(s_0=1\). Write \(v(z)=(e_0(z),\ldots,e_D(z))^T\).
The original Frobenius functional and genuine unscaled turn are
\[
 \phi_N(f)=(-1)^D N^2[z^D](f\bmod P_N),\qquad
 \mathscr R e_j=e_{D-j}.
 \tag{2}
\]
Let \(J_{ij}=\delta_{i+j,D}\). The full original source identities are
\[
 \phi_N(e_i e_j)=J_{ij},\qquad
 \phi_N(f^\sharp\mathscr R g)=\sum_j\overline{f_j}g_j,
 \qquad f^\sharp(z)=\overline{f(\bar z)}.
 \tag{3}
\]
The coefficients \(f_j,g_j\) in (3) are Newton coefficients.
Products and remainders in (2)--(3) are taken in the full quotient,
not on its distinct-node reduction. Thus all repeated-node first
normals and the odd simple node are retained. These are precisely
the source identities of [the Newton-turn theorem][newt],
Sections 1--4.

For any \(N\)-by-\(N\) coefficient matrix \(B\), define its literal
two-boundary polynomial
\[
             Q_B(x,y)=v(x)^T Bv(y).
 \tag{4}
\]
Let \(\mathscr R_x,\mathscr R_y\) act separately on these two
ordinary polynomial variables. For matrices \(B,C\), finite expansion
in (3) gives the three exact identities
\[
\begin{split}
 \phi_x\phi_y[Q_B Q_C]&=\operatorname{tr}(B^TJCJ),\\
 \phi_x\phi_y[Q_B\,\mathscr R_x\mathscr R_y Q_C]
       &=\operatorname{tr}(B^TC),\\
 \phi_x\phi_y[Q_B^\sharp\,\mathscr R_x\mathscr R_y Q_C]
       &=\operatorname{tr}(B^\dagger C).
\end{split}                                                    \tag{5}
\]
In the last line the reflection conjugates both coefficients and
ordinary variables, as in (3). For example the first line is
\(\sum B_{ij}C_{kl}J_{ik}J_{jl}\); each turn replaces a coefficient
index by its reversal. This proves every line without a nodal
approximation or a nonzero-value division.

In particular, inserting the two actual turns but no conjugation
gives \(\sum B_{ij}^2\). Inserting the same turns and coefficient
reflection gives \(\sum|B_{ij}|^2\). Omitting the turns instead
leaves the two \(J\)'s in the first line. These are different
literal boundary sewings.

For comparison the original concatenation operation is
\[
 Q_{BC}(z,z')=\phi_x\phi_y
       [Q_B(z,x)K_N(x,y)Q_C(y,z')],
 \qquad K_N(x,y)=v(x)^Tv(y).
 \tag{6}
\]
Indeed its matrix product is \(B J I J C=BC\). Equation (6) is
the exact composition in [the endpoint extension criterion][ext],
Section 6. It explains why the boundary turns or bare-edge adapters
cannot be deleted when comparing an open word with a cyclic trace.
There are no unrecorded powers of \(N\) in (5)--(6): the
\((-1)^D N^2\) factors of the full traces are already in (2).

## 2. Same-sign and Hermitian doubles of a three/four word

Let \(M\) be the original crossing multiplication matrix, including
its Cartan scalar \(\kappa_N=q^{D^2/2}\), and let
\[
 A_n=JM^n,\qquad B=A_{n_1}\cdots A_{n_m},
 \qquad n_j\in\{3,4\}.
 \tag{7}
\]
The original multiplication and full-Hermite reflection identities
in [newt] are
\[
 (M^n)^T=JM^nJ,\qquad
 (M^n)^\dagger=JM^{-n}J.
\]
Consequently
\[
 A_n^T=A_n,\qquad A_n^\dagger=A_{-n},\qquad
 B^T=A_{n_m}\cdots A_{n_1},\quad
 B^\dagger=A_{-n_m}\cdots A_{-n_1}.
 \tag{8}
\]
The reflected sign is the original signed crossing sign. In
particular (8) is not conjugation of a completed fixed-sign tangle
while leaving its crossings unchanged.

**Proposition 1.** The two natural doubles are exactly
\[
\begin{split}
 T_{\rm bil,N}
   &=\operatorname{tr}(BB^T)
     =\operatorname{tr}
        (A_{n_1}\cdots A_{n_m}A_{n_m}\cdots A_{n_1})
     =\sum_{i,j}B_{ij}^{\,2},\\
 T_{\rm H,N}
   &=\operatorname{tr}(B^\dagger B)
     =\operatorname{tr}
        (A_{-n_m}\cdots A_{-n_1}A_{n_1}\cdots A_{n_m})
     =\|B\|_{\rm HS}^2.
\end{split}                                                    \tag{9}
\]
The first is the second line of (5) with \(C=B\); the second is
its third line. They include the complete finite matrices and both
parities.

Only the first word in (9) is a positive three/four word. Thus,
writing \(k=\#\{j:n_j=4\}\), the [full cyclic theorem][cyc] supplies
the genuine nonzero asymptotic
\[
 T_{\rm bil,N}
   =\kappa_N^{\,2(m+k)}
       A_{\rm pal}e^{NF_{\rm pal}}(1+O(N^{-1})),
                 \qquad A_{\rm pal}\ne0 .
 \tag{10}
\]
The action and Gaussian coefficient in (10) are those of that
palindromic cyclic word, with their original branches. A simultaneous
reversal of every sign would give its conjugate. It does not turn
the mixed-sign second word in (9) into a covered word.

Cauchy--Schwarz gives the exact inequality in the direction
\[
              |T_{\rm bil,N}|\le T_{\rm H,N}.
 \tag{11}
\]
Hence a consequence of the established cyclic theorem is
\[
 \liminf_{N\to\infty}\frac1N\log\|B\|_{\rm HS}
       \ \ge\ \frac12\Re F_{\rm pal}.
 \tag{12}
\]
It is a lower bound on a norm. Neither an upper bound on that norm
nor a lower bound on any specified open observation follows from
(11). The statement does not exclude a separately proved comparison
between these quantities.

There is a strict discrepancy in the actual source, without choosing
an artificial matrix. From the full triangular crossing formula,
\[
 (M^n)_{ii}=\kappa_N^n(-1)^{ni}q^{ni(i+1)}.
 \tag{13}
\]
For \(B=A_n\), its entries at \((D,0)\) and \((D-1,1)\)
are the \(i=0,1\) diagonal entries in (13). Their ratio is
\((-1)^nq^{2n}\), which is nonreal whenever \(N>2n\).
The squares of these two nonzero entries therefore have different
arguments. Strictness in the finite triangle inequality proves
\[
        |\operatorname{tr}(A_n^2)|<\|A_n\|_{\rm HS}^2
                   \qquad(n=3,4,\ N>2n).
 \tag{14}
\]
Thus the same-sign cyclic double is not the positive Gram double,
even up to a unit scalar, already for a single original block.
Equation (14) asserts no exponential size of the discrepancy and
does not rule out an additional polynomial comparison.

## 3. What a literal Plancherel argument would measure

There is an exact coefficient Plancherel formula:
\[
 \|B\|_{\rm HS}^2=
 \frac1{(2\pi)^2}\int_0^{2\pi}\int_0^{2\pi}
   \left|\sum_{i,j=0}^D B_{ij}e^{i(i\xi+j\eta)}\right|^2
                                  d\xi\,d\eta .
 \tag{15}
\]
This is finite Fourier orthogonality of the complete Newton
coefficient array. Its Fourier polynomial is not the ordinary-color
source \(Q_B(-2\cos\xi,-2\cos\eta)\).

For the latter ordinary-color integral, define the actual positive
moment matrix
\[
 G_{ij}=\frac1{2\pi}\int_0^{2\pi}
                 e_i(-2\cos\xi)e_j(-2\cos\xi)\,d\xi .
 \tag{16}
\]
It is positive definite because a nonzero polynomial cannot vanish
on the whole real interval. Direct finite expansion gives
\[
 \frac1{(2\pi)^2}\int\!\!\int
      |Q_B(-2\cos\xi,-2\cos\eta)|^2\,d\xi\,d\eta
                 =\operatorname{tr}(B^\dagger G B G).
 \tag{17}
\]
The Newton basis is not orthonormal for this measure. In fact
\(G_{00}=1\) and \(G_{01}=c_0/s_1^2>0\) for \(N>2\),
because the mean of \(-2\cos\xi\) is zero. Replacing \(G\) by
the identity in (17) is not a source identity; it requires a
separate metric estimate with its actual exponential cost.

Sampling only the physical values has an additional exact problem.
The nodes satisfy \(c_j=c_{D-j}\), so there are fewer than \(N\)
distinct nodes at every \(N\ge2\). Let
\[
                 r_N(z)=\prod_{c\ {\rm distinct}}(z-c).
 \tag{18}
\]
Its degree is \(N/2\) for even \(N\) and \((N+1)/2\) for odd
\(N\). It is a nonzero element of \(\mathcal H_N\), but all
its physical values vanish. At each repeated root its first
derivative is nonzero. Thus a norm based only on physical color
values is degenerate on the actual source space. Nondegeneracy of
(3) also implies that some full Frobenius pairing detects (18).
A value-only sampling or Plancherel argument therefore cannot
replace the full boundary metric without recovering the normals.

## 4. The positive pairing that retains a specified open scalar

For arbitrary complex ordinary colors \(w_L,w_R\), set
\[
 a=\overline{v(w_L)},\qquad b=v(w_R),\qquad
 E_L=aa^\dagger,\quad E_R=bb^\dagger .
 \tag{19}
\]
Both \(E_L,E_R\) are rank-one positive matrices; their normalization
is not changed to make them idempotent. The literal open
observation has the exact representation
\[
\begin{split}
 Q_B(w_L,w_R)&=a^\dagger B b,\\
 |Q_B(w_L,w_R)|^2
       &=\operatorname{tr}(B^\dagger E_L B E_R).
\end{split}                                                    \tag{20}
\]
This is a positive reflected pairing with its actual rank-one
boundary factors retained, rather than an undecorated cyclic word.
It preserves the desired scalar exactly.

The boundary factors have an intrinsic full-source interpretation. The
Riesz element for evaluation at \(w\) in (3) is
\[
           k_w(z)=\sum_{j=0}^D\overline{e_j(w)}e_j(z),
 \qquad f(w)=\phi_N(k_w^\sharp\mathscr R f).
 \tag{21}
\]
Its squared norm is \(\sum|e_j(w)|^2\). Thus (20) is obtained
from the original finite source with (21), not by declaring a
physical marked cap to be an adjoint cap. Any externally prescribed
normalization \(\chi_N Q_B\) has exactly the squared normalization
\(|\chi_N|^2\) multiplying (20). In particular original dimension,
framing and peripheral factors are not set to one.

The corresponding elementary upper bound is
\[
 |Q_B(w_L,w_R)|
       \le \|B\|_{\rm HS}\,\|v(w_L)\|_2\,\|v(w_R)\|_2 .
 \tag{22}
\]
If a new mixed-sign Gram theorem were to bound the first factor,
the two evaluation norms in (22) would still have to be retained.
For example upper rates \(L\) for \(\|B\|_{\rm HS}^2\) and
\(\beta_L,\beta_R\) for these evaluation norms yield only the
rate \(L/2+\beta_L+\beta_R\), not automatically the original
open geometric rate.

For the required outside-angle loss it would be sufficient instead
to estimate the actual positive scalar on the right of (20) at
twice the desired open action, with its outside-angle deficit.
That is a concrete source-compatible energy target. It is not
proved here, and positivity of (20) alone supplies no lower bound
for \(Q_B\). In particular a large norm of \(Bb\) does not force
its component along \(a\) to be large.

## 5. Why the existing action and reflection theorems do not close this gap

The [open-word action][openH] already contains the endpoint terms
\[
 B(e,u)=-2J(1/2-u)-3J(u)-J(e-u)
 \tag{23}
\]
and their original quadratic coupling, at order \(N\). For example
\[
 B_{uu}=-\pi\{2\tan\pi u+3\cot\pi u+\cot\pi(e-u)\}.
 \tag{24}
\]
On the proved private-leg/endpoint domain its negative real part
is strictly positive. Thus the boundary insertion is not an
action-independent bounded prefactor in a cyclic saddle. Neither
(9) nor the cyclic theorem identifies \(F_{\rm pal}/2\), or a
mixed-sign Gram action, with the open action including (23).
No equality or inequality between those critical actions is
asserted here.

The [original reflection obstruction][obstruction] rules out a
different attempted shortcut: the full reduced word functional
cannot be made positive on every reflection square. Its value on
the identity is zero, while its value on the normalized original
unknot Markov word is one. A positive functional with zero identity
value would vanish by Cauchy--Schwarz. This obstruction concerns
the original marked functional, not the valid metric (3) or
the positive scalar (20).

There is also an actual positive [planar three-port double][double].
With its prescribed reversed port order, one complete circle per
seam, and one physical mark, its exact scalar is
\[
 Z_{\rm dbl}
    =\sum_{(a,b,c)\in\mathcal D_N}
             \frac{|Z_\Gamma(a,b,c)|^2}{\theta_N(a,b,c)}.
 \tag{25}
\]
The theta factor is the original positive marked theta scalar.
Its generic quotient retains the one prescribed first normal
before specialization. Its source and [topological certificate][top]
reverse all crossings in the reflected half. It is not the
same-sign cyclic word of (10). Even for this correctly normalized
positive double, the source theorem still requires a sharp estimate
of the coherent half-packets \(Z_\Gamma\). Its geometric double has
the recorded theta-volume subtraction; one may not silently replace
that normalization by twice an open action.

These distinctions leave three possible new estimates, each with
a specific exact source: a mixed-sign Gram theorem for the second
line of (9), a boundary-decorated estimate for (20), or a coherent
weighted half-packet estimate for (25). None is supplied by the
established positive cyclic theorem. They may be useful corrected
routes, but the cyclic result and Cauchy/Plancherel alone do not
prove the complete open boundary gap at its own geometric action.
The original open-source obligations in [the stability reduction][open]
therefore remain, except for the particular component sources
already proved separately. No new signed lower bound, short-filling
stability theorem, or closed-knot volume theorem follows here.

## 6. Frozen direct source bindings

All source identities and scope statements above use the following
unchanged files. Hashes are provenance bindings, not mathematical
evaluations.

| Source | SHA-256 |
|---|---|
| [Newton turn and full positive Gram][newt] | `d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3` |
| [Original reflection obstruction][obstruction] | `98263806bbbb5d69a9c595d0bba5e9a653063bc306c36f5b75bb482427e7ce85` |
| [Planar three-port reflected source][double] | `f0a995003e4060935158fbbecbbad6d2e0b25ab8785a730e2b9eb5f9221e142b` |
| [Actual double topology][top] | `ebbb359e3d76cbfdb2f6563e9cedc0bb5d66c6e4e9fa5a18f25764064590fa2f` |
| [Full positive cyclic theorem][cyc] | `eabe5cc6350bf4367ad97b9388e6814e18a1b626123da112878f9db8709daf47` |
| [Complete open-source stability reduction][open] | `5d501024dddb98ff28f1ae3d44110d4a34bfc82d8063ff01353315c3efbfc31c` |
| [Original open-word action and Hessian][openH] | `21556711a3ac410ce7d3e4dda0d3a6395cd7ee2a69993d82f5f8325c6e7dad23` |
| [Exact kernel composition][ext] | `1c8dbffa027dda4da39d1e1d2954305520708cc413e1e1ae7bc46a2aa730d8bb` |

[newt]: actual_newton_turn_positive_gram.md
[obstruction]: original_reflection_gram_obstruction.md
[double]: actual_planar_three_port_reflection_double.md
[top]: actual_planar_three_port_double_topology.md
[cyc]: research_mixed_full_cyclic_period.md
[open]: research_mixed_open_source_stability_reduction.md
[openH]: research_mixed_open_word_hessian.md
[ext]: research_mixed_endpoint_packet_extension_criterion.md
