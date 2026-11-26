# A bounded occupation-preserving routed framing coordinate

Private written proof, 18 November 2026.

The original finite source admits a routed insertion of total
occupation degree zero whose principal symbol is the residual
framing coordinate \(r/s\), after the common momentum quotient.
The insertion and all its fixed-order genuine normals have
explicit polynomial bounds on the full heads. Its Ward identity
retains the complete cut, pivot, marked-word, and correction
currents.

This repairs a specific limitation of the earlier routed mark:
the degree-zero trace of that mixed-degree mark drops its
lower-left meridian term. The new mark balances that term
before taking the original trace. No geometric cycle,
nonzero source weight, or small anomaly estimate is inferred.

The complete proof directs are C, W, and M, pinned below.

## 1. The invariant principal coordinate

Use C's fixed irreducible complete reference representation.
Its first meridian is \(J_1=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\).
Choose the same initial head \(j\) with reference meridian
\(H^0=\left(\begin{smallmatrix}a&b_0\\c&d\end{smallmatrix}\right)\),
\(c\ne0\). Such a head exists by irreducibility.
On the reference framing family
\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\qquad s\ne0,
 \qquad \mu_1=F^{-1}J_1F,\quad \mu_j=F^{-1}H^0F,
 \tag{1}
\]
C proves
\[
 \frac{\mu_{j,11}-\mu_{j,21}-d}{c}=\frac rs,
                    \qquad \mathscr V=s\partial_r .
 \tag{2}
\]
The physical sign \(\mu_j=-B_{j-1}^{-1}G_jB_{j-1}\)
and all prefix orders are those of M/C.

The larger regular cut chart retains the nonzero cut
momentum \(p=p_{\rm new}\) and the common scaling of all
head momenta. At completeness, M's literal factorial-basis
symbols give
\[
 K_1=-A^{-1},\qquad e_1=(A^{-1}-1)p,\qquad
 f_1=(1-A)/p.
 \tag{3}
\]
On the open set \(K_1+1\ne0\), define
\[
 q_{\rm cut}=\frac{e_1}{K_1+1}=-p,\qquad
 \tau_{\rm bal}
   =\frac{\mu_{j,11}+q_{\rm cut}\mu_{j,21}-d}{c}.
 \tag{4}
\]
The notation \(q_{\rm cut}\) in (4) is a classical function,
not the quantum parameter \(q\).
On the selected slice \(p=1\), it is \(-1\), so (4) is
exactly \(r/s\) by (2).

More is true than an equality on that slice. Common momentum
scaling by \(\lambda\in\mathbb C^*\) sends
\[
 e_i\longmapsto\lambda e_i,\quad
 f_i\longmapsto\lambda^{-1}f_i,\quad K_i\longmapsto K_i.
 \tag{5}
\]
Each triangular prefix and each meridian is conjugated by
\(\operatorname{diag}(\lambda,1)\). Thus \(\mu_{j,11}\)
is unchanged, \(\mu_{j,21}\) is multiplied by \(\lambda^{-1}\),
and \(q_{\rm cut}\) by \(\lambda\). Formula (4) is invariant.
It therefore descends to the actual common-momentum quotient
on this chart; fixing \(p=1\) identifies its value with \(r/s\).
No averaging over a quantum gauge orbit is being substituted
for this invariance calculation.

W's field fixes the first meridian, hence fixes its entries
and the ratio \(q_{\rm cut}=\mu_{1,12}/(\mu_{1,11}-1)\).
It is equivariant under (5). Consequently
\[
                         \mathscr V\tau_{\rm bal}=1
 \tag{6}
\]
on the fixed reference framing family and its common-momentum
orbit. This does not assert (6) at every neighboring
representation.

## 2. The exact finite insertion

Keep the actual matrices of C/W on \(e_0,\ldots,e_{N-1}\):
\[
 K e_a=-M q^{-1}Q^{-a}e_a,\qquad
 \mathcal E e_a=(MQ^{-a}-M^{-1})e_{a-1}\quad(a>0),
 \qquad \mathcal E e_0=0,\qquad Q=q^2 .
 \tag{7}
\]
The actual \(F\) and its zero top arrow are also retained.
Use C's exact noncommutative \(\widehat\mu_j\), with only
the stated \(K\)-prefix inverses and original finite heads.
Set
\[
 \widehat Q=(K_1+I)^{-1}\mathcal E_1,\qquad
 \boxed{\quad
 T_{\rm bal}=
       \frac{\widehat\mu_{j,11}
                 +\widehat Q\,\widehat\mu_{j,21}-dI}{c}.
 \quad}
 \tag{8}
\]
The order of the product in (8) is part of the definition.
The inverse exists at every physical root
\(q_N=e^{\pi i/N}\), \(M=1\): the eigenvalues of \(K_1+I\) are
\[
                   1-q_N^{-(2b+1)},\qquad 0\le b<N,
 \tag{9}
\]
and none is zero. It also exists on the parameter bidisk
constructed below.

On input \(a>0\), the only nonzero entry of \(\widehat Q\) is
\[
 \widehat Q e_a
   =\frac{M q^{-2a}-M^{-1}}{1-Mq^{1-2a}}e_{a-1},
                         \qquad \widehat Qe_0=0.
 \tag{10}
\]
This uses the eigenvalue of \(K_1\) on the output row \(a-1\);
using its input eigenvalue would give a different insertion.
At the physical root its modulus is
\[
 \frac{\sin(\pi a/N)}
      {|\sin(\pi(a-\tfrac12)/N)|}\le2.
 \tag{11}
\]
To prove the inequality, write \(\theta=\pi/N\).
The denominator's sine is positive for \(1\le a<N\) and
at least \(\sin(\theta/2)\). The addition formula and
triangle inequality give
\(\sin(a\theta)\le\sin((a-\tfrac12)\theta)+\sin(\theta/2)\).
This proves (11), including every finite endpoint.

Total occupation degree is the actual integer shift of
\(a_1+\cdots+a_b\). The entries
\(\widehat\mu_{j,11}\) have degree zero and
\(\widehat\mu_{j,21}\) have degree \(+1\): multiply C's
lower triangular prefix, or count the degrees in its
displayed generators. Formula (10) has degree \(-1\).
Thus
\[
                            \deg T_{\rm bal}=0
 \tag{12}
\]
exactly, at all parameters where it is defined. Total-degree
selection does not remove either meridian term in (8);
their numerical source contractions may still vanish.
Its regular principal symbol is (4), because all products
in (8) have the stated ordered principal symbols and
\(K_1+1\) is a unit on the chosen classical chart.

## 3. A whole-head bidisk and genuine-normal bounds

There are constants \(\eta>0\) and \(C\), independent of
\(N\ge2\), such that (8) is defined on
\[
 |q-q_N|\le\eta N^{-2},\qquad |M-1|\le\eta N^{-1},
 \tag{13}
\]
and
\[
       \|\widehat Q\|_{\rm row}\le C,\qquad
       \|(K_1+I)^{-1}\|_{\rm row}\le CN .
 \tag{14}
\]
Here the row norm is the maximum absolute row sum in the
actual factorial tensor basis. The first estimate concerns
the full product; it is stronger than bounding its two
factors separately.

Here are uniform estimates proving the claim. At the root,
\[
 \delta_b=|1-q_N^{-(2b+1)}|
       =2|\sin((2b+1)\pi/(2N))|\ge 2/N.
 \tag{15}
\]
For \(|m|\le2N\), integration of \(m q^{m-1}\) along the
straight segment from \(q_N\) to \(q\) gives
\[
 |q^m-q_N^m|\le C_0\eta/N,\qquad |q^m|\le C_0
 \tag{16}
\]
on (13), with an absolute \(C_0\), for sufficiently small
fixed \(\eta\). The same estimates and
\(|M^{-1}-1|\le2|M-1|\) show that every denominator in
(9)--(10) changes by at most \(C_1\eta/N\), and every
numerator in (10) by at most \(C_1\eta/N\).
Choose \(\eta\) so that \(C_1\eta<1\). Each denominator is
then at least half its root modulus by (15).
At the root, the numerator in (10) is at most twice that
denominator by (11). The perturbation estimate and (15)
therefore bound the ratio uniformly. This proves (14).
It also proves invertibility on a neighborhood of the
closed smaller bidisk, as needed for Cauchy estimates.

The matrices \(K_i^{\pm1},\mathcal E_i,F_i\) have uniformly
bounded row norms on (13), at fixed braid width. The prefix
formulas in C are finite sums of a fixed number of their
products. Hence (8) has
\[
                         \|T_{\rm bal}\|_{\rm row}\le C_j
 \tag{17}
\]
uniformly in \(N\); the constant retains the fixed nonzero
\(c\) and the reference \(d\).
On the half bidisk, the finite-matrix Cauchy formula gives
for every fixed \(u,v\ge0\)
\[
 \|\partial_q^u\partial_M^v T_{\rm bal}\|_{\rm row}
 \le C_j\,u!v!
           (2N^2/\eta)^u(2N/\eta)^v .
 \tag{18}
\]
The same bound holds for \(\widehat Q\), with its own fixed
constant. This is an operator-norm Cauchy estimate, so no
factor equal to the dimension of the tensor space is inserted.

For ordinary finite-color quantum normals use the genuine
path \(M=-q^N\). On a sufficiently small \(q\)-disk of radius
\(\eta' N^{-2}\), this path lies inside the half bidisk:
integration of \(Nq^{N-1}\) bounds \(|-q^N-1|\) by
\(C N|q-q_N|\). The composed insertion is holomorphic and
bounded there. Its fixed \(k\)-th ordinary \(q\)-derivative
is therefore bounded by \(C_j k!(C N^2)^k\).
All derivatives act on (8) as a whole, including its
denominator and its finite endpoint rows.

The bounds (17)--(18) are bounds for this insertion.
They are not estimates of the unknown marked braid word,
the scalar knot period, or the sourced Ward anomaly.

## 4. Exact Ward and source identities

Keep W's original divergence-form current, coefficient
ordering, and original source functional:
\[
 \mathcal D_N(B)=h^{-1}\sum_\iota[X_\iota,A_\iota B],
 \qquad \Phi_O(B)=\varkappa_\beta\operatorname{Tr}(PBO).
 \tag{19}
\]
Here \(P\) is the actual cut and pivotal tensor and \(O\)
is the entire marked word. Its boundary current is
\[
 \mathcal C_P(B,O)=\frac{\varkappa_\beta}{h}
 \sum_\iota\left\{
 \operatorname{Tr}([P,X_\iota]A_\iota BO)
 +\operatorname{Tr}(PA_\iota B[O,X_\iota])\right\}.
 \tag{20}
\]
Exactly as in C, finite multiplication gives
\[
 [\mathcal D_N,M_{T_{\rm bal}}](B)=
 \frac1h\sum_\iota\left\{
 [X_\iota,T_{\rm bal}]A_\iota B+
 [X_\iota,[A_\iota,T_{\rm bal}]B]\right\}.
 \tag{21}
\]
Define the exact operator on finite insertions
\[
 \mathcal A_N^{\rm bal}
       =[\mathcal D_N,M_{T_{\rm bal}}]-\operatorname{Id}.
 \tag{22}
\]
Its principal restriction to the fixed reference family
and its common-momentum orbit vanishes, by (6).
This is not an ambient principal vanishing statement or a
whole-head \(O(h)\) norm estimate. In particular (17)
does not imply that (22) is small.

For every polynomial \(p(t)=\sum_k p_kt^k\), let
\[
 \mathcal A_{N,p}^{\rm bal}
 =\sum_{k\ge1}p_k\sum_{\ell=0}^{k-1}
 M_{T_{\rm bal}}^\ell\mathcal A_N^{\rm bal}
                         M_{T_{\rm bal}}^{k-1-\ell}.
 \tag{23}
\]
The product commutator rule and the exact identity
\(\Phi_O(\mathcal D_NB)=\mathcal C_P(B,O)\) give
\[
 \boxed{\quad
 \Phi_O(p'(T_{\rm bal})B)=
  \mathcal C_P(p(T_{\rm bal})B,O)
   -\Phi_O(p(T_{\rm bal})\mathcal D_N(B))
   -\Phi_O(\mathcal A_{N,p}^{\rm bal}(B)).
 \quad}
 \tag{24}
\]
No divergence term is deleted:
\(\mathcal D_N(I)=h^{-1}\sum_\iota[X_\iota,A_\iota]\)
is retained. For a marked product every
\([O,X_\iota]\) in (20) has its full ordered expansion.
The cut and tail-pivot commutators keep the actual zero
arrows and all quantum normals.

All three terms in (24) preserve the degree bookkeeping.
Indeed W has degrees
\[
 (\deg X_E,\deg X_F,\deg X_K)=(-1,1,0),\qquad
 (\deg A_E,\deg A_F,\deg A_K)=(1,-1,0),
 \tag{25}
\]
so \(\mathcal D_N\) preserves degree, as does
\(M_{T_{\rm bal}}\). In particular the source of the
degree-zero insertion in (8) is already compatible with
the exact common occupation symmetry.

## 5. A bounded exterior resolvent and its full source current

Set
\[
 R_{\rm bal}(\zeta)=(\zeta I-T_{\rm bal})^{-1}.
 \tag{26}
\]
For \(|\zeta|>C_j\), (17) gives the uniform finite-matrix
Neumann estimate
\[
 R_{\rm bal}(\zeta)=
   \sum_{k\ge0}\frac{T_{\rm bal}^k}{\zeta^{k+1}},
 \qquad
 \|R_{\rm bal}(\zeta)\|_{\rm row}
                           \le (|\zeta|-C_j)^{-1}.
 \tag{27}
\]
This also supplies normal estimates by Cauchy on the
smaller bidisks. No spectrum analogous to the earlier mixed-degree
clock spectrum is asserted for (8). It is an ordinary
finite rational resolvent inside that fixed exterior circle.

The one-variable marked source is
\[
             \mathcal L^{\rm bal}_{N,B,O}(\zeta)
                        =\Phi_O(R_{\rm bal}(\zeta)B).
 \tag{28}
\]
A fixed positively oriented circle \(|\zeta|>C_j\) recovers
\(\Phi_O(B)\) by its Cauchy integral and
\(\Phi_O(p(T_{\rm bal})B)\) after multiplication by \(p(\zeta)\).
The whole circle and this identity are valid throughout the
smaller parameter bidisk. Bounds for the insertion do not
bound the unknown source coefficients in (28).

Since \(\partial_\zeta R_{\rm bal}=-R_{\rm bal}^2\), the
exact inverse-commutator rule gives
\[
 [\mathcal D_N,M_{R_{\rm bal}}]+\partial_\zeta M_{R_{\rm bal}}
           =M_{R_{\rm bal}}\mathcal A_N^{\rm bal}M_{R_{\rm bal}}.
 \tag{29}
\]
Applying the actual source gives
\[
 \boxed{\begin{split}
 \partial_\zeta\mathcal L^{\rm bal}_{N,B,O}
 ={}&-\mathcal C_P(R_{\rm bal}B,O)
       +\Phi_O(R_{\rm bal}\mathcal D_N(B))\\
    &+\Phi_O\big(R_{\rm bal}
                    \mathcal A_N^{\rm bal}(R_{\rm bal}B)\big).
 \end{split}}
 \tag{30}
\]
The anomaly acts on the whole displayed insertion.
This identity is meromorphic in \(\zeta\) and exact for
the original finite arrays.

For fixed regular interior rows and bounded exponential
momentum probes, the finite-band proof of (17) applies
after conjugating each shift by those weights. The resulting
exterior Neumann series allows its principal limit term
by term: each fixed power has principal symbol
\(\tau_{\rm bal}^k\), and the geometric tail is uniformly
bounded. The principal resolvent is therefore
\(1/(\zeta-\tau_{\rm bal})\). Its regular continuation to
the fixed reference framing quotient is \(1/(\zeta-r/s)\).
Only this principal continuation is meant on the complex
framing chart; no uniform asymptotic statement for a
complex coherent kernel or a geometric contour is asserted.

## 6. What is now available

The source now contains a bounded, degree-zero routed
coordinate with the correct framing-quotient symbol,
polynomial genuine normals, and exact polynomial and
resolvent current identities. The lower-left meridian
term is no longer eliminated by occupation-degree selection;
this does not assert that its contraction is nonzero.

The unknown part is the comparison of these exact currents
with the original relative geometric chain, including its
ends and possible same-action layers. Neither the bounded
coordinate nor (24)/(30) computes a framing period, an
endpoint multiplicity, or a nonzero geometric coefficient.
The old explicit clock spectrum belongs to the old
mixed-degree insertion and is not transferred to (8).

## Complete proof-source pins

* C: notes/research_actual_routed_centralizer_coordinate.md,
  SHA256 6bc8e8438646ad713d3951f072259cfd8844a13e97c844601b2eca11a9497033.
* W: notes/research_actual_weighted_ward_centralizer_lift.md,
  SHA256 e689364ab8e756ef51f8da43a7ea86d84086afd6bf57ffbe0af1a4f508c2648a.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.

All three complete texts were freshly read in full in this
active author sequence and retained unchanged. Their actual
matrix, symbol, prefix, current, and parameter conventions
were checked. All new bounds and identities are proved above.
No frozen or public file was changed.
