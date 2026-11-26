# The exact filtered carrier at a reciprocal resonance

Private written proof, 16 November 2026.

The Newton degree filtration gives an exact quadratic carrier for a
turned ordinary product. At a reciprocal resonance its integral null
direction has a nontrivial linear carrier and changes the output
degree. Keeping that degree gives a shifted binomial, together with
explicit boundary and amplitude-difference terms. These are identities
of the associated graded source, not replacements for the full
canonical product.

The original triangular crossing matrix and the need to retain its
normal data are established in the source literature. The present
calculation identifies the complete linear carrier of this graded
resonance and its precise relationship to the original trace.

## 1. The filtered original algebra

Put
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^D,\quad\kappa=q^{D^2/2},\quad
 s_j=2\sin(\pi j/N),\quad S_j=\prod_{a=1}^j s_a,\quad S_0=1,
\]
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_k(Z)=S_k^{-2}\prod_{j<k}(c_j-Z),\qquad
 p_k(Z)=(-1)^kS_k^2e_k(Z).
 \tag{1}
\]
Thus \(p_k\) is monic of degree \(k\). Use the full original algebra
\[
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 P_N(Z)=2T_N(Z/2)+2,\qquad
 V_n=\kappa^nTR^{-n}T,\quad U_\tau=V_\tau,\quad \tau=\pm1 .
 \tag{2}
\]
Here \(T_N\) is Chebyshev's polynomial, \(Te_k=e_{D-k}\) is the
original turn, and \(R\) is the original crossing of the first source.
Every canonical representative has degree at most \(D\). Let
\(F_k\mathcal A_N\) be the degree-at-most-\(k\) subspace for
\(0\le k\le D\), with \(F_{-1}=0\) and \(F_k=\mathcal A_N\)
for \(k\ge D\).

The all-degree triangular formula in the first source gives
\[
 \operatorname{gr}V_n(x^k)=\lambda_n(k)x^k,\qquad
 \lambda_n(k)=(-1)^{nk}q^{-nk(k+1)},\qquad 0\le k<N.
 \tag{3}
\]
Indeed the diagonal for \(U_\sigma\) is
\((-1)^kq^{-\sigma k(k+1)}\); the two unit maps are inverses
and \(V_n=U_+^n\). Hence every signed power preserves the flag,
and its diagonal is (3).

Since \(P_N\) is monic of degree \(N\), the associated graded algebra is
\[
                       \operatorname{gr}\mathcal A_N
                               \simeq\mathbb C[x]/(x^N).
 \tag{4}
\]
In particular canonical multiplication induces ordinary multiplication
in total degree below \(N\). In total degree at least \(N\) its graded
image is zero; its actual canonical image need not be zero.

Fix \(r\ge1\) and nonzero integers \(n_1,\ldots,n_r\), and consider the actual
multilinear map
\[
 \mathcal M_{\tau,\mathbf n}(f_1,\ldots,f_r)
       =U_\tau\operatorname{can}\prod_{i=1}^rV_{n_i}f_i.
 \tag{5}
\]
For \(\mathbf k=(k_1,\ldots,k_r)\in\mathbb Z_{\ge0}^r\) with
\(K=\sum_i k_i<N\), its exact top-degree identity is
\[
 \mathcal M_{\tau,\mathbf n}(p_{k_1},\ldots,p_{k_r})
       =\Phi_N(\mathbf k)p_K+F_{K-1}\mathcal A_N,
 \tag{6}
\]
\[
 \Phi_N(\mathbf k)
   =(-1)^{\ell(\mathbf k)}
       q^{-\{\mathcal Q(\mathbf k)+\ell(\mathbf k)\}},
 \quad
 \mathcal Q(\mathbf k)=\sum_i n_i k_i^2+\tau K^2,\quad
 \ell(\mathbf k)=\sum_i(n_i+\tau)k_i .
 \tag{7}
\]
This follows by multiplying the individual diagonals and then
the outer diagonal. It is an equality in the indicated graded
quotient; the lower-degree terms of (6) remain in the actual source.
All ordinary exterior parameters can be retained coefficientwise.

## 2. The resonant null direction and its full linear carrier

Set
\[
 \gamma=\sum_i\frac1{n_i},\qquad
 L=\operatorname{lcm}_i|n_i|,\qquad
 \mathbf a=(L/n_1,\ldots,L/n_r).
 \tag{8}
\]
The quadratic matrix in (7) is
\[
 H=\operatorname{diag}(n_i)+\tau\mathbf1\mathbf1^{\mathsf T},
 \qquad \det H=\Big(\prod_i n_i\Big)(1+\tau\gamma).
 \tag{9}
\]
For example (9) follows by factoring the diagonal matrix and
using the rank-one determinant identity, which itself follows
by multilinearity of the determinant.

Assume the actual outer-turn resonance
\[
                             \gamma=-\tau.
 \tag{10}
\]
Then \(H\mathbf a=0\), its kernel is one-dimensional, and
\(\mathbf a\) is a primitive integral vector. To see the kernel
assertion, \(Hz=0\) implies
\(z=-\tau(\sum_i z_i)(1/n_i)_i\). Primitivity follows from
\(\gcd_i(L/|n_i|)=1\): for each prime dividing \(L\), some
\(|n_i|\) contains its maximal prime power.
Crucially,
\[
 \sum_i a_i=-\tau L,\qquad
 \ell(\mathbf a)=L(r-1).
 \tag{11}
\]
Extend the elementary chirp (7) to all integer \(\mathbf k\).
Since \(H\mathbf a=0\), its exact translation law is
\[
 \boxed{\quad
 \Phi_N(\mathbf k+\mathbf a)=\chi_N\Phi_N(\mathbf k),
 \qquad
 \chi_N=(-1)^{L(r-1)}q^{-L(r-1)}.
 \quad}
 \tag{12}
\]
Both the quadratic cross term and \(\mathcal Q(\mathbf a)\)
vanish, but the linear carrier in (11) does not generally vanish.
Its integer exponent is nevertheless even at resonance:
\[
 0=\mathbf a^{\mathsf T}H\mathbf a
       \equiv\sum_i(n_i+\tau)a_i=L(r-1)\pmod2.
 \tag{12a}
\]
Here the cross terms disappear modulo two and \(a_i^2\equiv a_i\).
Thus the full derived carrier simplifies to
\(\chi_N=q^{-L(r-1)}\), without discarding its finite \(q\)-shift.

If \(r=1\), (10) says \(n_1=-\tau\). Then \(\chi_N=1\),
and the original map is exactly \(U_\tau V_{-\tau}=I\),
not merely an identity of associated graded maps.
The remaining statements about a nontrivial carrier concern \(r\ge2\).

For \(r\ge2\), put \(c=L(r-1)>0\). If \(N\ge2c\), then
\[
                       |1-\chi_N|^{-1}\le C_c N.
 \tag{13}
\]
Indeed for even \(c\) the denominator is
\(2\sin(\pi c/(2N))\ge2c/N\); \(c\) is even by (12a).
This scalar bound does not justify translating a closed source:
the same translation changes its output degree by \(-\tau L\).

## 3. The exact truncated binomial identity

Let
\[
 \Omega_N=\{\mathbf k\in\mathbb Z_{\ge0}^r:\ \sum_i k_i<N\}.
 \tag{14}
\]
Choose any complex weights \(A(\mathbf k)\) on this finite set,
and extend \(W(\mathbf k)=\mathbf1_{\Omega_N}A(\mathbf k)\) by zero
to \(\mathbb Z^r\). Introduce an independent degree character \(z\ne0\):
\[
 \Theta_N(z)=\sum_{\mathbf k\in\Omega_N}
                  A(\mathbf k)\Phi_N(\mathbf k)z^{K(\mathbf k)}.
 \tag{15}
\]
The variable \(z\) is a bookkeeping variable for the graded output
degree. It has not been identified with a physical angular color.
Reindexing a finite sum and using (11)--(12) gives exactly
\[
 \boxed{\quad
 (1-\chi_Nz^{-\tau L})\Theta_N(z)
  =\sum_{\mathbf k\in\mathbb Z^r}
    [W(\mathbf k)-W(\mathbf k-\mathbf a)]
       \Phi_N(\mathbf k)z^{K(\mathbf k)}.
 \quad}
 \tag{16}
\]
This is a finite Laurent-polynomial identity. Its right side consists
of the following three retained pieces:

* on \(\Omega_N\cap(\Omega_N+\mathbf a)\), the weight is
  \(A(\mathbf k)-A(\mathbf k-\mathbf a)\);
* on \(\Omega_N\setminus(\Omega_N+\mathbf a)\), the weight is
  \(A(\mathbf k)\);
* on \((\Omega_N+\mathbf a)\setminus\Omega_N\), the weight is
  \(-A(\mathbf k-\mathbf a)\).

The last two are the actual boundary terms of this finite
degree-window reindexing. Terms outside \(\Omega_N\) in (16) are
formal chirp terms; they are not extra admissible Newton states.
In particular (16) never invokes a source move through a negative
index or a canonical degree at least \(N\).

For \(|z|=1\) away from the displayed binomial zeros, (16) gives
the elementary bound by the sum of the absolute weights of all
three pieces, divided by \(|1-\chi_Nz^{-\tau L}|\).
It gives no bound on those weights by itself.

The zeros of this binomial are exactly
\[
                          z\in q^{-\tau(r-1)}\mu_L .
 \tag{17}
\]
Using the unsimplified carrier in (12) gives the set
\((-1)^{r-1}q^{-\tau(r-1)}\mu_L\). If \(L\) is even,
\(-1\in\mu_L\). If \(L\) is odd, all \(L/n_i\) are odd
integers, and (10) multiplied by \(L\), reduced modulo two,
forces \(r\) odd. This proves (17) in both cases.
Equivalently (12a) simplifies the binomial directly to
\(z^L=q^{-\tau L(r-1)}\).

Thus the limiting degree-character roots are \(\mu_L\), whose
formal folded values are \(2\cos(2\pi k/L)\). This agrees with
the phase grid in the projective resonance theorem, while retaining
the explicit finite shift \(q^{-\tau(r-1)}\). It does not prove
that the degree character \(z\) is the physical \(v\), or that the
same binomial divides any maximal minor of the full source rows.

At a zero of the binomial, the complete term
\(\Phi_N(\mathbf k)z^{K(\mathbf k)}\) is constant along each
integral null line. Positive real weights on a finite segment
of such a line therefore add coherently. The real microscopic
weights in (22) have this positivity. This says nothing about
cancellation between different lines or the remaining canonical
terms, but precludes using the carrier-only cancellation below
as evidence of vanishing at a resonant degree character.

A separate completed chirp calculation illustrates the boundary
issue. The function \(\Phi_N\) is \(2N\)-periodic in every integer
coordinate. Hence on \((\mathbb Z/2N\mathbb Z)^r\), its unweighted
sum is multiplied by \(\chi_N\) under translation by \(\mathbf a\).
For \(r\ge2\) and \(N>c=L(r-1)\), \(\chi_N\ne1\), so this
completed sum is zero. Indeed \(\chi_N=1\) would imply
\(2N\mid (N-1)c\), and therefore \(N\mid c\).
This completed group is not the Newton simplex (14); its closed
translation orbit exits the original degree range. Its vanishing
is not a vanishing assertion for an original source.

## 4. What original closing actually extracts

Let arbitrary canonical inputs have expansions
\[
 f_i(Z)=\sum_{k=0}^D A_i(k)p_k(Z),\qquad
 f_i(t,Z)=\sum_{k=0}^D A_i(k)t^kp_k(Z).
 \tag{18}
\]
The second variable \(t\) is an ordinary degree marker; at \(t=1\)
the original input is recovered. Apply the actual map (5) before
the original trace \(\phi_N\).
For \(K<N\), the coefficient of \(t^K\) has degree at most \(K\),
and its leading coefficient is
\[
 \Theta_{N,K}=
  \sum_{\substack{\mathbf k\ge0\\\sum_i k_i=K}}
             \Phi_N(\mathbf k)\prod_i A_i(k_i).
 \tag{19}
\]
The Frobenius rule \(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\)
annihilates degree below \(D\). Also \(S_D=N\), by taking
absolute values in
\(\prod_{j=1}^{N-1}(1-e^{2\pi i j/N})=N\).
Thus
\[
 \phi_N(p_D)=(-1)^D N^2=\eta N^2,\qquad
 \boxed{\quad
 [t^K]\phi_N\mathcal M_{\tau,\mathbf n}(f_1(t),\ldots,f_r(t))
  =\begin{cases}
      0,&K<D,\\
      \eta N^2\Theta_{N,D},&K=D .
    \end{cases}\quad}
 \tag{20}
\]
This is an exact coefficient identity for the original full trace,
including all double-root normals, at both parities.

The outer carrier in (19) at \(K=D\) is
\[
                 \lambda_\tau(D)
                   =(-1)^{\tau D}q^{-\tau D(D+1)}=1.
 \tag{21}
\]
Consequently this lowest possible nonzero marked trace coefficient
is independent of the outer sign \(\tau\). The null translation
changes \(K\) by \(-\tau L\), so it is not a summation direction
inside the constraint \(K=D\).

In fact \(\phi_N V_n=\phi_N\) on the entire algebra: degree
preservation and \(\lambda_n(D)=1\) leave its top coefficient
unchanged. Thus a bare closing cannot detect the outer sign.
For an actual ordinary spectator \(g\) of degree \(d\le D\),
the same exact argument instead gives zero when \(K+d<D\), and
\[
 [t^{D-d}]\phi_N\!\left(
   g\,\mathcal M_{\tau,\mathbf n}(f_1(t),\ldots,f_r(t))\right)
       =\eta N^2\,\operatorname{lc}(g)\,\Theta_{N,D-d}.
 \tag{21a}
\]
The spectator remains inside this original trace. Formula (21a)
again fixes one degree and does not control its higher marked terms.

For \(r\ge2\), the remaining coefficients \(N\le K\le rD\)
are still present in the original polynomial in \(t\).
They involve canonical reduction and lower triangular entries
which (6) does not determine. At \(t=1\) they cannot be omitted.
No estimate for their first-normal aliases follows from (16) or
from the completed chirp calculation.

For the actual microscopic endpoint inputs \(f_i=K_N(w_i,Z)\),
their marked amplitudes are exactly
\[
 A_i(k)=\frac{(-1)^ke_k(w_i)}{S_k^2}
       =\frac{\prod_{j<k}(w_i-c_j)}{S_k^4},\qquad
 s_{k+1}^4 A_i(k+1)=(w_i-c_k)A_i(k).
 \tag{22}
\]
The cross-multiplied identity is valid also at complex parameter
zeros, for \(0\le k<D\). For real microscopic \(w_i=2\cosh(\alpha_i/N)\) and bulk
\(k/N\to x\in(0,1)\), it gives
\[
             \frac{A_i(k+1)}{A_i(k)}
                    \longrightarrow\frac1{4\sin^2(\pi x)}.
 \tag{23}
\]
The convergence is uniform on fixed compact bulk intervals and
bounded real parameter sets. In particular the weight difference
in (16) is not automatically a small perturbation of its weight.
An unweighted Gaussian model would remove these exact factorial
amplitudes as well as the high-degree canonical terms.

## 5. Scope and direct sources

The graded quadratic rank loss, shifted linear carrier, finite
binomial identity and exact marked trace coefficient are proved
above. They identify an algebraic mechanism that a source-preserving
analysis of reciprocal resonance must retain. They give no universal
minor nonvanishing, whole-source norm estimate, or contributing
geometric coefficient.

The all-degree triangular formula is already in the first source.
The archived arbitrary-power compilation also explains why the
double-root crossing operator cannot be replaced by a semisimple
finite Gaussian chirp. Nothing here removes those normal channels.

Complete direct sources, with their used identities checked:

* [Full endpoint unit-turn identities](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8:
  original full algebra, signed triangular matrix, Newton pairing
  and the ordinary endpoint coefficients.
* [Terminal-product projective resonance](research_terminal_product_projective_resonance.md),
  SHA256 a648b644c5506e539d14fa715d61a3f680d7d53e48eec8efc1358b6ca047bf08:
  actual inverse-turn sign, reciprocal condition and phase grid,
  with normalization multiplicities distinguished from source data.

Only written mathematics and source-text/hash reads are used.
No mathematical program, numerical experiment, test or build is run.
Adopted notes and public manuscripts are unchanged.
