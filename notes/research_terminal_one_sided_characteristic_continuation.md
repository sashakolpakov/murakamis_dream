# A common slow baseline and exponentially small terminal window interface

Private written proof, 16 November 2026.

One-sided interpolation of polynomially bounded physical jets is
already available. Its real interface need not be small. The added
result here is a common holomorphic slow baseline for the actual bare
terminal, continued through a specified regular characteristic
domain. The two exact one-sided representatives differ from that
baseline by exponentially small corrections on their respective
half-domains. Their original real interface consequently has a
quantified exponential saving.

The complex-domain hypotheses concern the original finite-shift
coefficients and the selected double characteristic. They are not
asserted for every parent height. All exterior window currents and
the original remaining spectator are retained.

## 1. The source and the complex-domain criterion

Fix \(|n|\ge2\), \(h=N^{-1}\), \(q=e^{\pi i/N}\),
\(\eta=(-1)^{N-1}\), and the actual terminal polynomial
\[
 G_N(Z)=T(R^n)(Z),\qquad x_j=(j+\tfrac12)h,
 \quad c(x)=2\cos(2\pi x).
 \tag{1}
\]
Use precisely the normalization of the bulk scalar-compatibility
source:
\[
 {\cal S}(x)=S_n(\pi-2\pi x),\quad
 p(x)=(\sin2\pi x)^{-1/2},\quad f_h=p e^{{\cal S}/h},
\]
\[
 a_j=f_h(x_j)^{-1}G_N(c(x_j)),\qquad
 b_j=f_h(x_j)^{-1}c'(x_j)G_N'(c(x_j))
             -({\cal S}'/h+p'/p)(x_j)a_j.
 \tag{2}
\]
The original carrier and signed phase constant are unchanged.
The normalized scalar operator is
\[
 P_h=f_h^{-1}(\widetilde D_{-n}-c_0)f_h
       =\sum_{k=-m}^m a_{k,h}(x)E^k,
 \quad m=|n|,\quad E u(x)=u(x+h),\quad c_0=q+q^{-1}.
 \tag{3}
\]
Its physical value and differentiated normal rows are exact; its
ordinary source residual is still the specified multiple of \(P_N\).

Let \(I\Subset J\Subset(0,1/2)\) be fixed real intervals. The
following is a sufficient complex continuation criterion.

Choose bounded simply connected domains
\[
 \overline\Omega_1\subset\Omega_2,\qquad
 \overline\Omega_2\subset\Omega_3,
 \qquad J\subset\Omega_1,
 \tag{4}
\]
with strictly positive distances between the indicated boundaries.
They have a common real base point in \(J\). Require a fixed bound
on the lengths of paths within each domain from that base point
to its other points. This makes the fundamental-matrix bounds below
explicit; ordinary rectangles and suitable finite disk chains have
this property. The target complex contour must lie in a fixed
compact subset of \(\Omega_1\).

On a neighborhood of \(\overline\Omega_3\), require:

1. The continued original \({\cal S}\) and the chosen \(p\) are
   holomorphic, with \(p\) a unit, and agree with (2) on \(J\).
2. The ordinary finite-shift coefficients in (3) are holomorphic
   and uniformly bounded for small \(h\), with bounded inverse
   extreme coefficients and the usual holomorphic small-\(h\)
   expansions. All fixed derivatives on smaller domains are bounded.
3. The selected principal root of the normalized companion is
   exactly \(1\), of algebraic multiplicity two, and has a fixed
   positive separation from every other root throughout that
   neighborhood.

These are conditions on the actual characteristic and ordinary
lift, not on unknown source amplitudes. On the real interval \(J\)
the other normalized roots are strictly inside the unit circle,
by the selected dominant-root theorem already used in the direct
sources. They need not remain inside that circle at complex points.
The complex construction only requires separation from \(1\).

**Theorem.** Under (4) and these three conditions, there is a common
holomorphic baseline \(A_N^0\) on \(\Omega_1\), with
\(\|A_N^0\|\le C N^p\), such that on a fixed real buffer about \(I\)
\[
 |a_j-A_N^0(x_j)|+|b_j-(A_N^0)'(x_j)|
                                  \le C e^{-\kappa N}
 \tag{5}
\]
for some \(\kappa>0\). There are exact scalar representatives
\({\cal H}_N^\sigma=f_h(A_N^0+C_N^\sigma)\), \(\sigma=\pm1\),
matching both physical jets on the window, for which
\[
 \|C_N^\sigma\|\le C e^{-\kappa_1 N}
 \quad\hbox{on fixed compact subsets of }
                 \Omega_1\cap\{\sigma\Im x\ge0\}.
 \tag{6}
\]
All fixed derivatives obey (6) with a polynomial factor absorbed
by decreasing \(\kappa_1>0\). The same conclusion holds across a
sufficiently thin fixed collar on the opposite side. The width of
this collar depends on \(\kappa\); the height on the designated
side does not enter that repair loss.

The theorem supplies a common baseline and a small relative
interface. A polynomial phase-normalized bound for the separate
half-plane representatives alone was already proved by the
weighted-window source and would not require condition 3.

## 2. Continuing the regular slow graph

The original even midpoint identities and the double-root equation
give \(P_h1=O_{\rm hol}(h^2)\) on these domains, by the same finite
Taylor calculation as in the regular-amplitude source. This identity
continues holomorphically; it is not inferred merely from a principal
symbol. In the scalar companion the fixed columns
\({\bf r}=(1,\ldots,1)^T\) and \({\bf v}\) of successive integer
offsets consequently satisfy
\[
 M_h{\bf r}={\bf r}+O(h^2),\quad
 M_0{\bf r}={\bf r},\quad M_0{\bf v}={\bf v}+{\bf r}.
 \tag{7}
\]

A fixed small circle around \(1\) defines the holomorphic Riesz
projection of the principal matrix \(M_0\). Its generalized unit
space is the constant span of \({\bf r},{\bf v}\).
The analytic Kato equation for this projection gives a holomorphic
complement frame on the simply connected domain. It fixes the two
displayed columns. The stated path-length bound and bounded
projection derivatives give uniform bounds on the frame and its
inverse on a smaller buffered domain. In this frame the step is
\[
 \begin{pmatrix}A_h&B_h\\C_h&D_h\end{pmatrix},\qquad
 A_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
 B_h,C_h=O(h),\quad D_h=D_0+O(h).
 \tag{8}
\]
The Sylvester map \(R\mapsto RA_0-D_0R\) is uniformly invertible
on the compact domain: no eigenvalue of \(D_0\) is \(1\).
No modulus ordering at nonreal points is needed for this assertion.

For completeness, the analytic graph iteration solves
\[
 R(x+h)(A_h+B_hR)=C_h+D_hR
 \tag{9}
\]
to exponential accuracy. Write its right fixed-point equation as
\[
 \begin{split}
 RA_0-D_0R={}&C_h+(D_h-D_0)R-R(A_h-A_0)\\
 &-[R(x+h)-R(x)]A_h-R(x+h)B_hR.
 \end{split}
 \tag{10}
\]
On a ball \(\|R\|\le C h\), its Lipschitz constant on a domain
eroded by \(\delta\ge2h\) is at most \(C(h+h/\delta)\), by
Cauchy's estimate. Choose \(\delta=Mh\) with fixed large \(M\).
Iteration from zero maps the ball into itself and contracts by at
most \(1/2\) between successive eroded domains. There are
\(K\ge c/h\) iterations within a fixed available buffer, so the
residual is \(O(e^{-c'/h})\). Reserve a fixed inner buffer for
derivatives, obtaining \(R_h=O(h)\), \(R_h'=O(h)\).

Applying (9) to the first slow column, (7) gives
\[
 (A_h-I)e_1=O(h^2),\quad C_he_1=O(h^2),\quad
                      R_he_1=O(h^2).
 \tag{11}
\]
For the last assertion first use \(R_h'=O(h)\) in the shifted
equation and then invert \(I-D_h\), which is uniformly invertible
by condition 3. Hence the gauge \(\operatorname{diag}(1,h)\)
gives an analytic slow step
\[
                         T_h(x)=I_2+hB_h^{\rm s}(x),
                    \|B_h^{\rm s}\|\le C,
 \tag{12}
\]
and an embedding \(G_h\) with polynomial conditioning and
\[
             M_hG_h=G_h(x+h)T_h+O(e^{-c'/h}).
 \tag{13}
\]
These objects are defined on a fixed neighborhood of
\(\overline\Omega_2\), after choosing the construction buffers
inside \(\Omega_3\). This repeats the actual scalar reduction;
only its complex-domain separation hypothesis has been enlarged.

## 3. An exponentially accurate bounded modified differential equation

We give the analytic embedding argument because a formal logarithm
of \(T_h\) would not control the error at exponential scale.
For a bounded holomorphic matrix \(A(x)\), let \(\Phi_h(A;x)\)
be the fundamental matrix from \(x\) to \(x+h\) of
\(Y'=A(x)Y\), with initial matrix \(I\). Define
\[
 Q_h(A)=\frac{\Phi_h(A)-I}{h}-A,
 \qquad \mathcal F_h(A)=B_h^{\rm s}-Q_h(A).
 \tag{14}
\]
On a domain eroded by \(\delta\ge2h\), and for
\(\|A\|,\|\widetilde A\|\le R\),
\[
 \|Q_h(A)-Q_h(\widetilde A)\|
           \le C_R(h/\delta+h)\|A-\widetilde A\|.
 \tag{15}
\]
Indeed, writing \(U_A(s;x)\) for the flow to \(x+s\),
\[
 Q_h(A)(x)=\frac1h\int_0^h[A(x+s)-A(x)]\,ds
       +\frac1h\int_0^h A(x+s)[U_A(s;x)-I]\,ds.
 \tag{16}
\]
Cauchy's estimate bounds the difference of the first integrals
by \(C h\|A-\widetilde A\|/\delta\). The integral equation for
the flow gives \(\|U_A-I\|\le C_Rh\) and
\(\|U_A-U_{\widetilde A}\|\le C_Rh\|A-\widetilde A\|\).
These bound the second difference by \(C_Rh\|A-\widetilde A\|\),
proving (15).

Start at \(A^{(0)}=B_h^{\rm s}\). Reserve a fixed initial shrink;
there its derivatives are bounded, so
\(A^{(1)}-A^{(0)}=-Q_h(B_h^{\rm s})=O(h)\).
For subsequent iterations use erosion \(Mh\) and choose \(M\)
large enough that (15) is at most \(1/2\) on a fixed ball containing
\(B_h^{\rm s}\). The successive differences contract. Performing
\(K\ge c/h\) iterations within the remaining fixed buffer gives
a holomorphic matrix \(A_h\), uniformly bounded and satisfying
\[
 A_h=B_h^{\rm s}+O(h),\qquad
              \Phi_h(A_h;x)-T_h(x)=O(e^{-c_2/h})
 \tag{17}
\]
on a neighborhood of \(\overline\Omega_1\). The last estimate is
the exact identity
\(\Phi_h(A^{(K)})-T_h=h(A^{(K)}-\mathcal F_h(A^{(K)}))\)
and the final contracted difference. Fixed derivatives follow on
reserved smaller domains. Thus (17) is a finite analytic estimate,
not a formal all-orders assertion.

The fundamental matrix of \(Y'=A_hY\) is single valued on
\(\Omega_1\). If the prescribed initial vector is polynomially
bounded, its solution is polynomially bounded throughout this
domain: along the specified paths of length at most \(L\), both
the fundamental matrix and its inverse have norm at most \(e^{CL}\).
This is why the path-length and simple-connectivity assumptions
were stated explicitly.

## 4. Choosing the baseline from the actual source

On the real buffer the actual normalized scalar packet has
polynomial size by the terminal bulk-compatibility theorem. The
continued graph (13) has the same strict real stable complement.
Forward attraction after a fixed positive left buffer therefore
makes the actual packet exponentially close to this graph. Its
regular slow coordinates differ exponentially from an exact
trajectory of (12), throughout a smaller real buffer about \(I\).
The left packet is retained in this attraction estimate.

Start the differential equation (17) with that trajectory's actual
slow coordinates at one interior real row. On the real interval,
the step error in (17) sums to an exponential error under the
bounded forward and inverse propagators of (12). Thus extraction
of the current scalar slot from
\[
                         G_h(x)Y_h(x)
 \tag{18}
\]
defines a baseline \(A_N^0\), polynomially bounded on \(\Omega_1\),
whose actual nodal value errors are exponentially small on the
real buffered window.

The same baseline retains the approximate scalar equation:
\[
                  P_hA_N^0=O_{\rm hol}(e^{-c_3/h})
 \tag{18a}
\]
on fixed inner subdomains with their finite shifts included.
Indeed (13),(17) make the vector (18) satisfy its companion
equation with exponential error. The companion's shift rows
identify its other slots with the finitely shifted current slot,
up to the same error. Substitution in its last row proves (18a).
The polynomial norm of the initial vector only decreases the
positive exponential constant.

It remains to estimate its derivative error, rather than assume
it. Let \({\cal A}_N\) be the exact moderate scalar representative
given by the terminal compatibility theorem on a small real tube.
Both it and \(A_N^0\) have polynomial norms there. Their nodal value
differences are exponentially small. Repair these differences on
a still buffered real interval with the ordinary finite sinc
interpolant. Its norm is at most
\(C N^p e^{-cN+\pi N|\Im x|}\), so on a fixed sufficiently narrow
tube it is exponentially small, including fixed derivatives.
After this temporary repair the two functions agree at every node.
The disk Blaschke estimate with \(cN\) real zeros, and a finite
disk cover with reserved Cauchy radii, makes their difference and
derivative exponentially small on an inner tube. Removing the
temporary repair proves
\[
 e_j:=a_j-A_N^0(x_j)=O(e^{-\kappa N}),\qquad
 d_j:=b_j-(A_N^0)'(x_j)=O(e^{-\kappa N}).
 \tag{19}
\]
This uses the actual normal-compatibility theorem. Polynomial
packet size or a principal characteristic alone would not prove
the second equation. All constants are fixed by the domain and
real buffers; \(\kappa\) may be decreased to absorb polynomial
losses and is not a freely adjustable error rate.

## 5. Exact one-sided repair and the common-baseline interface

For \(\sigma=\pm1\), sum over the window's physical nodes and put
\[
 L_j^\sigma(x)=e^{\sigma2\pi i(x-x_j)/h}
                    \operatorname{sinc}^2((x-x_j)/h),
\]
\[
 C_N^\sigma(x)=\sum_j
     [e_j+(d_j-\sigma2\pi i e_j/h)(x-x_j)]L_j^\sigma(x).
 \tag{20}
\]
The value and derivative of this correction at row \(j\) are
\(e_j,d_j\); every other summand has a double zero there. Hence
\({\cal H}_N^\sigma=f_h(A_N^0+C_N^\sigma)\) matches the original
full physical jets exactly.

The Fourier support of \(L_j^+\) is \([0,2/h]\), and that of
\(L_j^-\) is \([-2/h,0]\), with total absolute coefficient mass
one. Thus \(|L_j^\sigma|\le1\) on \(\sigma\Im x\ge0\), and its
fixed derivatives cost only powers of \(h^{-1}\). Combining this
with (19) and the \(O(h^{-1})\) nodes proves (6) on every fixed
bounded part of the designated half-domain. On the opposite side
the bound is \(e^{4\pi|\Im x|/h}\). A fixed collar of width less
than \(\kappa/(8\pi)\) therefore retains an exponential estimate.
The amount of designated-side continuation has no such restriction.
Together with (18a), the same estimates give an exponential
normalized scalar residual for \(A_N^0+C_N^\sigma\) on fixed
inner designated half-domains with their finite real shifts included.

To see exactly what enters the original current, use the centered
grid kernel
\[
                 D_h(x)=(\pi/h)^2\sec^2(\pi x/h).
 \tag{21}
\]
Put \(z=x-x_j\), \(k=2\pi i/h\). Cancellation of the common
baseline and of the double-pole kernel gives exactly
\[
 \boxed{\quad
 D_h(C_N^+-C_N^-)=\sum_j
 \frac{[e_j+(d_j-k e_j)z]e^{kz}
               -[e_j+(d_j+k e_j)z]e^{-kz}}{z^2}.
 \quad}
 \tag{22}
\]
Each summand is removable at \(z=0\), with value \(4\pi i d_j/h\).
For real \(z\), Taylor's estimate on \(|z|\le h\) and the
elementary numerator bound on \(|z|\ge h\) give
\[
 \left|\frac{\cdots}{z^2}\right|
        \le C(h^{-2}|e_j|+h^{-1}|d_j|).
\]
Consequently
\[
        \sup_{x\text{ in the real window}}
            |D_h(C_N^+-C_N^-)|\le C e^{-\kappa_1N}
 \tag{23}
\]
after absorbing a polynomial and decreasing \(\kappa_1>0\).
This is the improvement over direct one-sided interpolation of
the original jets: the coefficients in (22) are the exponentially
small errors relative to one common slow baseline.

## 6. Original closing, exterior boundaries and the action budget

Let the entire remaining original spectator be
\(P_N^{\rm sp}(Z;\mathbf y)\), with all shared colors, crossing
normals, free parameters and remaining traces retained. It is not
the spectral polynomial \(P_N\). Set
\[
 g_\sigma(x)=\sin(2\pi x)\,{\cal H}_N^\sigma(x)
                              P_N^{\rm sp}(c(x);\mathbf y).
\]
Choose a closed window rectangle contained in \(\Omega_1\), with
midpoint vertical boundaries enclosing the selected half-grid
rows \(j_0\le j\le j_1\), namely
\(a_N=j_0h\) and \(b_N=(j_1+1)h\).
The positive-row normalization of the weighted-window source,
translated by \(h/2\), gives exactly
\[
 \phi_{N,I}(G_NP_N^{\rm sp})=-\frac{\eta}{2\pi^2i}
 \left\{\int_{E_-}D_hg_-\,dx+\int_{E_+}D_hg_+\,dx
                  +\int_{a_N}^{b_N}D_h(g_+-g_-)\,dx\right\}.
 \tag{24}
\]
Here \(E_-\) runs down the left side, across the lower boundary,
and up the right side; \(E_+\) runs up the right side, across the
upper boundary, and down the left side. Every vertical half-side
is included. These contours must lie in the supplied domains.
The double-pole kernel in (21) retains all original angular aliases.

Equation (23) bounds the real interface pointwise by
\[
 C e^{-\kappa_1N}e^{N\Re{\cal S}(x)}
                |\sin(2\pi x)p(x)P_N^{\rm sp}(c(x);\mathbf y)|.
 \tag{25}
\]
The exact identity holds before any remaining original closing.
For example, if a bound for that actual retained spectator after
the required norm/closing gives rate \(E(x)\), uniformly on the
window, (25) gives the interface upper rate
\[
                 \sup_x\{\Re{\cal S}(x)+E(x)\}-\kappa_1.
 \tag{26}
\]
To obtain a parent gap this expression must actually lie below the
parent action. The positive number \(\kappa_1\) cannot be chosen
larger just because a larger deficit is needed.

The exterior currents are still those in (24). On the midpoint
verticals and on fixed nonzero horizontal heights,
\(|D_h(x)|\le C N^2e^{-2\pi N|\Im x|}\), exactly as in the
weighted-window theorem. The designated representative supplies
its calibrated phase bound there, but this does not estimate the
joint spectator or prove an exterior-current gap. In angular
coordinates \(t=\pi-2\pi x\), a lower parent height
\(\Im t=-H\) uses the upper \(x\) half-domain, with
\(\Im x=H/(2\pi)\). The sign is not interchangeable.

For fixed physical marks apply their finite ordinary polynomial
in \(\widetilde J\) to the common baseline and the exact
representatives, constructed first on a slightly larger real
window and complex buffered domain. Every fixed shifted row of
the target window is then among the matched rows. Finite shifts and fixed
derivatives preserve the polynomial bounds and exponential errors;
the polynomial exponent may depend on the mark. Fixed shared
products similarly have a common product baseline. Telescoping
their differences preserves (25) with the sum of the phases and
the full shared normal product rule. No arbitrary free color is
quotiented, and no shared spectator is separated in (24).

The criterion is therefore a source-specific continuation and
small-interface theorem. It does not assert that a given positive
parent provides the required separated complex domain, that its
terminal sheet remains the selected one, or that its geometric
heights lie in such a domain. It does not remove the exterior
currents or establish noncancellation of the original closing.

## 7. Coverage and complete direct sources

The direct one-sided kernels and original relative trace identity
are already in the weighted-window note. The new inputs are the
bounded modified differential equation with exponential step error,
its use with the actual continued regular slow graph, and the
common baseline making the exact one-sided correction and
original interface exponentially small. The result is not obtained
by continuing a small-strip sinc repair into its growing half-plane.

Complete source reads were fresh or retained at the following
unchanged versions; used implications and all hashes were checked.

* [Actual regular amplitude transport](research_filled_leaf_regular_amplitude_transport.md),
  SHA256 7110294071ac8ad878cf3848e744966ab9682c9c29177878842bf94ff6d63574:
  the ordinary even-symbol identity, fixed slow columns, analytic
  graph and polynomial gauge, and real stable attraction.
* [Terminal scalar compatibility](research_terminal_bulk_scalar_compatibility.md),
  SHA256 9f4a359260c9aef37d93b2158cc551a7867ec3eab7644b633cf1c2beac9257e4:
  the actual polynomial real packet budget, exact moderate scalar
  representative, full normal convention and fixed-mark scope.
* [Original weighted window current](research_filled_leaf_weighted_window_current.md),
  SHA256 d1b533a14265451d31fb33870787f8f5145c7971f4cfc2d912b1c6652b523188:
  complete fresh read; exact one-sided Hermite kernels, original
  trace factor and orientations, aliases and retained spectators.

Only written mathematics, source-text reads and file hashes were
used. No mathematical programs, numerical experiments, tests or
builds were run. Adopted notes and public manuscripts are unchanged.
