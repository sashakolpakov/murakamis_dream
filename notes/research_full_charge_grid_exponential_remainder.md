# Exponentially accurate full charge-grid source remainders

Private written proof, 16 November 2026.

The adopted full charge-grid theorem has a uniform Gevrey-1
strengthening: its expansion may be truncated at a sufficiently small
fixed multiple of the level, with an exponentially small relative
error. This is an estimate for the actual original finite source,
including mixed zero/unit charge faces, both parities and ordinary
free-boundary data. It uses the same phase, coefficients and finite
companion sum as that theorem.

Optimal Euler--Maclaurin truncation already occurs for narrower
products in the archived cap-cross proofs and in the Conway leaf
source. The additional work here is the uniform growing-order
Gaussian remainder, exact odd division at charge-zero faces, and
assembly with the original higher aliases and high Newton sectors.
Neither complex reconstruction nor a subsequent heat integral is
assigned a geometric leading term by this estimate.

## 1. Original source and quantitative statement

Keep the source and notation of the pinned full-grid theorem. Thus
\(S\) is a nonempty connected proper selected subtree of a fixed
finite tree, every selected power is zero, and every original selected
degree is at least twelve. Write
\[
 s=|S|,\qquad e=|E_S|,\qquad b=|\partial S|,\qquad
 e=s-1+b,\qquad p=3(b-1)/2,\qquad D=N-1.
 \tag{1}
\]
Every outside incidence remains an independent ordinary spectral
variable \(z_w=-2\cos u_w\). Use the original full Newton algebra,
kernel and closing
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=(-1)^D N^2[z^D]\operatorname{rem}_{P_N}f,
\]
\[
 K_N(t,u)=\sum_{a=0}^{D}e_a(-2\cos t)e_a(-2\cos u).
 \tag{2}
\]
For \(c_v=J_v/N\), \(1\le J_v\le N\), the exact coupon, including
its first normals, is \(\mathcal C_{N,c_v}=T_{N-J_v}(-z_v/2)\).
The source is
\[
 Z_N(\mathbf c;\mathbf u)=
 \left(\prod_{v\in S}\phi_N^{(v)}\right)
 \left[\prod_{v\in S}\mathcal C_{N,c_v}
                         \prod_{vw\in E_S}K_N(t_v,t_w)\right].
 \tag{3}
\]
No replacement of this closing by values alone is made.

The full-grid theorem constructs the original stationary action
\(W(\boldsymbol\lambda,\mathbf u)\) on a holomorphic neighborhood
of \([0,2]^S\) and a fixed outside polydisk. At complete outside
angles its value is the height minimum \(M(\boldsymbol\lambda)\).
Every effective saddle in this doubled cube is uniformly regular:
its heights obey \(H_v\le\log3\), its edge products are at most
\(1/3\), and all stationary wire indices have a fixed interior
margin in \((0,1/2)\). Put
\[
 \lambda_v^\omega=
 \begin{cases}c_v,&\omega_v=0,\\2-c_v,&\omega_v=1,\end{cases}
 \qquad
 R_\omega(\mathbf c)=\prod_v\lambda_v^\omega/c_v,
               \quad \omega\in\{0,1\}^S.
 \tag{4}
\]
The quotients in (4) are used only on the nonzero lattice.

**Theorem 1.** The coefficient functions \(\beta_r\) of the
full-grid theorem can be bounded on a fixed complex neighborhood
of the doubled cube and a fixed outside polydisk by
\[
                       |\beta_r|\le C^{r+1}r!.
 \tag{5}
\]
After reducing the outside polydisk, there are constants
\(C\ge1,a>0,\delta>0,N_0\), independent of \(L,N,\mathbf J\),
such that, for \(N\ge N_0\), \(1\le L\le aN\), and every
\(\mathbf J\in\{1,\ldots,N\}^S\),
\[
 \begin{split}
 Z_N={}&N^{-p}\left(\prod_vc_v\right)e^{NW(\mathbf c,\mathbf u)}
       \left\{\sum_{r=0}^{L-1}N^{-r}
                       \mathcal B_{N,r}(\mathbf c,\mathbf u)
                          +\mathcal R_{N,L}(\mathbf c,\mathbf u)\right\},\\
 \mathcal B_{N,r}={}&
 \sum_\omega R_\omega(\mathbf c)\,
 \beta_r(\boldsymbol\lambda^\omega,\mathbf u)
 e^{N\{W(\boldsymbol\lambda^\omega,\mathbf u)
                              -W(\mathbf c,\mathbf u)\}},\\
 |\mathcal R_{N,L}|\le{}&
              C^{L+1}L!N^{-L}+Ce^{-\delta N},\qquad
 |\mathcal B_{N,r}|\le C^{r+1}r!.
 \end{split}
 \tag{6}
\]
The leading sum \(\mathcal B_{N,0}\) has the same uniform
positive lower bound at complete outside angles and the same
holomorphic unit property as in the adopted theorem.

In particular there are \(a_*>0,\kappa>0,C_*>0\) such that
the actual finite sum \(\mathscr S_N\) in (6), truncated at
\(L_N=\lfloor a_*N\rfloor\), satisfies
\[
 |Z_N-\mathscr S_N|
 \le C_*N^{-p}\left(\prod_vc_v\right)
          e^{N\Re W(\mathbf c,\mathbf u)-\kappa N}.
 \tag{7}
\]
The normalized error has the same estimate with every fixed ordinary
spectral boundary derivative on a smaller polydisk. The constants
depend on the fixed original subtree and the chosen domains.
The proof specifies how a positive \(\kappa\) is obtained from
analytic neighborhood sizes and the actual contour gaps; it gives
no comparison of that constant with a remote heat target.

## 2. Uniform Gevrey bounds for the exact factorials

Use the original normalized factorial and sine primitive
\[
 H_N(u)=G_N(Nu-1/2),\qquad
 J'(u)=\Log(2\sin\pi u),\quad J(1/2)=0,
\]
\[
 \Omega=\mathbb C\setminus((-\infty,0]\cup[1,\infty)).
 \tag{8}
\]
The pinned centered-factorial proof gives the exact identities
\[
 H_N(1/2)=\sqrt N,\qquad
 \partial_u\log H_N(u)
   =\sum_{k=0}^{N-1}F_u((k+1/2)/N),\qquad
 F_u(v)=\pi(u-v)\cot\pi(u-v).
 \tag{9}
\]
The point \(u=v\) is removable. The logarithm is fixed by its real
value at \(1/2\), and has no divisor on \(\Omega\).

Choose a compact set of arguments in \(\Omega\), together with a
slightly larger compact set and paths from \(1/2\) of uniformly
bounded length inside it. On an additional fixed neighborhood there
are \(A_0,\rho>0\) with
\[
 \sup_{u,\ 0\le v\le1}|\partial_v^mF_u(v)|
                         \le A_0m!\rho^{-m}.
 \tag{10}
\]
Indeed the nonremovable poles have positive distance from this
compact product; Cauchy's estimate gives (10).
All actual local arguments used below lie in such a common set.

Midpoint Euler--Maclaurin with \(q\) even corrections has the
periodic Bernoulli remainder bound
\[
 |\mathfrak r_{q,N}(u)|
       \le A_1N\,\frac{(2q)!}{(2\pi\rho N)^{2q}}.
 \tag{11}
\]
This follows by integrating the \(2q\)-th derivative against the
translated periodic Bernoulli function and using
\(\sup|B_{2q}(\{v\})|/(2q)!\le4/(2\pi)^{2q}\).
Including or omitting the last endpoint correction only changes
the constant in (11). The identities
\[
 \int_0^1F_u(v)\,dv=J'(u),\qquad
 \partial_v^{2q-1}F_u(1)-\partial_v^{2q-1}F_u(0)
                                      =J^{(2q+1)}(u)
 \tag{12}
\]
are exact. Integrate along the fixed paths and use
\(J^{(2q)}(1/2)=0\) and (9). Thus the logarithmic coefficients
are exactly
\[
 \ell_{2q-1}(u)=
       \frac{B_{2q}(1/2)}{(2q)!}J^{(2q)}(u),\qquad
 \ell_{2q}(u)=0.
 \tag{13}
\]
There is no unknown integration constant.

Cauchy bounds for \(J\), (11), and one extra correction when
necessary give constants \(A,a_0>0\) such that
\[
 |\ell_j|\le A^{j+1}j!,\qquad
 \left|\log H_N-\tfrac12\log N-NJ
                  -\sum_{j=1}^{L-1}\ell_jN^{-j}\right|
                    \le A^{L+1}L!N^{-L}
 \tag{14}
\]
for \(1\le L\le a_0N\). To check the powers explicitly, the
remainder indexed by \(2q\) has power \(N^{-(2q-1)}\).
Choose \(2q=L+1\) or \(L+2\), according to parity, retaining
only corrections of order below \(L\). The extra factorial
factors \(L+1,L+2\), and the possible extra \(N^{-1}\), are
absorbed into \(A^{L+1}\) when \(L\le a_0N\). The same bounds
hold on slightly larger argument sets before taking any fixed
derivatives.

Replacing \(u\) by \(u+\alpha/N\), for bounded fixed offsets
\(\alpha\), preserves (14) after the exact leading action and
order-zero factor are extracted. This follows by Taylor expansion
on the same larger neighborhood. A coefficient at total order \(r\)
uses a derivative of a coefficient of order \(j\le r\);
its bound is at most \(A^{r+1}j!(r-j)!\), times an exponential
combinatorial factor, and hence at most \(A'^{r+1}r!\).
The Taylor remainders obey the same estimate. In particular this
includes the uncentered \(G_N(Nu)=H_N(u+1/(2N))\).

We record why exponentiating (14) preserves this quantitative
order, rather than only a fixed-order formal expansion.
Let \(Q_{L-1}(h)=\sum_{j=1}^{L-1}\ell_jh^j\). On
\(|h|\le (A_2L)^{-1}\), with \(A_2\) sufficiently large,
\[
 |Q_{L-1}(h)|\le
       A\sum_{j=1}^{L-1}(A/A_2)^j\,j!/L^j
                         \le C.
 \tag{15}
\]
The same circle bounds its exponential and inverse. Their Taylor
tails at \(h=1/N\), when \(L\le a_1N\) and \(a_1\) is sufficiently
small, are at most \(C(A_2L/N)^L\).
The elementary bound \(L^L\le e^L L!\) converts this to
\(C^{L+1}L!N^{-L}\). The exact error in (14) changes the
exponential by this same bound: its size and the truncated
logarithm are uniformly bounded after \(a_1\) is reduced.
Finite products and inverses satisfy the same estimate.
Their formal coefficients have the bound \(C^{r+1}r!\), since
\(\prod j_i!\le(\sum j_i)!\) and the number of compositions
is at most exponential in the total order. This argument uses
a polynomial in the auxiliary variable \(h\); it does not
assume that \(G_N\) is analytic as a function of \(1/N\).

At an original retained edge the literal factorial interpolation is
\[
 E_N(x,t)=
 \frac{N}
 {H_N(1/2-x+t/(2\pi))H_N(1/2-x-t/(2\pi))G_N(Nx)^2}.
 \tag{16}
\]
It equals \(e_a(-2\cos t)\) at \(x=a/N\). The numerator \(N\)
is the exact complementary factorial product, not an asymptotic
normalization. On the common strict neighborhoods furnished by
the doubled-cube geometry, (14)--(15) therefore give
\[
 E_N(x,t)=\frac{e^{Nb(x,t)}}{2N\sin\pi x}\,a_N(x,t),
 \quad
 \left|a_N-\sum_{j<L}a_jN^{-j}\right|
       \le C^{L+1}L!N^{-L},\quad |a_j|\le C^{j+1}j!.
 \tag{17}
\]
Here \(a_0=1\), and \(b\) is exactly the original phase of the
regular low-source proof. Its marking is fixed at imaginary
angles by the positive products and continued inside these same
regular neighborhoods. All factorial arguments have a fixed
bulk margin, even at zero heights. No continuation across a
factorial wall, no free-cardinal replacement, and no estimate
at an index endpoint is used in (17).

## 3. Growing-order analytic Gaussian remainders

We give the quantitative local integration step. Suppose an exact
amplitude \(a_N(w,\theta)\), holomorphic on a fixed complex
neighborhood of \(w=0\) and a parameter set, satisfies the bounds
in (17) there. Suppose the local phase has a nondegenerate
critical point with uniform analytic neighborhoods and a contour
through it which can be put into
\[
                         W(\theta)-|w|^2/2,
                   \qquad w\in\mathbb R^d,\quad |w|<r.
 \tag{18}
\]
Assume its remaining actual contour pieces have a fixed phase
loss and a polynomial bound for the exact amplitude. Then its
normalized Gaussian expansion has coefficients \(g_j\) and
remainder
\[
 |g_j|\le C^{j+1}j!,\qquad
 \left|(N/2\pi)^{d/2}e^{-NW}I_N
                     -\sum_{j<L}g_jN^{-j}\right|
          \le C^{L+1}L!N^{-L}+Ce^{-\delta_1N}
 \tag{19}
\]
for \(L\le a_2N\). Powers and fixed constants in the density may
of course be restored outside this formula.

Here is a proof including the growing-degree tails. Analytic Morse
coordinates can be chosen with fixed radii on a finite parameter
cover. One construction solves the first critical equation by the
implicit function theorem, completes the first square with its
analytic nonzero square root, and repeats on its Schur complement.
At the base the negative real Hessian fixes the square roots and
orientation. Invertibility and compactness give common smaller
radii and uniform holomorphic Jacobian bounds. Multiplying by
that Jacobian preserves (17).

On a complex ball of radius \(R>2r\), Cauchy's estimate bounds
the Taylor terms of \(a_j\) by
\[
                     C^{j+1}j!\,(C/R)^m|w|^m
 \tag{20}
\]
at total degree \(m\), absorbing the polynomial number of
multiindices into \(C^m\). In the \(N^{-j}\) amplitude term
retain degrees below \(2(L-j)\). Its Taylor remainder on
\(|w|\le r\), after reducing \(r/R\), is bounded by
\[
                C^{j+L-j+1}j!|w|^{2(L-j)}
 \tag{21}
\]
with the fixed radius powers included in \(C\).
Normalized Gaussian integration of \(|w|^{2q}\) is at most
\(C^{q+1}q!N^{-q}\). Thus the contribution of (21), multiplied
by \(N^{-j}\), is at most
\[
                C^{L+1}j!(L-j)!N^{-L}
                         \le C^{L+1}L!N^{-L}.
 \tag{22}
\]
Summation over \(j<L\) only changes \(C\). The exact symbol
remainder in (17) has the same bound after Gaussian integration.
Only even total Taylor degrees survive integration over
\(\mathbb R^d\). Their moments give the coefficient estimate
in (19) by the same inequality with \(j+q\) fixed.

Extending these Taylor polynomials from the local ball to
\(\mathbb R^d\) is harmless uniformly for \(L\) growing linearly
with \(N\), for the following reason. On \(|w|\ge r\), split
\[
 e^{-N|w|^2/2}\le e^{-Nr^2/4}e^{-N|w|^2/4}.
 \tag{23}
\]
The normalized moment of degree \(m\ge1\) for the remaining
Gaussian is bounded by
\[
                  C_d\{C_d\sqrt{(m+d)/N}\}^{m};
 \tag{24}
\]
this is the elementary radial Gamma integral, or the product
one-variable even-moment formula with Cauchy--Schwarz for odd
degrees. The degree-zero moment is bounded by a fixed constant.
Every retained term has \(j\le L\) and \(m\le2L\).
Combine (20), (24) and
\(j!N^{-j}\le(j/N)^j\) for \(j\ge1\).
If \(L\le a_2N\) with \(a_2\) sufficiently small, all these
factors are uniformly bounded, except for a polynomial in \(L\)
from the number of terms. This polynomial is absorbed in half
the exponential loss in (23). For the finitely many small
degrees the same assertion follows directly from their moments.
This proves a bound \(Ce^{-\delta_2N}\) for the sum of all
Taylor tails, with \(\delta_2>0\) independent of \(L\).
The actual contour complement retains its own fixed loss.
Together with (22) this proves (19).

For small complex parameter changes the Morse contour is the image
of the same real ball in (18). Cauchy's theorem supplies its local
connectors, whose strict base losses persist on a smaller parameter
domain. Thus (19) is a holomorphic bound on a fixed larger domain,
available for later Cauchy division and derivatives. It is not
merely an estimate at real parameter points.

## 4. Applying the estimate to the actual fixed-face contours

We specify the source contours so that the local lemma does not
replace a missing global transport argument. At an effective-charge
base point \(\boldsymbol\lambda^0\in[0,2]^S\), let
\(A=\{v:\lambda_v^0=0\}\) and keep
\[
 C_v^0=[-\pi,\pi]-iH_v(\boldsymbol\lambda^0),\qquad
 \mathcal P_N^0(\boldsymbol\lambda;\mathbf u)=
 \left(\frac{iN^2}{2\pi}\right)^s
 \int_{\prod C_v^0}\prod_v\sin t_v
          \prod_e K_N^{\rm low}(t_v,t_w)
                           e^{-iN\boldsymbol\lambda\cdot\mathbf t}
                                  d\mathbf t .
 \tag{25}
\]
At integer \(N\boldsymbol\lambda\), this is exactly the original
principal full-normal Fourier block. Off that lattice it is the
specified fixed-contour interpolant. Its use is justified in the
zero-endpoint and full-grid sources, not by a symmetry assumption
about the off-lattice cosine source.

The following margins in those proofs can all be chosen fixed on
a finite cover of the doubled cube:

1. The wire maxima lie in closed intervals strictly inside
   \((0,1/2)\). All omitted low indices have a strict phase gap.
2. For retained indices the full angular integrand has a unique
   maximum at \(\Re\mathbf t=0\); outside a small neighborhood
   its loss is uniform, including when some heights vanish.
3. The exact index-cotangent rectangles have half-grid vertical
   sides near fixed endpoints and fixed small imaginary heights.
   Their nonconstant modes decay as \(e^{-2\pi N\epsilon}\).
   The possible phase growth there is \(O(N\epsilon^2)\), so
   choosing \(\epsilon\) small preserves a strict loss.
4. The retained constant modes give \(N\) times each wire
   integral. Its endpoint connectors and those of the angular
   contour keep their fixed losses under small complex parameter
   changes.

These are estimates for the exact source before an asymptotic
amplitude is discarded. Their polynomial prefactors and gaps do
not depend on the truncation order. The factorial proof in Section 2
applies on the larger compact neighborhoods of the retained pieces.

For precision one may perform the local Gaussian step jointly.
First use the fiberwise analytic Morse coordinate for each wire
phase \(Q_e=b(x_e,t_v)+b(x_e,t_w)\). It changes that phase to
\(\psi(t_v,t_w)-\xi_e^2/2\). Then apply the angular Morse
coordinates to \(\sum_e\psi-i\boldsymbol\lambda\cdot\mathbf t\).
This gives exactly \(W-(\sum_e\xi_e^2+\sum_v y_v^2)/2\).
All coordinates and Jacobians have fixed analytic neighborhoods;
the sequential contour changes are the ones already justified
by the margins above. The resulting one joint Gaussian has
dimension \(e+s\) and an exact amplitude satisfying (17).
In particular an error in a wire expansion is not estimated on
an unrelated angular contour.

The source powers are \(N^{2s}\) from (25), \(N^e\) from the
cotangent constant modes, \(N^{-2e}\) from the paired exact
factorials, and \(N^{-(e+s)/2}\) from the joint Gaussian.
Their product is \(N^{-p}\). By (19),
\[
 N^p e^{-NW}\mathcal P_N^0
   =\sum_{r=0}^{L-1}\mathfrak a_rN^{-r}+E_{N,L},\qquad
 |\mathfrak a_r|\le C^{r+1}r!,\quad
 |E_{N,L}|\le C^{L+1}L!N^{-L}+Ce^{-\delta_3N}
 \tag{26}
\]
on a fixed complex neighborhood of the face base point, uniformly
for \(L\le a_3N\).

The coefficients in (26) are the same canonical coefficients as
in the fixed-order theorem: for any fixed order the expansion just
proved has its original actual remainder and its original phase.
Uniqueness of asymptotic coefficients, or the explicit local
Taylor--Gaussian formula, identifies them on overlapping charts.
No \(N\)-dependent reassignment of a Fourier companion is made.

## 5. Odd division, companions, and the full source

For each \(v\in A\), the circle in (25) is real. Reflection makes
\(\mathcal P_N^0\) exactly odd in \(\lambda_v\); \(W\) is even
in that coordinate. The coefficients \(\mathfrak a_r\) are
therefore odd, and so is the exact normalized remainder
\(E_{N,L}\) for every \(L\), including \(L\) depending on \(N\).

Take a fixed larger face polydisk for (26), and a smaller one.
Successive Cauchy division of an odd holomorphic function by the
coordinates in \(A\) costs a fixed product of inverse radius
margins. For example \(f(z)/z=\int_0^1f'(tz)\,dt\) when
\(f(0)=0\). The other charges are bounded away from zero on
this patch. Consequently division by \(\prod_v\lambda_v\)
preserves both the factorial coefficient bounds and the
growing-order error in (26), with constants independent of
\(L,N\). In particular it does not cost \(N^{|A|}\).
A finite face/interior cover gives
\[
 \mathcal P_N(\boldsymbol\lambda;\mathbf u)=
 N^{-p}\left(\prod_v\lambda_v\right)e^{NW}
 \left\{\sum_{r<L}\beta_rN^{-r}
             +O\!\left(C^{L+1}L!N^{-L}+e^{-\delta_4N}\right)\right\}
 \tag{27}
\]
at every doubled-cube lattice point, with the divided expression
holomorphic on each face patch. The coefficients glue as in the
full-grid theorem. This proves (5).

The exact principal part of the original trace is
\(\sum_{\omega\in\{0,1\}^S}\mathcal P_N(\boldsymbol\lambda^\omega)\).
Both identical companions at any unit coordinate are retained.
The leading \(\beta_0\) already contains the factor \(2^{-s}\).
In particular no extra cosine factor is inserted in (27).

On a fixed complex outside polydisk the adopted action estimate is
\[
 \Re\{W(\boldsymbol\lambda^\omega,\mathbf u)-W(\mathbf c,\mathbf u)\}
               \le-2h_0\sum_{\omega_v=1}(1-c_v),\qquad h_0>0.
 \tag{28}
\]
For each reflected coordinate its normalization factor obeys
\[
 \frac{2-c_v}{c_v}e^{-2h_0N(1-c_v)}
 \le3\quad(c_v\ge1/2),\qquad
 \le2Ne^{-h_0N}\quad(1/N\le c_v<1/2).
 \tag{29}
\]
Thus all branch coefficients and remainders in (27), after
normalization by the common reference in (6), obey the same
Gevrey estimate. There are only \(2^s\) branches, independently
of \(L,N\). This proves the assertions in (6) for the principal
part, uniformly through all mixed zero/unit corners.

The rest is the actual source remainder, not a formal symbol
error. The full-grid proof bounds all higher trace aliases by
\(CN^A e^{N(M(\mathbf c)-\delta_{\rm alias})}\) and the entire
high Newton complement by
\[
 CN^A e^{N(M(\mathbf c)-\gamma)},\qquad
 \gamma=M_\infty-4\operatorname{arsinh}(2-\sqrt3)>4/99.
 \tag{30}
\]
These are uniform for the complete nonzero grid at both parities.
They retain the shared indices, the original normal multipliers
and the ordinary boundary polynomial. The original degree bound
continues them to a fixed small complex outside polydisk with
smaller positive gaps. Division by \(\prod c_v\ge N^{-s}\)
costs only a fixed polynomial; reduce the gaps once more to
absorb it. All these steps are independent of \(L\).
Combining (27)--(30) proves (6) for \(Z_N\) itself.

Separate evenness in every outside angle holds for the exact
source, all phase and coefficient functions, and all errors.
They descend holomorphically near completeness through
\(z_w=-2\cos u_w\). Cauchy's estimate on fixed nested spectral
polydisks therefore gives the claimed ordinary boundary derivative
bounds after extracting the displayed reference factor. No growing
order of boundary differentiation is asserted.

## 6. Optimal truncation and the reconstruction budget

Choose \(a_*>0\) smaller than the constants allowed in Sections
2--5, and also with \(Ca_*\le1/4\) for the final \(C\) in (6).
For \(N\) large enough that \(L_N=\lfloor a_*N\rfloor
\ge a_*N/2\), the elementary inequality \(L!\le L^L\) gives
\[
 C^{L_N+1}L_N!N^{-L_N}
       \le C(Ca_*)^{L_N}
       \le C\exp[-(a_*/2)\log4\,N].
 \tag{31}
\]
Any fixed
\[
             0<\kappa\le
                    \min\{\delta,(a_*/2)\log4\}
 \tag{32}
\]
is therefore valid after a harmless enlargement of \(C_*\).
This proves (7). The constants entering \(C,a_*,\delta\) are
the factorial Cauchy radius in (10), the finite Morse neighborhood
radii and Jacobian bounds, the fixed contour losses, the face
division margins, and the two actual source gaps in (30).
The choice requires all of them; the fixed lower bound on
\(\gamma\) alone is not a lower bound on \(\kappa\).

The sum of terms of orders \(1,\ldots,L_N-1\) in (6) is
\(O(N^{-1})\): the bound \(C^{r+1}r!N^{-r}\) has successive
ratios \(C(r+1)/N\le1/2\) after decreasing \(a_*\) if needed.
The uniform unit \(\mathcal B_{N,0}\) consequently also controls
the optimally truncated expression. This does not replace the
exact finite companion sum by one of its terms.

At complete outside angles,
\(M(\mathbf c)\le M(\mathbf0)=eM_\infty\) and
\(\prod_vc_v\le1\). Hence (7) supplies the actual entire sample
array with the absolute error
\[
 \max_{\mathbf J\in\{1,\ldots,N\}^S}
       |Z_N(\mathbf J/N;\mathbf0)-\mathscr S_N(\mathbf J/N;\mathbf0)|
                    \le C_*N^{-p}e^{N(eM_\infty-\kappa)}.
 \tag{33}
\]
Apply the exact one-block full-normal reconstruction to these
approximate samples. For the canonical finite polarized
observation at \(y_v=1-\chi_v\), its error is at most
\[
 C_*N^{s-p}\prod_v(1+2|y_v|)
 \exp\left\{N(eM_\infty-\kappa)
                    +\pi D\sum_v(-\sigma_v\Im y_v)_+\right\}.
 \tag{34}
\]
In particular a comparison with a proposed target real action
\(A_{\rm target}\) requires, on the desired target domain,
\[
       \kappa>
       eM_\infty-A_{\rm target}
                       +\pi\sum_v(-\sigma_v\Im y_v)_+.
 \tag{35}
\]
Nothing in the proof asserts (35), or identifies the asymptotics
of the reconstructed approximation itself. Exact endpoint terms
of the canonical finite observation can retain the complete
action. The contour-polarized family is a different family.

Thus (7) is an exponentially accurate actual charge-grid theorem,
with a quantified positive error rate obtained from fixed analytic
data. It does not assert a single geometric asymptotic for the
canonical finite observation, a global heat initializer, or coverage
of arbitrary short fillings. Exact zero samples \(J_v=0\) remain
excluded; the \(N^s\) reconstruction block needs only \(1\le J_v\le N\).

## Direct sources and coverage

The complete final proof and all directly used source versions are
read and their hashes checked before author freeze.

- [Full charge-grid source](research_full_charge_grid_zero_power_source.md),
  SHA256 89f6f0e77cef5a74c433aa7ade37b4441521629a935a352da0853fc39bf5a5c9:
  original source, doubled-cube geometry, companion normalization,
  actual higher-alias and high-sector gaps, and boundary continuation.
- [Centered exact factorial](research_two_square_factorial_amplitude.md),
  SHA256 995c38d1cc6fcd5a1a1306601778ce6068b5f1d766364216e7cdd933f344290f:
  exact midpoint logarithmic derivative, normalization and fixed
  primitive coefficients used in Section 2.
- [Regular low source](research_regular_zero_subtree_low_source.md),
  SHA256 06e4b7c14e3a61616dea61642103e2d2803709fcd465ae9860258119db3299d1:
  original factorial interpolation, cotangent rectangles, local
  wire and angular contours, strict complementary losses.
- [Zero-charge face interpolation](research_zero_charge_uniform_low_source.md),
  SHA256 d4412c67ca520894840b80e390058ce2438af906ea13f719abb5def5c252496d:
  fixed face-centered circles, exact parity, zero-height tail
  estimates and holomorphic division on a larger face polydisk.
- [Finite quantitative reconstruction](research_finite_charge_quantitative_reconstruction.md),
  SHA256 5d13994e8b6d2dc3c54d1fcf15d1f9435efc2d26921046bca14b90d22e75bf23:
  exact one-block tensor reconstruction and its directional norm.

Coverage was checked in the optimal-truncation sections of
research_cap_cross_full_low_demand_subexponential_contraction.md,
research_cap_cross_two_spectrum_neighborhood_stability.md,
actual_pretzel_mixed_inner_source_wkb.md, and
papers/conway-asymptotics/leaf.tex. Those narrower interpolation
arguments are credited above; none is an additional premise of
this proof. The growing-order estimates here are proved directly
from (9) and the stated actual contours.

Only written mathematics, text reads and file hashes are used.
No mathematical program, numerical experiment, test or compilation
is run. Frozen notes, manuscripts and public documents are unchanged.
