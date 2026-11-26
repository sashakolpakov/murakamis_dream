# The actual projective occupation quotient and a finite radial continuation

Private written proof, 18 November 2026.

The original reduced first-meridian-jet source admits an exact
compact quotient by its homogeneous phase. The result is a
finite sum of projective periods, with the physical total
occupation, the Cartan twists, and every finite box cap retained.
One can instead retain a single radial generating variable.
Its non-Gaussian factor is a finite polynomial, and its contour can
make arbitrary bounded complex excursions with controlled ends.
This continuation requires no noninteger occupation interpolation.

Each fixed-occupation quotient fixes the common moment and
removes the common diagonal momentum. The whole source still
sums over that moment. A fixed point in one such quotient
can close with a diagonal seam; the remaining moment
stationarity is needed to remove it. In fact the
complete loxodromic geometric point has nonreal total moment,
so it cannot belong to any undeformed physical occupation
level. The radial continuation supplies a legal route in
that variable; it does not identify the geometric component
of the remaining compact angular period.

The complete proof directs are B, R and G, pinned below.
The earlier compact coherent-source and common-framing-gauge
notes were read for coverage. Their common circle symmetry
is not a new claim here. The capped projective kernels,
the closed first-jet quotient, and the finite radial
continuation are proved directly.

## 1. Exact integer sectors, including the caps

Use B's notation
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad d=N-1,\quad r=m-1,\quad
 x_0=-q^{-1},\quad \varepsilon=(-1)^{(N+1)r}.
 \tag{1}
\]
The common meridian \(M\) varies at fixed \(q\).
Assume \(r\ge1\); an empty remaining tensor is a scalar.
Let \(A_L(M)\cdots A_1(M)\) be the actual reduced word
of R, including its original scalar and diagonal factors,
with \(L\ge1\) (insert an identity for the empty word), and let
\[
 T_\ell=\mathcal G^{-1}A_\ell\mathcal G,\qquad
 \mathcal G=G_F^{\otimes r},\qquad
 T=T_L\cdots T_1 .
 \tag{2}
\]
The gauge is the one in B and is independent of \(M\).

Every \(T_\ell\) preserves the exact integer occupation
\(J=\sum_{j=1}^rJ_j\), not only its residue modulo \(N\).
Indeed the physical signed crossing transfers occupation
between its two heads and then flips them; the total is
unchanged. Each term of R's new star lowers its donor by
the same integer that it raises its recipients. Its
inverse has the identical support. The other factors in
R are diagonal. The factorial gauge changes none of
these support statements. They hold throughout the
fixed-root meridian family, and hence for its derivatives.

Put
\[
 I_k=\{a\in\{0,\ldots,d\}^r:|a|=k\},\quad
 V_k=\operatorname{span}\{w_a:a\in I_k\},\quad
 s_k=|I_k|,\qquad 0\le k\le rd .
 \tag{3}
\]
The actual matrices split into these finite blocks.
Write \(T_{\ell,k}\) for the block and
\(t_k(M)=\operatorname{Tr}_{V_k}(T_{L,k}\cdots T_{1,k})\).
No monomial outside the original box is added.

## 2. A compact projective kernel for every capped block

Let \(d\sigma\) be probability surface measure on the
unit sphere in \(\mathbb C^r\), and let \(d\nu\) be
its pushforward to \(\mathbb P^{r-1}\). The latter
is the probability measure on the quotient by the
circle of common phases. For multi-indices of the
same total degree \(k\),
\[
 \int \zeta^a\overline\zeta^{\,b}\,d\sigma(\zeta)
      =\mathbf1_{a=b}\frac{a!}{(r)_k},\qquad
 (r)_k=\frac{(k+r-1)!}{(r-1)!}.
 \tag{4}
\]
Here and below \((r)_0=1\).
For a proof, integrate the independent coordinate
angles in the standard Gaussian integral. Its
monomial moment is \(a!\). In polar coordinates
its radial moment is \((r)_k\), by integration
by parts. The Gaussian integral of one fixes
the surface normalization, giving (4).

For an actual matrix \(A\) on \(V_k\) define
\[
 \mathscr K_{A,k}(\zeta,\eta)
       =(r)_k\sum_{a,b\in I_k}\zeta^a A_{ab}\frac{\eta^b}{b!}.
 \tag{5}
\]
It has degree \(k\) in each argument. Substitution
of (4) proves the exact composition and trace
identities
\[
 \int\mathscr K_{A,k}(\zeta,\overline u)
              \mathscr K_{C,k}(u,\eta)\,d\sigma(u)
                     =\mathscr K_{AC,k}(\zeta,\eta),
 \qquad
 \int\mathscr K_{A,k}(u,\overline u)\,d\sigma(u)
                     =\operatorname{Tr}A .
 \tag{6}
\]
The integrands in the traced product are invariant
under an independent phase at each interface.
They therefore descend to \(d\nu\). Kernels with
different endpoints separately carry their displayed
homogeneous weights; no global choice of unit lift
of a projective point is needed for their closed product.

The identity kernel is the capped polynomial
\[
 \mathscr P_k(\zeta,\eta)
  =(r)_k\sum_{a\in I_k}\frac{\zeta^a\eta^a}{a!}
  =(r)_k[t^k]\prod_{j=1}^r E_d(t\zeta_j\eta_j).
 \tag{7}
\]
Thus the whole finite \(E_d\) cap of B remains.
Only if \(k\le d\) is this the full homogeneous
kernel
\(\binom{k+r-1}{r-1}(\zeta\cdot\eta)^k\).
For larger \(k\), replacing (7) by that expression
would add forbidden physical states. Other occupation
windows are the corresponding subsets of \(I_k\).

For \(r=1\), projective space is a point and
\((1)_k=k!\); all these formulas reduce to the
literal one-dimensional block. At \(k=0\) the
projective integral is still valid, but its
constant kernel provides no positive-moment
symplectic reduction.

## 3. The original closed first-jet source

Define the compact closed integrand
\[
 F_k(M;\zeta)=
 \mathscr K_{T_{L,k},k}(\zeta_0,\overline\zeta_{L-1})
 \cdots
 \mathscr K_{T_{1,k},k}(\zeta_1,\overline\zeta_0),
 \qquad
 t_k(M)=\int_{(\mathbb P^{r-1})^L}F_k(M;\zeta)
                                      \prod_\ell d\nu(\zeta_\ell).
 \tag{8}
\]
For \(L=1\) use the single diagonal kernel. These
are known local factors from the actual reduced
word, rather than a kernel assigned to an unknown
scalar invariant.

The output rotation in B acts on a homogeneous
degree-\(k\) block by \(Q^{\mp k}\). Put
\(\chi_k=x_0^rQ^{-k}\). B's exact source and
residue row become
\[
 \boxed{\quad
 \Phi_0(W(1))=
 \frac1{2\varepsilon}\sum_{k=0}^{rd}
       (\chi_k+\chi_k^{-1})t_k(1)
 +\frac1{2\varepsilon m}\sum_{k=0}^{rd}
       (\chi_k-\chi_k^{-1})t_k'(1),
 \quad}
 \tag{9}
\]
\[
              \sum_{k=0}^{rd}
                  (\chi_k-\chi_k^{-1})t_k(1)=0 .
 \tag{10}
\]
The derivatives are the actual meridian product
rule in (8); the complete Cartan in \(\chi_k\)
is frozen at \(M=1\). Compactness permits
differentiation under the finite integrals.
The original external scalar line is retained
as in B. As there, the first-jet formula requires
the actual intertwining family; an arbitrary
marked nonintertwiner is not promoted to one.

For comparison directly with the original cycle,
write each Bargmann interface as
\(u_\ell=\sqrt{\rho_\ell}\zeta_\ell\).
The phase integrals in B's full product force
all adjacent block degrees to agree. One of
these equalities is redundant around the closed
chain; every circle has probability measure,
so it supplies no extra factor \(N\) or \(2\pi\).
The radial measure is
\[
 d\gamma_{r,N}(\rho)=
       \frac{N^r}{(r-1)!}e^{-N\rho}\rho^{r-1}\,d\rho,
 \qquad
 \int_0^\infty \rho^k\,d\gamma_{r,N}(\rho)
                          =\frac{(r)_k}{N^k}.
 \tag{11}
\]
The factor \(N^k\) in each Bargmann dual is
cancelled by precisely this radial integral.
This derives (8)--(9) by disintegration of the
original cycle, not by choosing a new positive
state or suppressing any cap.

The complement \(a\mapsto d\mathbf1-a\) sends
\(I_k\) to \(I_{rd-k}\), and exactly
\[
                    \chi_{rd-k}=\chi_k^{-1}.
 \tag{12}
\]
This records both total-product eigenvalue
orientations in (9). It proves a bijection
of basis sets and inversion of weights, not
an equality of the two actual block traces.
Moreover distinct integer sectors can have
the same Cartan weight modulo \(N\). No
pairwise cancellation is inferred from the
single residue row (10).

## 4. A single finite radial variable and its legal continuation

Instead of integrating every radial moment,
retain one shared generating variable:
\[
 \mathscr F_{\pm,N}(s,M;\zeta)=
   \sum_{k=0}^{rd}
       \frac{(Ns)^k}{(r)_k}Q^{\mp k}F_k(M;\zeta).
 \tag{13}
\]
This is a finite polynomial in \(s\), with
the original capped projective factors.
Equations (8) and (11) give exactly
\[
 \mathcal I_\pm(M)=
 \int_0^\infty d\gamma_{r,N}(s)
       \int_{(\mathbb P^{r-1})^L}
                      \mathscr F_{\pm,N}(s,M;\zeta)\prod_\ell d\nu.
 \tag{14}
\]
One can obtain this also by integrating the
other \(L-1\) radial variables in the original
disintegration. No value of a factorial or
matrix entry at a noninteger \(k\) is used.
Equation (9), equivalently B's first-jet row,
uses these same two periods and derivatives.

The full density in \(s\) in (14) is entire,
including at zero. Hence its path can be
replaced by any piecewise smooth path from
zero which has a bounded complex excursion
and then agrees with the positive ray.
In particular the path may pass through
any specified finite complex number. A
finite closed contour bounds a domain on
which the density is entire, so Cauchy's
theorem proves equality. The lower endpoint
zero is retained, and the positive end is
unchanged. The same statement holds for
the actual first meridian derivatives.

There is uniform end control, not merely
formal contour equality. In the block
metric \(h_a=a!/(r)_k\), Cauchy--Schwarz
gives the paired estimate
\[
 |\mathscr K_{A,k}(\zeta,\overline\eta)|
 \le\|A\|_{h}\sqrt{\mathscr P_k(\zeta,\overline\zeta)
                         \mathscr P_k(\eta,\overline\eta)}.
 \tag{15}
\]
This metric is a scalar multiple of B's
\(H_a=a!/N^k\) on each block. Thus
\(\|T_{\ell,k}\|_h\le\|T_\ell\|_H\).
The projective integral of \(\mathscr P_k\)
is \(s_k\). Consequently
\[
 \int |F_k|\,d\nu^L
       \le s_k^L\prod_\ell\|T_\ell\|_H .
 \tag{16}
\]
In particular the compact quotient has
only polynomial dimension cost:
\[
 \sum_k s_k^L
 \le(\max_k s_k)^{L-1}N^r
 \le C_{r,L}N^{(r-1)L+1}.
 \tag{17}
\]
The last bound follows by choosing the first
\(r-1\) indices freely; for \(r=1\) it is \(N\).

On the positive radial ray the measure
in (14) times \((Ns)^k/(r)_k\) is precisely
the probability gamma density of shape
\(k+r\) and rate \(N\). Its shape is at most
\(rd+r=rN\). For \(R>r\), the exponential
moment argument used in B, now with
\(\theta=1-r/R\), gives
\[
 \int_R^\infty
       \frac{(Ns)^k}{(r)_k}\,d\gamma_{r,N}(s)
 \le e^{-NJ_r(R)},\qquad
 J_r(R)=R-r-r\log(R/r).
 \tag{18}
\]
Indeed the bound is
\(e^{-\theta NR}(1-\theta)^{-(k+r)}\);
use \(k+r\le rN\). Combining (16)--(18)
with B's actual local-word bound
\(\prod\|T_\ell\|_H\le N^p e^{CN}\)
proves an arbitrarily strong exponential
radial tail by choosing one fixed large
\(R\). Fixed meridian derivatives cost
only the recorded polynomial factors.
Bounded contour excursions do not alter
these ends.

They have a recorded exponential bound
as well. On \(|s|\le A\), use
\((r)_k\ge k!\), (16), and
\(e^{-N\operatorname{Re}s}\le e^{NA}\).
After integration of the projective
variables, the absolute density is
at most a fixed power of \(N\) times
\(\exp((C+2A)N)\). A fixed finite
excursion therefore keeps a finite
exponential cost; it is not assigned
the representation-volume rate.

This is a continuation of one actual
finite source polynomial and its full
pairing. It is not an analytic
interpolation of separate occupation
blocks. Passing the radial path through
a desired value does not prove a
stationary point or its coefficient.

## 5. The diagonal gauge, its moment, and the geometric obstruction

The exact diagonal scaling on all remaining
heads is \(w_a\mapsto c^{|a|}w_a\).
In B's Bargmann variables its covariance
is
\[
                         z\mapsto cz,\qquad w\mapsto c^{-1}w .
 \tag{19}
\]
Every actual local matrix commutes with it.
On the elementary physical chart proved
in B,
\[
 A_j=e^{c_0z_jw_j},\quad f_j=z_j,\quad
 p_j=(1-A_j)/z_j,\qquad c_0=2\pi i.
 \tag{20}
\]
Thus (19) is precisely common momentum
scaling \(p_j\mapsto c^{-1}p_j\), with
the inverse convention for the parameter.
It is not the eliminated additive
centralizer direction.

The moment for (19), with the holomorphic
form \(\sum dz_j\wedge dw_j\), is
\[
 \mu=\sum_jz_jw_j
      =c_0^{-1}\sum_j\Log A_j .
 \tag{21}
\]
The sign follows by contracting with
\(\sum(z_j\partial_{z_j}-w_j\partial_{w_j})\),
which gives \(d\mu\). On \(\mu\ne0\)
the quotient of \(\{z\cdot w=\mu\}\)
by this \(\mathbb C^*\) is locally
parametrized by the projective lines of
\(z,w\), with their incidence nonzero.
Conversely any such pair of lines has
representatives with \(z\cdot w=\mu\),
unique up to (19). On \(z_1\ne0\),
set \(z_1=1\) and
\(w_1=\mu-\sum_{j>1}z_jw_j\); the
remaining pairs give the reduced
holomorphic form directly. Its real
positive level has \(w=\overline z\),
\(|z|^2=\mu\), and quotient
\(\mathbb P^{r-1}\).

The exact homogeneous block has the
Euler identity \(z\cdot\partial_z=k\).
Its physical normalized moment is
\(\mu=k/N\). The gamma mean in (11)
after the degree-\(k\) weighting is
\((k+r)/N\); this finite normal shift
is not deleted by asserting an exact
radius \(k/N\). The projective quotient
removes the phase, while the sum in
(9), or the radial variable in (14),
retains the moment.

Equation (20) is a controlled kernel
principal statement only on B's stated
small-product chart. On other resolved
charts we use G's physical logarithmic
coordinates and the same exact diagonal
action, not an unproved whole-kernel
asymptotic. G proves that on the
resolved total-lowering-zero level
\[
 K_\Sigma=x_{\rm cl}K_{\rm r},\qquad
 K_{\rm r}=x_{\rm cl}^{\,r}
                  \exp\left(-\sum_j\Log A_j\right),
                   \qquad x_{\rm cl}=-M.
 \tag{22}
\]
Its remaining common momentum is exactly
the diagonal framing direction.
Consequently each projective block
removes that direction at a specified
moment. The full sum (9) does not
select a value of (22).

There is a further distinction between
a fixed point in a fixed-moment
quotient and G's full occupation
gradient. A projective fixed point
can lift to
\[
                 R_\beta(z)=D_c\cdot z,
                 \qquad p_j'=c\,p_j ,
 \tag{23}
\]
where \(D_c\) is common diagonal
scaling. It need not have \(c=1\).
On a regular marked logarithmic
coefficient chart, G's primitive
has differential
\[
 d\mathcal S=\sum_{\rm out}\log p_j'\,d\Log A_j'
                         -\sum_{\rm in}\log p_j\,d\Log A_j .
\]
After solving its internal equations
at fixed \(\mu\), the positions close,
and their momentum mismatch in (23)
is the same at every head. Hence,
with \(\phi=\mathcal S/c_0\),
\[
                         d\phi=\log(c)\,d\mu .
 \tag{24}
\]
The logarithm here includes the
actual assigned Fourier covector
and its sheet. Equivalently, the
annihilator of variations with
\(\sum d\Log A_j=0\) consists of
the common covector; varying that
sum tests its remaining coefficient.
Thus full occupation stationarity
requires this last coefficient to
vanish. Its exponentiated consequence
is \(c=1\), while the additive
equation retains the recorded
Fourier branch. This is the
remaining diagonal seam equation,
not another quotient direction.

The shared radial formula retains
this distinction. Before making
any asymptotic claim it obeys the
exact integration-by-parts row
\[
 \int_0^\infty d\gamma_{r,N}(s)
 \sum_k \frac{(Ns)^k}{(r)_k}Q^{\mp k}
                         (k+r-Ns)F_k=0 ,
 \tag{25}
\]
also after the compact integrations.
Indeed each summand is the derivative
of \(s\) times its density in (14);
both endpoints vanish. The same
identity holds on the continued
path and for the meridian derivatives.

For the principal interpretation,
let \(k/N=\eta\) stay in a compact
positive interval and let \(s\ne0\)
have a recorded logarithm. The
radial factor in (14) has logarithm
\[
 N\{\eta\log(s/\eta)+\eta-s\}+O(\log N).
 \tag{26}
\]
This follows directly from
\(\log k!=k\log k-k+O(\log k)\),
proved by bounding the sum of
\(\log j\) between its adjacent
integrals; the fixed \(r\) shifts
change only the stated error.
No noninteger matrix coefficient
has been used. If a separately
justified local contribution admits
a differentiable phase
\(\phi(\eta,\ldots)\), the joint
radial and moment critical rows
therefore have the principal form
\[
 s=\eta,\qquad
 \partial_\eta\phi+\log(s/\eta)=0 .
 \tag{27}
\]
At \(s=\eta\), the second row is
exactly the missing equation (24).
A change of radial log sheet must
be accompanied by its Fourier
branch; it is not silently removed.
Equation (27) describes what a
valid local saddle comparison must
prove. It does not interpolate
the finite \(k\) sum or assert
that such a contribution exists.
G's isolated resolved fixed germ,
under its positive gluing premise,
concerns the full equation with
this seam removed, not arbitrary
fixed-moment projective fixed points.

There is a concrete obstruction to
finding it on one undeformed physical
moment level. Use R's source-preserving
presentation for which the complete
total product is regular semisimple,
and suppose the representation is
complete discrete faithful. G proves
that this product is loxodromic. At
total lowering zero its two eigenvalues
are \(K_\Sigma,K_\Sigma^{-1}\), both
of modulus different from one. But
on any physical sequence \(k/N\to\eta\)
with real \(\eta\in[0,r]\), equations
(21)--(22) at \(M=1\) give
\[
              |K_{\rm r}|=|K_\Sigma|=1 .
 \tag{28}
\]
Equivalently the exact block Cartan
weight \(\chi_k\) has modulus one at
every \(N\). Complexifying only the
projective angular coordinates at
that fixed moment cannot change this
scalar constraint.

Thus both geometric total-product
eigenline choices have nonreal
\(\mu_*=c_0^{-1}\sum\Log A_j\).
Integer log-deck shifts change only
its real part and do not remove this
obstruction. Formula (14) now supplies
a legal finite-source radial path
through \(\mu_*\) without inventing
complex physical indices. The compact
angular cycle, its caps and its
possible cancellation remain in that
same formula. There is no conclusion
that its geometric component occurs.

## 6. Scope and complete proof-source pins

The exact quotient (9) and continuation
(14) retain every original local matrix,
every finite box projector, both Cartan
weights and the entire first-meridian
product rule. They remove the redundant
circle and expose the still necessary
complex total moment. They neither
identify a uniform phase for the full
projective kernels nor select an
angular geometric cycle. Quantum
normals away from the root, arbitrary
marked Ward defects, and the compact
geometric coefficient require their
original additional source data.

* B: notes/research_reduced_word_bargmann_source_period.md,
  SHA256 abbe118e89f2d80f82f4bcd591a71dc193fda852cd488262461d07b262696655.
* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

All three complete directs were freshly read nontruncated
in the active author sequence. Every used implication
was checked. Only written proofs and text operations
were used; frozen and public files were not edited.
