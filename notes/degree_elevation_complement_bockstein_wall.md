# The degree-elevation complement is one marked quantum-normal wall line

Research theorem and actual crossing/source calculation, 27 October
2026. The complement omitted by actual cut degree elevation has
dimension 2N+1, but its whole memory-Borel complex contracts to ONE
two-term wall complex. The contraction retains the two extreme
corners and uses no division by the wall parameter. Its root norm
is O(N) in the natural unitary spin metric.

The source on that wall is essential. The original coherent cut
assigns it 2^(-N); the uniform interval assigns 1/(N+1). Their
exponential ratio cannot be discarded as a Ward homotopy.
An explicit charged component of the FIRST ACTUAL universal R
normal hits the wall generator in an ordered current calculation.
No full-network cancellation or selected geometric contribution
is inferred from these local statements.

## 1. The actual missing subspace and its global boundary polynomial

Use [actual matrix degree elevation](degree_elevation_actual_head_ward_map.md)
\(\mathcal E_N:\operatorname{End}\operatorname{Sym}^{N-1}
\to\operatorname{End}\operatorname{Sym}^{N}\). It is injective,
unital, cut-preserving and equivariant for the ACTUAL divided
classical commutators. Write

\[
 \mathcal I_N=\operatorname{im}\mathcal E_N,\qquad
 \operatorname{End}\operatorname{Sym}^{N}
                          =\mathcal I_N\oplus\mathcal W_N.
\]

The summands have adjoint spins 0,...,N-1 and N respectively;
\(\dim\mathcal W_N=2N+1\). A concrete quotient map is

\[
 \operatorname{ob}_N(C)(u)
   =u^N\ell_N(u)C\psi_N(-1/u)
   =\sum_{i,j}(-1)^j{N\choose i}C_{ij}u^{N+i-j}.      \tag{1.1}
\]

Its kernel is exactly I_N: the symbol numerator is divisible by
1+ut precisely when its restriction t=-1/u vanishes. The degree
bound then leaves a numerator of bidegree at most N-1, giving the
unique old matrix. Its image is every polynomial of degree at most
2N. Thus W_N is the GLOBAL H0(O(2N)) boundary module, rather than
an arbitrary missing collection of matrix entries. Its two endpoint
corners are e^N=N!E_(0,N) and f^N=N!E_(N,0).

For complete direct verification, (1.1) takes ad e,ad f,ad h to
partial_u, 2Nu-u^2 partial_u, 2N-2u partial_u, and takes Ad(Q^(-J))
to g(u)->Q^N g(u/Q). The
[independent incidence/source calculation](degree_elevation_wall_residual_and_source_moments.md)
records this quotient and its one-sided clock residuals.

One may project onto W_N algebraically without choosing a split
matrix basis: the adjoint Casimir
\(\mathcal C=(\operatorname{ad}h)^2/2+
\operatorname{ad}e\operatorname{ad}f+
\operatorname{ad}f\operatorname{ad}e\) has eigenvalues
2l(l+1). Its polynomial projector onto eigenvalue 2N(N+1) is
\(\prod_{l=0}^{N-1}(\mathcal C-2l(l+1))/
[2N(N+1)-2l(l+1)]\). All denominators are nonzero constants.

## 2. The exact whole Borel complex

Let R be the actual coefficient field completed in
delta=1-Q^N, retaining
Q=Q_N(1-delta)^(1/N). Work first in the untwisted target frame,
with memory K=Q^(-J), rho=Ad K and F=ad f. The ACTUAL whole
arrow gauge B_s(q) sends f to the original F^(N)|_s and commutes
with memory K. Conjugating the complex below by B_s carries all
its units and source marks. The memory K is not the old physical
high-color head clock.

On any invariant spin module define

\[
 \begin{split}
 d_0C&=((\rho-I)C,FC),\\
 d_1(X,Y)&=(\rho-Q^{-1})Y-Q^{-1}FX.                  \tag{2.1}
 \end{split}
\]

The identity rho F=Q^(-1)F rho proves d_1d_0=0 exactly over R.
No root specialization has occurred.

For spin l choose a basis v_0,...,v_L, L=2l, satisfying
Fv_j=v_(j+1) and rho v_j=Q^(l-j)v_j. Each j<L gives a separate
three-term fork

\[
 R\ \xrightarrow{a\mapsto(A_ja,a)}\ R^2
       \xrightarrow{(x,y)\mapsto Q^{-1}(-x+A_jy)}\ R,
 \quad A_j=Q^{l-j}-1.                                \tag{2.2}
\]

It contracts using h_1(x,y)=y and h_2(z)=(-Qz,0), whether or not
A_j vanishes at the root. The only remaining terms are

\[
 [R\xrightarrow{Q^{-l}-1}R]_{0,1},\qquad
 [R\xrightarrow{Q^l-Q^{-1}}R]_{1,2}.                 \tag{2.3}
\]

This is a literal direct decomposition, not a numerical rank
argument. In particular it keeps both possible resonance lines.

For W_N take l=N and normalize the chain by

\[
 v_j=\frac{(-1)^N}{(2N)!}(\operatorname{ad}f)^j e^N,
                 \quad v_{2N}=f^N.                 \tag{2.4}
\]

The last equality follows by expanding the commutator: only its
middle term survives, giving ad(f)^(2N)e^N=(-1)^N(2N)!f^N.
The second arrow in (2.3) is a unit since its root is
1-Q_N^(-1). The entire complement therefore contracts to

\[
 \boxed{\ [R f^N\xrightarrow{,Q^{-N}-1,}R f^N]_{0,1}\ },
             \qquad Q^{-N}-1=\frac\delta{1-\delta}.   \tag{2.5}
\]

The coefficient has a SIMPLE zero, with derivative one. At the
root H0 and H1 are each the one-dimensional marked wall line,
and H2=0. Over the whole formal DVR, H0=0 and H1=R/(delta).
Its root kernel and its first-normal Bockstein must therefore
be retained together; no free whole horizontal source line is
being asserted.

## 3. Explicit projection and contraction retaining every unit

For x=sum x_jv_j, y=sum y_jv_j and z=sum z_jv_j, projection to
(2.5) is pi_0(C)=C_(2N) and pi_1(x,y)=x_(2N); inclusion uses
v_(2N) in degree zero and (v_(2N),0) in degree one. Put

\[
 \begin{split}
 h_1(x,y)&=\sum_{j=0}^{2N-1}y_{j+1}v_j,\\
 h_2(z)&=\left(-Q\sum_{j=1}^{2N}z_jv_{j-1},\
               (Q^N-Q^{-1})^{-1}z_0v_0\right).        \tag{3.1}
 \end{split}
\]

Direct substitution gives
h_1d_0=I-iota_0pi_0,
d_0h_1+h_2d_1=I-iota_1pi_1, and d_1h_2=I.
Only Q^N-Q^(-1), a unit, is inverted. The wall delta is never
inverted. Conjugating all maps by the ACTUAL B_s(q) gives the
same contraction on the actual whole target complement
Ad(B_s)W_N. The original source/co-source must be conjugated
or evaluated with those same B_s units; root B_s=I does not
erase their derivatives.

In the unitary Fr metric ||v_k||^2=binom(N,k), e and f are
adjoints. The highest-spin Hilbert--Schmidt module has an
orthonormal chain with F-arrow coefficients
sqrt((j+1)(2N-j)). Its anchored F inverse has norm 1/sqrt(2N).
Using those coefficients in (3.1), its fork inverses have that
same bound; the remaining unit inverse has root norm
1/[2 sin(pi/N)]. The orthogonal W_N projector has norm one.
Hence the root complement contraction has norm O(N), explicitly
at most max(1/sqrt(2N),1/[2 sin(pi/N)]).
This is a bound on the COMPLEX contraction, not on every source
functional or on a uniform off-root neighborhood.

## 4. The actual global co-source on the extra module

Under (1.1), the basis (2.4) is
\(\operatorname{ob}_N(v_j)=N!u^j/(2N-j)!\).
Thus any ACTUAL cut functional Phi restricts to the global dual
Čech class

\[
 c_\Phi(u)=\sum_{j=0}^{2N}
          \frac{(2N-j)!}{N!}\Phi(v_j)u^{-j-1}
                 \quad\text{in }H^1(O(-2N-2)).       \tag{4.1}
\]

Its residue pairing with ob_N(C) equals Phi(C) on W_N, by the
[explicit two-chart source pairing](global_frobenius_cech_source_and_endpoints.md).
The two corner components occupy different north/south Laurent
modes. Neither is a zero Čech class merely because it was absent
from the degree-elevation image.

For the normalized wall generator w=f^N/N!=E_(N,0), ||w||_HS=1,
the ACTUAL paired coherent source gives

\[
 \Phi_m(w)=\left(\frac{1-m}{2}\right)^N,
 \qquad \Phi_+(w)=2^{-N}\quad(m=0).                   \tag{4.2}
\]

The uniform interval row gives instead

\[
                  \Phi_{\rm uni}(w)=\frac1{N+1}.      \tag{4.3}
\]

The ratio is 2^N/(N+1), GENUINELY exponential. For the unnormalized
divided generator f^N the two values are N!/2^N and N!/(N+1).
Their actual normalization has not been hidden by declaring its
matrix unit to be the source value one.

The coupled original source makes the head endpoint explicit:
\(\Phi_{e_D}(w\otimes H_{\rm head})=2^{-N}(H_{\rm head})_{00}\).
The Fr endpoints 0 and N are the SAME cyclic head endpoint.
The uniform interval row is not that original coherent coupon.
Since w is root Ward-closed, no root co-source homotopy on the
full target can equate (4.2) and (4.3).

There is still an exact relative-endpoint interpretation:
Phi_m(w)dm/2=-d[((1-m)/2)^(N+1)/(N+1)]. Its interval integral
from -1 to +1 is 1/(N+1), while its endpoint-coherent value at
m=0 is 2^(-N). Exactness of a primitive does not eliminate its
marked endpoint jump. The global class (4.1), actual normal
units, and relative endpoint density remain together.

The OTHER omitted corner w_high=E_(0,N) has response
Phi_m(w_high)=((1+m)/2)^N. It is carried by the contracted forks,
not a second H0 wall: Fw_high!=0. Its interval primitive is
((1+m)/2)^(N+1)/(N+1), with a nonzero POSITIVE-endpoint jump.
Thus the two corners have different cochain roles even though
their uniform integrals and their coherent values at m=0 agree.
Contracting the highest corner requires its recorded Ward/source
homotopy, rather than deleting its relative endpoint pairing.

## 5. An unavoidable charged FIRST ACTUAL R normal sees the wall

In the constant actual integral frame, put I_1=R_0^(-1)R_1.
For r=N its first resonant transfer, including every head entry,
is exactly

\[
                    (I_1)_{(-1,+1)}=N e\otimes f
                                      \otimes I_{\rm heads}.      \tag{5.1}
\]

This is the original universal R tail, not an appended operator:
the first-normal coefficient is kappa_N E^(N) tensor F^(N),
kappa_N=N(-1)^(N-1), and E^(N)=(-1)^(N-1)e.
All nonresonant normal terms change at most ONE Fr block, while
Cartan terms change neither. Thus no other first-normal term
can cancel the charged component (-1,+1) of (5.1).
The actual whole diagonal arrow gauges B_s(q) add first-normal
gauge terms of ZERO Fr block charge. They therefore cannot erase
this charged channel; their units remain in all other rows.

Let n=N-1 and choose actual old-head matrix coupons
P_0=E_(0,0) and C_low=E_(n,0). Put X=E_N(P_0), Y=E_N(C_low).
Their entries are

\[
 X=\operatorname{diag}(1,1/N,0,\ldots),\qquad
 Y=N^{-1}E_{N-1,0}+E_{N,1}.
\]

Here fY=Yf=w. Consequently the charged (-1,+N) component of the
ACTUAL adjoint normal current is

\[
 \Pi_{(-1,+N)}[I_1,X\otimes Y]
                  =N[e,X]\otimes w\otimes I_{\rm heads}.          \tag{5.2}
\]

Its first factor is
\([e,X]=-(N-1)E_{0,1}-(N-1)E_{1,2}/N\), an elevated old
head current. The second factor is precisely the wall generator,
not an element of I_N. At a generic root the first factor is a
memory-Cartan Ward term, since its charge has unit Q_N-1.
Thus (5.2) is a concrete LOCAL Ward/carry source with a wall-valued
coefficient; it is not a closed scalar knot invariant by itself.

Its two legitimate paired values are different:

\[
 (\Phi_{\rm uni}\otimes\Phi_{\rm uni})(5.2)
                      =-\frac{N-1}{N+1},\qquad
 (\Phi_+\otimes\Phi_+)(5.2)
                      =-\frac{N(N-1)}{2^{2N-1}}.      \tag{5.3}
\]

Both are nonzero. The relative co-source can therefore detect
this actual omitted-corner channel; it cannot be dropped as a
zero Čech boundary or replaced by its uniform value.

Under the controlled coupled-source gauge G, the e and f factors
also acquire their literal head shifts V^(-1) and V. The source
coupon must be conjugated WITH the operator. Leaving a head
shift behind while changing the source would give a different
pairing, potentially zero. No such change is made in (5.3).

For the relative interaction-commutator used here, I(0)=I and
its root commutator is zero. Thus its first coefficient depends
only on (5.2), even when the input coupons and paired source have
their actual whole lifts. This does NOT remove the separate lift
terms in the whole Euler/current formula (8d) of the
[endpoint-completed clock theorem](endpoint_completed_normal_clock_euler_current.md).
That formula still uses the prescribed H_1 and its charged head
neighbors. No general current descent follows by replacing it
with this one isolated interaction channel.

## 6. Low raw PBW order versus ordered products and clock gauges

A PBW operator of degree d<N has normalized coherent numerator
divisible by (1+ut)^(N-d), so ob_N vanishes. In particular raw
interaction coefficients of order j lie in the elevation image
on every Fr leg whenever N>2j, by the actual all-normal bound.
The first possible order for a raw PBW complement is ceil(N/2).
This is an exclusion bound; attainment by a particular actual
crossing or closed word is a separate assertion.

This does NOT say multiplication by such a coefficient preserves
the image: (5.2) is already a first-normal counterexample on
elevated input coupons. Nor does it apply to a controlled source
gauge containing genuine whole clock dilations. Their one-sided
symbols can have nonzero ob_N even at root order. Their actions
must be kept as whole functions with their source characters.

The [Clebsch strictification](clebsch_memory_dilation_and_actual_r_excursions.md)
keeps its complementary memory sector for precisely this reason;
neither that construction nor (2.5) declares the full actual R
network image-invariant. Every actual offimage current must be
projected by (1.1) and then checked in the explicit complex (2.1).
A CLOSED residual reduces to its ONE wall component; its value
there uses the ORIGINAL source row, not automatically (4.3).

The global geometric Ward/current map, its charged head neighbors
and the selected regulator norm remain to be proved. This result
replaces an arbitrary 2N+1-dimensional missing source by an exact
single marked Bockstein wall line and exhibits an actual R channel
which makes its source normalization unavoidable.

[Exact actual-matrix/complex audit](../experiments/audit_degree_elevation_complement_wall.py).
[Results](../experiments/degree_elevation_complement_wall_results.json).
[Independent quotient/source audit](degree_elevation_wall_residual_and_source_moments.md).
