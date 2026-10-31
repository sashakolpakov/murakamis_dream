# The finite cut average: exact resonance, a source obstruction, and a leading criterion

Independent calculation, 27 October 2026. The Euler--Maclaurin
operator is exact in its proper domain. Constancy of the geometric
action and its nonzero principal density nevertheless do not, by
themselves, determine the leading actual finite cut. This note
gives a counterexample using the same canonical finite source,
not a change of period functional, and an analytic criterion that
would suffice to obtain its nonzero leading coefficient.

## 1. The exact averaging operator and its resonances

Write \(A=e^u\), \(D=\partial_u=A\partial_A\),
\(H=2\pi i/N\), and
\[
 \mathcal E_N(D)=\frac1N\sum_{j=0}^{N-1}e^{jHD}.
\]
As an entire function of a scalar spectral variable \(\lambda\),
\[
 \mathcal E_N(\lambda)
 =\frac{e^{2\pi i\lambda}-1}{N(e^{H\lambda}-1)},               \tag{1.1}
\]
with all removable values retained. On polynomials in \(u\),
\(D\) is nilpotent, and the exact finite Taylor identity is
\[
 \mathcal E_N(D)=
 \frac{HD}{e^{HD}-1}\,
 \frac{e^{2\pi iD}-1}{2\pi iD}.                              \tag{1.2}
\]
The second factor is the continuous logarithmic average.

On Laurent powers the multipliers are instead
\[
 \mathcal E_N(A^k)=\begin{cases}A^k,&N\mid k,\\0,&N\nmid k,\end{cases}
\quad
 \mathcal C(A^k)=\int_0^1(e^{2\pi it}A)^kdt
 =\begin{cases}1,&k=0,\\0,&k\ne0.\end{cases}                  \tag{1.3}
\]
The \(1\) in the second display denotes its constant-function
action. In particular \(\mathcal C(A^N)=0\) but
\(\mathcal E_N(A^N)=A^N\). Therefore no linear operator \(B\)
on all Laurent polynomials satisfies
\(\mathcal E_N=B\mathcal C\). The meromorphic factors in (1.2)
are not separately composable there: at \(kN\ne0\), one has
the essential zero/pole cancellation in (1.1).

On the canonical band \(1,A,\ldots,A^{N-1}\), the finite average
at \(A=1\) and the logarithmic residue coincide exactly:
\[
 \boxed{\phi_N(f)=\frac1N\sum_{a=0}^{N-1}f(Q_N^a)
       =[A^0]f=\operatorname{Res}_{A=0}f(A)\frac{dA}{A}.}       \tag{1.4}
\]
No asymptotic Euler correction is needed on this band.
It does not follow that the Bernoulli factor is uniformly
\(1+O(H)\): at frequency \(N-1\), its modulus is of order \(N\).

In the whole normal order \(A^N=U\), an unreduced \(A^N\) gives
the canonical constant \(U\). Formula (1.4) must be applied
after this carry. It cannot be applied to the unreduced
ordinary Laurent expression and then used to delete \(U\).

## 2. A canonical, pole-free counterexample with the actual cut

For \(N\ge3\), set
\[
 \boxed{f_N(A)=1-A^{N-1}-(1-A)^{N-1}.}                       \tag{2.1}
\]
It is already a canonical polynomial of degree at most \(N-1\).
It has \(f_N(0)=f_N(1)=0\). Consequently
\[
 \boxed{\phi_N(f_N)=0,\qquad
 \phi_{S,N}(f_N)=
 \frac{N\phi_N(f_N)-f_N(1)}{N-1}=0,}                         \tag{2.2}
\]
for both the original finite source and the repaired source
which deletes \(A=1\).

On every compact lens
\[
 |A|\le r<1,\qquad |1-A|\le r<1,
\]
one has, for each fixed derivative order \(k\),
\[
 \partial_A^k(f_N-1)=O_k(N^k r^{N-1-k}).
\]
Thus \(f_N\) has the normalized local asymptotic series
identically \(1\), to every order in \(1/N\), on a nonempty
open chart. Its local action is zero and its principal
amplitude is the nonzero constant \(1\). There are no poles.

At completeness the actual density is, up to its nonzero
frame-independent torsion/base line,
\[
 \Omega_{\mathrm{cut}}=dt\wedge d\log A.
\]
Multiplying it by \(f_N(A)\) and taking the already marked
relative interval \(t=0,1\), with zero endpoint co-sources,
still gives the same nonzero local principal density to all
orders. The relative transgression is exactly \(f_N\,d\log A\).
Both finite cut pairings of it are nevertheless zero by (2.2).

The example also has formally closed local Ward jets. On a
slightly smaller lens, \(Q_NA\) stays in the same larger lens,
so \(f_N(Q_NA)-f_N(A)\) is exponentially small with every
fixed derivative. Diagonal \(K\)-commutation is exact, and
the adjacent \(E,F\) Ward differences are flat there.
They are not exact global Ward identities.

This is not an actual knot state or a second coherent
rational-\(Q\) unfolding. It proves that canonical degree,
absence of poles, exact source normalization, all local
asymptotic jets, and formal residual Ward closure do not
imply the desired source survival. It does not contradict
scalarity of the actual complete cut, nor an exact global
Ward/source chain map if one is constructed.
Its failure is concrete: outside the local lens its norm
can be exponential, and the global source sees the resulting
cancellation.

## 3. A functional leading-source theorem

The following is a sufficient globalization statement whose
hypotheses can be checked on functions rather than at individual
levels.

Let \(\mathcal D\subset\mathbb C^\times\) be connected and contain
a nonempty geometric chart \(\mathcal U\) and a circle
\(\Gamma_\rho=\{|A|=\rho\}\) around zero. Suppose:

1. \(F_N\) is a canonical polynomial of degree \(<N\).
2. \(F_N\) is locally polynomially bounded on \(\mathcal D\):
   for each compact \(K\subset\mathcal D\),
   \(\sup_K|F_N|\le C_KN^{d_K}\), with \(d_K\) independent of \(N\).
3. On \(\mathcal U\), it has a complete uniform asymptotic
   expansion \(F_N\sim\sum_{j\ge0}N^{-j}F_j\), where every
   \(F_j\) is holomorphic on the same \(\mathcal D\).
4. \(F_0=c\ne0\) is the geometric constant after the retained
   action, torsion and base-only lines have been factored out.

Then the expansion propagates to compact subsets of
\(\mathcal D\), and
\[
 \boxed{\phi_N(F_N)=c+O(N^{-1}).}                            \tag{3.1}
\]

Here is a direct proof of the propagation. On three concentric
disks with radii \(r<\rho<R\), the maximum principle on an
annulus gives
\[
 M(\rho)\le M(r)^\theta M(R)^{1-\theta},\quad
 \theta=\frac{\log(R/\rho)}{\log(R/r)}>0.
\]
It follows by applying the maximum principle to
\(\log|f|\) minus the radial harmonic interpolation of its
two boundary bounds. A finite chain of overlapping disks
therefore propagates an \(O(N^{-m})\) local error to
\(O(N^{-m\theta_*+d_*})\), for fixed
\(\theta_*>0,d_*\).

Apply this to
\(F_N-\sum_{j<m}N^{-j}F_j\). Its global bound has a polynomial
exponent independent of \(m\), since each fixed truncation is
bounded on a compact set. Choosing \(m\) large proves any
desired target order. Compactness gives uniformity on
\(\Gamma_\rho\). Equation (1.4) and the residue integral
then give (3.1). This proof uses no asymptotic expansion of
the Bernoulli operator.

The theorem also applies to a relative density with coefficients
depending on \(t\), if these bounds are uniform on the marked
interval and its endpoint co-sources and the coefficient
functions extend on a common domain. The relative source
then remains the full integral-minus-endpoints functional.
For the root-deleted source, its additional term \(F_N(1)/(N-1)\)
must also be controlled or compensated by its retained Ward
homotopy; deletion alone is not that estimate.

Alternatively, an exponentially small local error and a
subexponential global bound suffice by the same disk argument.
Local formal expansions without either global bound do not.

## 4. The deleted-root boundary layer has an explicit size test

Deleting \(A=1\) removes the point, not its neighboring sampled
values. For a fixed meromorphic coefficient with pole order
\(p\) at \(1\), assume
\[
 |r(A)|\le C|1-A|^{-p}
\]
on the sampled circle away from that point. The elementary
bound \(|1-Q_N^a|\ge4\min(a,N-a)/N\) gives
\[
 \frac1{N-1}\sum_{a=1}^{N-1}|r(Q_N^a)|
 =\begin{cases}
 O(1),&p=0,\\
 O(\log N),&p=1,\\
 O(N^{p-1}),&p>1.
 \end{cases}                                                \tag{4.1}
\]
Thus an \(H^j r(A)\) loop term need not be small after averaging
if \(p\ge j+1\). A proof of suitable pole-order bounds and a
global remainder estimate could establish leading source
control. Merely knowing that each loop coefficient is rational
on the geometric chart does not give either bound.

## 5. Consequence for the proposed geometric source map

The constant action on the \(B_1\)-torsor and
\(\Omega_{\mathrm{geom}}=\text{nonzero constant}\cdot\Omega_{\mathrm{cut}}\)
correctly identify the **local** candidate coefficient. The
specified relative geometric interval would pair it to that
nonzero constant. The exact finite averaging identity does
not show that the actual canonical source is that relative
class after transverse elimination.

The missing comparison must preserve the resonant/carry data
and exclude the concrete cancellation in section 2. A global
tempered function theorem of the form in section 3, or an exact
source chain map with a nonzero leading projection, would do so.
Neither follows from the present local principal-density
identity or the formal residual Ward operators alone.
