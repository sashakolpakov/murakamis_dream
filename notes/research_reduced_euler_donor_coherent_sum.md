# A finite donor coherent sum for the reduced Euler star

Private written proof, 18 November 2026.

The actual lower-donor kernel can be summed over its integer
donor index, using a specified finite factorial coherent vector.
At the physical imaginary quantum parameter this gives a
nonzero coherent Gaussian kernel on the \(O(\sqrt N)\) coherent
scale. The linear characteristic may vanish. No interpolation
in a complex donor occupation is used.

The donor truncation has a superexponentially small relative
error. The recipient projectors have such an error only under
an explicit macroscopic upper margin. They remain exact outside
that margin. A nonzero local matrix kernel is not a nonzero
closed source coefficient.

The sole complete proof direct is W, the exact Euler-star word
kernel. All additional graph, generating-function, and tail
arguments are proved here.

## 1. The specified finite coherent input

Retain W's notation
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 h=2\pi i/N,\quad x=-M/q,\quad
 f_a=(Q;Q)_a,\quad G_Fw_a=f_aw_a,
 \tag{1}
\]
with \(N\ge2\), \(M\ne0\), and \(r\ge2\) heads.
Let \(\mathcal G=G_F^{\otimes r}\), and fix the actual integer
recipient input \(b=(b_2,\ldots,b_r)\), \(0\le b_j\le d\).
On the donor use the exact finite vector
\[
              \psi_N(\lambda)
                   =G_F\sum_{a=0}^d\frac{\lambda^a}{a!}w_a.
 \tag{2}
\]
The recipient inputs in this same presentation are \(G_Fw_{b_j}\);
if their original basis is used instead, the corresponding
nonzero \(f_{b_j}\) factors must be retained.

Let \(\Lambda_z\) evaluate normalized basis monomials
\(w_{a_0}\otimes w_{a_2}\otimes\cdots\) at
\(z_0^{a_0}\prod_{j=2}^rz_j^{a_j}\). The exact matrix kernel is
\[
 \Lambda_z\mathcal G^{-1}S_r^{\pm1}
          \left(\psi_N(\lambda)\otimes
                        \bigotimes_{j=2}^rG_Fw_{b_j}\right)
       =\left(\prod_{j=2}^rz_j^{b_j}\right)
                         \mathcal C_{N,b}^\pm(\lambda,z).
 \tag{3}
\]
Here W's word polynomial \(K_a^\pm\) gives
\[
 \mathcal C_{N,b}^\pm
       =P_b\sum_{a=0}^d\frac{\lambda^a}{a!}K_a^\pm.
 \tag{4}
\]
The exact operator \(P_b\) deletes a recipient monomial
with transfer degree \(n_j>d-b_j\). The factor outside
\(\mathcal C\) in (3) is not discarded.

Differentiating (3) \(a\) times in \(\lambda\) at zero
recovers the corresponding actual donor column, with its
specified factorial basis factors. Thus (2)--(4) are a finite
kernel presentation, not a replacement for the original cut
or a choice of a new preferred source vector.

## 2. The word extension and its entire generating function

For the ordered alphabet \(\mathcal J=\{0,2,\ldots,r\}\), put
\[
 c_0=z_0,\qquad
 c_j=x^{-(j-1)}Q^{\sum_{2\le i<j}b_i}z_j\quad(j\ne0).
 \tag{5}
\]
For the positive sign use \(c_j^+=c_j\). For the negative
sign use \(c_0^-=c_0\), \(c_j^-=-c_j\) for \(j\ne0\).
The pair energies are
\[
 B_+(j,k)=\boldsymbol1_{\{j>k\}},\qquad
 B_-(j,k)=\boldsymbol1_{\{j>k\}}
                     +\boldsymbol1_{\{j\ne0,\ k\ne0\}}.
 \tag{6}
\]
Each is a real integer between zero and two. W proves,
for every physical \(0\le a\le d\),
\[
 K_a^\pm=
 \sum_{\ell\in\mathcal J^a}\prod_{i=1}^ac_{\ell_i}^\pm
                 \exp\!\left(h\sum_{i<j}B_\pm(\ell_i,\ell_j)\right).
 \tag{7}
\]
Use the right side to define auxiliary polynomials also for
\(a>d\). These are bookkeeping polynomials, not extra physical
head states or values of a factorial ratio at its root zero.

We prove the analytic statement for one sign, writing \(c,B\).
Set
\[
 C_0=\sum_j|c_j|,\qquad H=\sum_jc_j,\qquad
 A=\sum_{j,k}c_jc_kB(j,k).
 \tag{8}
\]
At the physical imaginary \(h\), every exponential in (7)
has modulus one. Hence
\[
                         |K_a|\le C_0^a.
 \tag{9}
\]
In particular
\[
                 \mathcal E_h(\lambda;c)
                  =\sum_{a=0}^\infty\frac{\lambda^a}{a!}K_a
 \tag{10}
\]
is entire in \(\lambda\). No condition \(H\ne0\) is needed.
We will compare the actual finite polynomial (4) to (10)
with its exact tails retained.

## 3. A connected-graph identity with unit extra-edge factors

For a fixed set of \(s\) ordered sites and fixed labels
\(\ell_1,\ldots,\ell_s\), write
\[
 u_{ij}=e^{hB(\ell_i,\ell_j)}-1,\qquad i<j,\qquad
 v=\max_{j,k}|e^{hB(j,k)}-1|\le2|h|.
 \tag{11}
\]
Let \(w_s\) be the sum over all connected graphs on these
sites of \(\prod_{\{i,j\}\text{ edge}}u_{ij}\), followed by
the finite label sum weighted by \(\prod_i c_{\ell_i}\).
For \(s=1\), define \(w_1=H\).

We need a bound that keeps the cancellations among extra
edges. Root each connected graph at site \(1\), and let
its levels be the graph distances from that root.
For each other vertex select its smallest-labeled neighbor
in the preceding level as parent. This gives a rooted tree
\(T\). Define \(R(T)\) by adjoining to \(T\):

* every edge between two vertices in the same level;
* an edge between adjacent levels when its vertex in the
  preceding level has label at least that of the selected
  parent of the later-level vertex.

Every graph producing \(T\) lies between \(T\) and \(R(T)\).
Conversely every graph in that interval has exactly these
levels and selected parents. Indeed an added edge changes
level by at most one, so it cannot shorten a path to the
root below the tree level; tree paths attain that level.
The parent condition preserves the smallest preceding-level
neighbor. These intervals therefore partition the connected
graphs, without overlap.

For arbitrary complex edge variables this proves the exact
polynomial identity
\[
 \sum_{\text{connected graphs }G}\prod_{e\in G}u_e
   =\sum_{\text{rooted trees }T}
          \left(\prod_{e\in T}u_e\right)
          \left(\prod_{e\in R(T)\setminus T}(1+u_e)\right).
 \tag{12}
\]
There is no inequality or positivity assumption in (12).
At imaginary \(h\), each extra-edge factor has modulus one.
The number of rooted trees is at most \(s^{s-1}\), by assigning
a parent to each non-root vertex. Taking absolute values
only after (12), and then summing labels, gives
\[
                  |w_s|\le C_0^s s^{s-1}v^{s-1}
                              \qquad(s\ge2).
 \tag{13}
\]
This is where the physical ray is used. Bounding each
extra edge by \(1+|u_e|\) before summation would not give
the convergent estimate needed below.

## 4. Exact exponential generating function and its logarithm

Expand the pair factors in (7) into graphs and group every
graph into its connected components. A component on an ordered
subset \(S\) has weight \(w_{|S|}\). This assertion uses order:
the increasing relabeling \(S\to\{1,\ldots,|S|\}\) preserves
which endpoint of each pair comes first. The energies (6)
are not replaced by symmetric label functions.

If a partition has \(m_s\) components of size \(s\), the number
of such partitions is
\(a!/\prod_s((s!)^{m_s}m_s!)\).
Consequently, as formal power series at \(\lambda=0\),
\[
 \sum_{a\ge0}\frac{\lambda^a}{a!}K_a
                   =\exp\left(\sum_{s\ge1}
                                         \frac{\lambda^s}{s!}w_s\right).
 \tag{14}
\]
This also proves the normalization of the singleton term:
it is \(\lambda H\), not a scalar-normalized replacement.

The connected series converges whenever
\[
                         \theta=e|\lambda|C_0v<1.
 \tag{15}
\]
For example \(s^{s-1}/s!\le e^s\), obtained from the elementary
integral lower bound for \(\log(s!)\), makes its absolute
tail a geometric series. Both sides of (14) are analytic
there and have identical Taylor series, so equality holds.
In particular \(\mathcal E_h\ne0\) on (15), and its
holomorphic logarithm with value zero at \(\lambda=0\)
is exactly the connected series. This conclusion holds
even at \(H=0\).

The two-site term is
\[
                  w_2=\sum_{j,k}c_jc_k(e^{hB(j,k)}-1).
 \tag{16}
\]
Taylor's formula along the imaginary segment gives
\[
                         |w_2-hA|\le2C_0^2|h|^2.
 \tag{17}
\]
For \(\theta\le1/2\), (13) bounds the remaining terms by
\[
 \sum_{s\ge3}\frac{|\lambda|^s}{s!}|w_s|
          \le 2e^3|\lambda|^3C_0^3v^2.
 \tag{18}
\]
Thus the exact connected logarithm satisfies
\[
 \boxed{\quad
 \log\mathcal E_h
    =\lambda H+\frac{h\lambda^2}{2}A
       +O_{C_0}\bigl((|\lambda|^2+|\lambda|^3)|h|^2\bigr).
 \quad}
 \tag{19}
\]
For any fixed \(C\) and \(|\lambda|\le C\sqrt N\), (15)
holds for all sufficiently large \(N\) on compact bounded
coefficient sets, and
\[
 \mathcal E_h
   =\exp\left(\lambda H+\frac{h\lambda^2}{2}A\right)
                                      (1+O(N^{-1/2})).
 \tag{20}
\]
All actual \(N\)-dependent coefficients in (5), including
the half-shifts in \(x=-M/q\), remain in \(H,A\).
No principal substitution has removed them.

## 5. Relative control of the finite donor and recipient tails

Fix a compact coefficient neighborhood with \(C_0\le C_*\),
and \(|\lambda|\le C\sqrt N\). Put \(D_*=|\lambda|C_*\).
For an integer \(L\ge2D_*\), successive terms give
\[
 \sum_{a=L}^\infty\frac{D_*^a}{a!}
            \le 2\frac{D_*^L}{L!}
            \le2\left(\frac{eD_*}{L}\right)^L.
 \tag{21}
\]
The factorial bound follows by integrating \(\log t\);
no asymptotic factorial formula is needed.

Let the finite unprojected donor polynomial be
\[
                       \mathcal E_{N}^{\rm fin}
                            =\sum_{a=0}^d\frac{\lambda^a}{a!}K_a.
 \tag{22}
\]
Equations (9),(21), with \(L=N\), show that its difference
from (10) is at most
\[
                 \exp\left(-\tfrac12N\log N+O(N)\right).
 \tag{23}
\]
On the other hand the exponential on the right of (20)
has modulus at least \(e^{-C_1\sqrt N-C_2}\), uniformly.
Indeed \(|H|\le C_*\) and \(|A|\le2C_*^2\).
Thus (23) is also a superexponentially small relative error.
The finite unprojected donor kernel is nonzero for all
sufficiently large \(N\), with the same estimate (20).

For the recipient projector set
\[
                   L_b=1+\min_{j\ge2}(d-b_j)
                             =N-\max_{j\ge2}b_j.
 \tag{24}
\]
A word deleted by \(P_b\) has at least \(L_b\) nonzero
letters of some recipient type, hence has length at least
\(L_b\). Taking absolute values of just those deleted
monomials and using (9) bounds the change in (22) by
the left side of (21) with \(L=L_b\).
If the actual input satisfies
\[
                       d-\max_{j\ge2}b_j\ge\eta N,
                              \qquad \eta>0\ \text{fixed},
 \tag{25}
\]
this error is at most
\[
                     \exp\left(-\tfrac\eta2N\log N+O(N)\right).
 \tag{26}
\]
It is again superexponentially small relative to the
nonzero factor in (20).

Consequently the actual factored kernel (4), under (25),
satisfies for either sign
\[
 \boxed{\quad
 \mathcal C_{N,b}^\pm
  =\exp\left(\lambda H_\pm+
                       \frac{h\lambda^2}{2}A_\pm\right)
                                      (1+O(N^{-1/2})),
       \qquad |\lambda|\le C\sqrt N .
 \quad}
 \tag{27}
\]
It is nonzero for all sufficiently large \(N\), including
when \(H_\pm=0\). The full matrix kernel has the additional
exact monomial in (3); its nonvanishing also requires that
monomial to be nonzero. At \(\lambda=0\), the factored
kernel is exactly one.

All these bounds hold on slightly larger complex coefficient
neighborhoods with the same bound \(C_*\). Cauchy estimates
therefore give the same \(O(N^{-1/2})\) bound for every fixed
derivative of the normalized error in the coherent variables
and in \(M\) at fixed \(q\). This includes derivatives in the
scaled donor variable \(\tau=\lambda/\sqrt N\) on fixed compact
sets. The integer occupations \(b_j\), and hence their projector
thresholds, remain fixed when taking those derivatives.

## 6. What the coherent sum transports

The donor index was summed with every coefficient of the
specified finite vector (2). It was not analytically continued
to a complex value. Formula (7) beyond \(a=d\) was used only
to prove the tail estimate; it is not a new infinite head.

The unitary extra-edge estimate in (12)--(13) uses imaginary
\(h\). No zero-free neighborhood in a complex quantum parameter
or shortcut for closed quantum normals follows. The actual
meridian dependence in (1),(5) remains holomorphic and is
included in the stated fixed-\(q\) derivative estimates.

If the upper margin (25) fails, the exact formula (4) still
holds, but this proof does not approximate its projected
value by (20). In particular upper recipient sectors may
change or cancel the kernel. The original source can require
such sectors; they are not discarded by their absence from
the estimate. Nor does (27) estimate a donor sector near
\(a=d\) before the coherent sum.

The original recipient clocks are \(Q^{b_j}\). Holomorphic
coefficient parameters in (5) do not prove an interpolation
in complex recipient occupations, or produce a physical
integer sequence approaching arbitrary complex clocks.
The resolved principal identification in W remains a
separate statement about the correspondence.

Finally every factorial basis change, neighboring operator,
Cartan factor, pivot, scalar line and closing first-jet
functional must remain in a full word. The map (3) retains
them by transporting the source and dual along with the
matrix. A local nonzero kernel, even one proved by an exact
complex-weighted sum, does not imply noncancellation of
their subsequent contraction or a geometric cycle coefficient.

## Coverage and complete proof source

The graph interval partition is a standard cluster-expansion
technique; the primary abstract of
[Fernández--Procacci](https://arxiv.org/abs/math-ph/0605041)
was checked for coverage of the Penrose tree identity.
No external theorem is used in the proof above. The
source-specific result is the exact Euler-star coherent
sum with its original finite truncations and relative tails.

* W: notes/research_reduced_euler_star_complex_word_kernel.md,
  SHA256 6baac1f8303d21be4a5c3f6c809795272dd51d3e0060e13843e0f25958902fdb.

The complete source was freshly read nontruncated in this
active sequence and retained unchanged. Every used implication
was checked. Only written mathematics and text/hash operations
were used; frozen and public files were not edited.
