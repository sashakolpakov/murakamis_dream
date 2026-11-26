# Short contractions from physical envelopes and exact source windows

Private written proof, 17 November 2026.

The input estimates in this theorem concern the actual physical values
and first normals, together with one exact holomorphic representative
on a selected window. No estimate of the canonical polynomial between
the other physical nodes, or on a whole complex strip, is required.
Explicit inequalities for the input phases pay the complete selected
window and the untouched physical rows. The outgoing physical envelope
then follows from the original row profile, including its independent
normal. A nonzero local outgoing scalar is constructed and repaired.

This is a criterion for a fixed short contraction, and hence for a
finite tree whose successive contractions pass the stated checks.
It does not assert that arbitrary fixed short trees pass those checks.

## 1. The original source and the input class

Put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad \eta=(-1)^D,\qquad
 c_j=2\cos((2j+1)\pi/N),\quad J=\lfloor D/2\rfloor,
\]
\[
 P_N(C)=2T_N(C/2)+2,\quad C(t)=-2\cos t,\quad
 \tau_j=\pi-(2j+1)\pi/N,\quad
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f .
 \tag{1}
\]
The multiplicity \(\nu_j\) is two except at the odd-level node
\(c_J=-2\), where it is one. Write
\[
 F_j(C)=K_N(c_j,C),\qquad
 G_j(C)=\partial_wK_N(w,C)|_{w=c_j}
 \quad(\nu_j=2).
 \tag{2}
\]
All polynomials, crossings, turns and traces below are the original
ones. In particular \(Tf(w)=\phi_N^{(C)}[f(C)K_N(C,w)]\).

Let \(H_{a,N}\), \(1\le a\le m\), be actual boundary polynomials,
and let \(p\) be any fixed signed integer. The output is
\[
 H_{\mathrm{out},N}(w)
   =T\!\left(R^p\prod_{a=1}^m H_{a,N}\right)(w).
 \tag{3}
\]
Its ordinary degree is at most \(D\). Products in (3) are formed
before the full original trace. No child normal is omitted.

Here are the input hypotheses. They concern known incoming sources,
not the unknown output in (3).

**Physical envelopes.** There are constants \(M_a\in\mathbb R\),
\(\gamma_a\ge0\), and a sequence \(\epsilon_N\to0\), such that
\[
 |\partial_C^b H_{a,N}(c_j)|
 \le \exp\{N\epsilon_N+N[M_a-\gamma_a(1-\cos\tau_j)]\},
 \qquad 0\le b<\nu_j .
 \tag{4}
\]
Increasing \(\epsilon_N\) absorbs every fixed polynomial factor.
The constants and starting levels may depend on the fixed children.

**Exact window scalars.** Fix \(0<T<\pi\), \(h>0\), with buffers,
and let
\[
 \mathcal R=\{s-iy:|s|\le T,\ 0\le y\le h\}.
 \tag{5}
\]
The image \(C(\mathcal R)\), with a fixed neighborhood, lies in
\(\{\Re C<2\}\). For every child there is a spectral holomorphic
function \(\mathcal H_{a,N}(C)\) on a neighborhood of this image
and of the real seed window. Its angular pullback
\(f_{a,N}(t)=\mathcal H_{a,N}(C(t))\) is even. On a slightly
larger real window than \([-T,T]\), exactly
\[
 \partial_C^b\mathcal H_{a,N}(c_j)
       =\partial_C^b H_{a,N}(c_j),\qquad b<\nu_j .
 \tag{6}
\]
The functions are units on a buffered neighborhood of the rectangle.
There are even holomorphic input phases \(W_a(t)\), with
\(\Re W_a(0)=M_a\), and consistent logarithms such that
\[
 \log f_{a,N}(t)=N W_a(t)+o(N).
 \tag{7}
\]
The \(o(N)\) is uniform with every fixed buffered derivative used
below. A spectral phase near \(C=-2\) is intended: evenness is
actual angular evenness, not a claim about an uncentered degree
coordinate. The same spectral representative is used along the
entire selected window and its end connectors.

The class permits subexponential normalized units. Polynomial
prefactors and \(N\)-dependent logarithmic amplitudes are included.
There is no assumption of a limiting \(N\)-independent amplitude.
Any level-dependent scalar unit carrier remains in the exact
function and integral. Its logarithm in (7) may be chosen bounded;
this bookkeeping does not alter the explicit original crossing
carrier in (18),(19).
The theorem is also uniform over compact input parameter families
when all stated buffers and strict margins are uniform. In that
form the phases and \(M_a\) may follow those parameters with \(N\).

## 2. Explicit checks at the new vertex

Keep the original edge profile and its additive constant:
\[
 \Psi_x(C)=2\int_0^x
       \operatorname{arsinh}\!\left(\tfrac12\sqrt{2-C}\cot\pi r\right)dr,
 \qquad
 \psi(t,u)=\Psi_{(\pi-|u|)/(2\pi)}(C(t))
 \quad(u\ \hbox{real}).
 \tag{8}
\]
It extends evenly near \(u=0\). Put
\[
 P(t)=\sum_a W_a(t)+\psi(t,0),\qquad
 \Phi(t)=P(t)+\frac{ip t^2}{4\pi}-it .
 \tag{9}
\]
Require the following strict inequalities on the fixed buffered
rectangle, with some \(\kappa,\delta>0\):
\[
 \Re P''(t)\le-\kappa ,
 \tag{10}
\]
\[
 t_*=s_*-ih,\quad |s_*|<T,\qquad \Phi'(t_*)=0,\qquad
 M_{\mathrm{out}}=\Re\Phi(t_*),
 \tag{11}
\]
\[
 \Re P(T)=\Re P(-T)<M_{\mathrm{out}}-4\delta ,
 \tag{12}
\]
\[
 \sum_a M_a-\Bigl(\sum_a\gamma_a\Bigr)(1-\cos T)+\psi(T,0)
                         <M_{\mathrm{out}}-4\delta .
 \tag{13}
\]
The distance \(T-|s_*|\) is positive and fixed. All these conditions
are statements about the given input phases, their known physical
envelopes, and the original edge. The power \(p\) need not be long
or positive. Existence of the point in (11) is part of the check.

They are not consequences of local Schur accretivity alone.
In particular (13) pays the untouched original rows, and (12)
pays the tops of the two actual midpoint end connectors.

**Theorem.** Under (4)--(13), there is a constant \(c_{\mathrm{out}}>0\)
and a sequence \(\widetilde\epsilon_N\to0\) such that, for every
physical outgoing row and every original required normal,
\[
 |\partial_w^bH_{\mathrm{out},N}(c_j)|
 \le
 \exp\{N\widetilde\epsilon_N+
       N[M_{\mathrm{out}}-c_{\mathrm{out}}(1-\cos\tau_j)]\},
 \qquad b<\nu_j .
 \tag{14}
\]
There is a fixed spectral neighborhood of \(-2\) with a holomorphic
scalar \(B_N(w)\), a holomorphic phase \(\mathcal S(w)\), and
a holomorphic actual action \(\Lambda_N(w)=\mathcal S(w)+o(1)\),
such that \(B_N\) is a unit and has the Gaussian expansion (33)
below. Here \(\mathcal S(-2)=\Phi(t_*)\).

On a fixed sufficiently small physical fold window, \(B_N\) has
all the original values and first normals of \(H_{\mathrm{out},N}\)
up to an error with a fixed exponential gap. After choosing a
shorter window only after that gap, one spectral holomorphic unit
\(\mathcal H_{\mathrm{out},N}\) has those data exactly, satisfies
\[
 \log\mathcal H_{\mathrm{out},N}(w)
                         =N\mathcal S(w)+o(N),
 \tag{15}
\]
and obeys the same leading Gaussian formula. Its angular phase is
even and satisfies
\[
 \left.\frac{d^2}{du^2}\mathcal S(-2\cos u)\right|_{u=0}
          =-\frac{\cos(t_*/2)}{2\pi},\qquad
                 \Re\cos(t_*/2)>0 .
 \tag{16}
\]
The equality of source data in (15) is exact only on the specified
outgoing window. No equality to the canonical output at arbitrary
complex \(w\) is asserted.

## 3. Exact closed-window source and all outer rows

Choose \(T_N=T+O(N^{-1})\) at a full angular midpoint, with
\[
 (-1)^N\cos(NT_N)=1 .
 \tag{17}
\]
Use the real seed buffer in (6) and the rectangle buffer for this
rounding. The selected spectral rows are exactly
\(\mathcal I_N=\{j:0\le\tau_j<T_N\}\). At odd level its center
has multiplicity one. All remaining distinct rows are retained.

For a fixed outgoing physical row define \(L_{j,0}=F_j\) and,
when required, \(L_{j,1}=\widehat G_j\), the pole-free
Ward--Jacobi normal. At every child physical node it has exactly
the required value and first normal of \(G_j\). Therefore (6)
and the full product rule give the exact decomposition
\[
 \partial_w^b H_{\mathrm{out},N}(c_j)=O_{j,b,N}
 -\frac{N^2 C_{N,p}}{\pi i}
   \int_{\Gamma_N^-}
      \sin t\,W_N(t)e^{ipNt^2/(4\pi)}
      \left(\prod_a f_{a,N}(t)\right)L_{j,b}(C(t))\,dt ,
 \tag{18}
\]
\[
 C_{N,p}=q^{pD^2/4},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{19}
\]
The lower path \(\Gamma_N^-\) goes from \(-T_N\) down to
\(-T_N-ih\), across to \(T_N-ih\), and up to \(T_N\).
The term \(O_{j,b,N}\) is the literal original finite trace over
the outside rows. No endpoint or cut current has been set to zero.

To justify the normal replacement, the source identity is applied
only at the child nodes before their closed trace. A multiple of
the full relation has the requisite zero value and normal there.
This is not equality of \(G_j\) and \(\widehat G_j\) at a free
complex child color. In (18) the latter is an even holomorphic
angular function on the rectangle, so no spectral cut is crossed.
The upper half of the closed angular contour is paired by
\(t\mapsto-t\). The odd sine and reversed differential make its
integral equal to the lower half. This gives the displayed factor.
At the odd center it gives exactly one simple spectral value,
without an invented first normal.

For the outside rows the original local functional is
\[
 \mathcal R_{\ell,N}A
   =\eta\{(4-c_\ell^2)A'(c_\ell)-c_\ell A(c_\ell)\},
 \tag{20}
\]
or its one simple value. Expanding this derivative includes the
crossing derivative, every child derivative, and the child normal
of the outgoing edge. For \(b=1\) the latter is the original mixed
edge normal. All fixed crossing values have modulus one, and all
their physical first normals have polynomial cost.

The uniform two-real-row pressure theorem bounds every required
edge jet by a polynomial times
\(\exp[N\psi(\tau_\ell,\tau_j)]\).
Since \(\psi(t,u)\le\psi(t,0)\) for real arguments and
\(\psi(t,0)\) decreases with \(|t|\), (4), (13) and the
\(O(N)\) row count give
\[
 |O_{j,b,N}|
   \le \exp\{o(N)+N(M_{\mathrm{out}}-3\delta)\},
                         \qquad b<\nu_j ,
 \tag{21}
\]
uniformly over all outgoing rows, including both spectral ends.
The rounding in (17) consumes only a fixed constant in the bound.

## 4. Why one paid contour bounds every outgoing row

On a compact subset \(\mathcal K\Subset\{\Re C<2\}\), the all-row
Jacobi and Ward estimates give
\[
 |F_j(C)|+|\widehat G_j(C)|
       \le N^B e^{N\Re\Psi_{j/N}(C)}
 \tag{22}
\]
with the second term only at double rows. Fixed child derivatives
have an additional polynomial cost. There is no division by a
Jacobi root in this estimate.

There is \(c_{\mathcal K}>0\) such that
\[
 \Re\Psi_{1/2}(C)-\Re\Psi_x(C)
              \ge c_{\mathcal K}(1/2-x)^2,\qquad 0\le x\le1/2 .
 \tag{23}
\]
Indeed the integrand in (8) has strictly positive real part for
\(r<1/2\). Divided by \(1/2-r\), it has the positive limit
\(\pi\Re\sqrt{2-C}\) at the fold, uniformly on the compact.
Away from the fold compactness gives a positive lower bound;
near zero the logarithmic divergence only increases it.
Integration proves (23).
Since
\[
 \tfrac12-j/N=\tau_j/(2\pi)+1/(2N),
 \tag{24}
\]
this bounds the rows at their actual physical angles, with no
incorrect centering of an external spectral derivative.

On the lower horizontal, (10),(11) give
\[
 \Re\Phi(s-ih)
       \le M_{\mathrm{out}}-\tfrac{\kappa}{2}(s-s_*)^2 .
 \tag{25}
\]
At either midpoint vertical, exactly
\[
 |W_N(\pm T_N-iy)|
       =\frac{e^{-Ny}}{(1+e^{-Ny})^2}\le e^{-Ny}.
 \tag{26}
\]
The real unit-charge rate
\(\Re P(\pm T_N-iy)+p(\pm T_N)y/(2\pi)-y\)
is convex in \(y\), because its second derivative is
\(-\Re P''\ge\kappa\). At its upper endpoint (12) gives
a fixed loss. At its lower endpoint (25), and
\(T-|s_*|>0\), give a fixed loss as well. Thus both
entire original verticals have a strict loss from
\(M_{\mathrm{out}}\).

On the horizontal the exact denominator in (19) is
\[
 W_N(t)=e^{-iNt}\{1+O(e^{-Nh})\}.
 \tag{27}
\]
This bounds the sum of every nonunit alias, not a selected
finite truncation. On the verticals we used the full rational
kernel (26), including its real midpoint end.

Combine (7), (22)--(27) in (18). Every point of its central
contour gains the outgoing loss in (23). This gives
\[
 |\hbox{selected-window contribution}|
  \le \exp\{o(N)+N[M_{\mathrm{out}}-c_1(1-\cos\tau_j)]\}
 \tag{28}
\]
for some \(c_1>0\). Combine this with (21) and decrease
\(c_{\mathrm{out}}\) so that \(2c_{\mathrm{out}}<3\delta\).
This proves (14), including the original output first normal.
Only physical output data have been bounded; no interpolation
bound for the canonical polynomial off that grid was used.

## 5. The outgoing fold scalar and even-level normalization

Take a fixed short local descent arc \(\gamma_*\) around \(t_*\),
with fixed endpoints. It lies strictly below the real line.
The complete phase has a nonzero Hessian by (10). Standard local
holomorphic Morse coordinates give a fixed endpoint action gap.
Replacing a short part of the horizontal in (18) by this arc
retains two local connectors; their action is strictly below the
critical action. Shrink its neighborhood once to preserve these
gaps under a small complex outgoing variation.

The original positive pair at \((t_*,0)\) has a buffered product
chart: \(|\Re t_*|<\pi\), and
\(\operatorname{arsinh}(\tan(t_*/2))\) has imaginary part strictly
between \(-\pi/2\) and \(\pi/2\) on the original branch.
This is the positive return strip at complete second angle.
The exact short spectral edge construction supplies on
this arc and a fixed spectral neighborhood of \(-2\) one
holomorphic unit \(A_N(t,w)\), with
\[
 \log A_N(t,w)=N\Psi_{\mathrm e}(C(t),w)+o(N),
 \tag{29}
\]
including fixed derivatives and original phase constants.
Its unit assertion is the actual anchored regular-row comparison
used in the crossed-block source-window theorem, with the nonzero
child angle as degree variable. Its two-sided spectral repair is
exponentially smaller than that unit. Choose one product chart
on the short arc, so no chart-dependent integral is introduced.

On a fixed short outgoing fold window its line data are exact:
\[
 A_N(t,c_j)=F_j(C(t)),\qquad
 \partial_w A_N(t,c_j)=\widehat G_j(C(t))
                                      \quad(\nu_j=2).
 \tag{30}
\]
The first child-line window used in constructing this edge can
be chosen independently; (30) is an identity for the complex
child parameter on the whole arc.

At odd level \(c_J=-2\), so \(A_N(t,-2)=F_J(C(t))\).
At even level \(c_J=-2\cos(\pi/N)\), and
\(|c_J+2|=O(N^{-2})\). By (29) the logarithmic derivative in
\(w\) is \(O(N)\) on a buffered smaller neighborhood. Therefore
\[
 A_N(t,-2)=F_J(C(t))(1+O(N^{-1}))
 \tag{31}
\]
uniformly along the arc at even levels. This is a comparison
with the literal last physical row. It is not the false
identity \(A_N(t,-2)=K_N(-2,C(t))\) at a free complex color.
The last even row retains its independent normal, while the
odd center requires only its value.

Define the fixed-arc scalar by the original density,
\[
 B_N(w)=-\frac{N^2C_{N,p}}{\pi i}
   \int_{\gamma_*}\sin t\,W_N(t)e^{ipNt^2/(4\pi)}
           A_N(t,w)\prod_a f_{a,N}(t)\,dt .
 \tag{32}
\]
It is holomorphic and spectral in \(w\). Differentiating (32)
has no moving-endpoint term: both endpoints are fixed.

Choose the actual logarithms in (7),(29), and set
\[
 \Phi_N(t,w)=N^{-1}\log A_N(t,w)
       +N^{-1}\sum_a\log f_{a,N}(t)+\frac{ip t^2}{4\pi}-it.
 \tag{32a}
\]
Its limiting phase has the unique nearby critical point
\(t(w)\), with \(t(-2)=t_*\), on a sufficiently small fixed
spectral disk. The actual phase has a unique nearby
\(t_N(w)=t(w)+o(1)\). Put
\(\Lambda_N(w)=\Phi_N(t_N(w),w)\) and let
\(\mathcal S(w)\) be the corresponding limiting stationary value.
The fixed arc can be deformed inside its neighborhood to the
actual Morse arc. The two new endpoint connectors remain in
the fixed descent sectors and have a uniform action loss.
All these statements hold holomorphically on a smaller disk.

The full Gaussian evaluation is consequently
\[
 B_N(w)=
  \frac{iN^{3/2}}{\pi}C_{N,p}\sin t_N(w)
       \sqrt{\frac{2\pi}{-\partial_t^2\Phi_N(t_N(w),w)}}
       e^{N\Lambda_N(w)}(1+O(N^{-1})).
 \tag{33}
\]
The square root is fixed by the original oriented descent arc.
All its factors are units. In particular \(\Im t_*<0\)
prevents the sine from vanishing. The logarithmic amplitude
relative to \(e^{N\mathcal S}\) is \(o(N)\), with buffered
derivatives. Fixed actual-log derivatives are uniformly bounded,
so the Gaussian remainder in (33) is uniform.

For physical outgoing rows sufficiently near the fold, (30)
identifies the value and normal integrands in (32) exactly
with those in (18). The omitted horizontal portions,
all aliases, both original midpoint verticals, the two local
arc connectors, and the outside physical rows have the strict
gaps already proved. Their gaps persist uniformly after making
the outgoing real fold interval smaller. Thus, for a fixed
\(\gamma>0\),
\[
 |\partial_w^b(B_N-H_{\mathrm{out},N})(c_j)|
    \le \exp\{N\Re\mathcal S(c_j)-\gamma N+o(N)\},
                                      \qquad b<\nu_j .
 \tag{34}
\]
For the normal, the complete integrand difference is controlled
using (22), rather than differentiating a value estimate.
The physical error exponent is a complementary-contour gap.
It does not include an unproved off-grid canonical comparison.

Finally normalize the actual errors by \(e^{N\Lambda_N}\) and
use ordinary spectral Hermite interpolation. The short-window
operator costs
\(\exp[C\rho(1+|\log\rho|)N]\) when there are at most
\(\rho N\) rows, including their original multiplicities.
Choose \(\rho>0\) only after \(\gamma\). The correction is
exponentially small on the fixed smaller output disk:
\[
 \mathcal H_{\mathrm{out},N}
                =B_N+e^{N\Lambda_N}E_N,\qquad
                            \|E_N\|\le e^{-\gamma_1N}.
 \tag{35}
\]
It repairs precisely (34). It preserves the unit, (33), and
(15). The odd simple value is interpolated once.

Evenness of the original phase gives \(t_u(0)=0\).
Differentiating the stationary value then leaves only the
outgoing edge partial derivative at completeness, which is
exactly (16). Continuity gives strictly negative real angular
curvature on a fixed smaller output neighborhood.

## 6. Independently known input members

Physical rows of positive macroscopic degree belong to the input
class. More precisely, let \(H_N=F_{j,N}\), with \(j/N\) in a
compact subset of \((0,1/2]\). The all-row half-plane theorem gives
(7), with \(W(t)=\Psi_{j/N}(C(t))\), on every admitted rectangle;
the actual row is itself a unit there and needs no repair.
The original real two-row bounds, including normals, give (4).
To see its strict Gaussian loss, use the exact real-edge derivative
\[
 \partial_u\psi(\theta,u)
   =-\pi^{-1}\operatorname{arsinh}
                   (\cos(\theta/2)\tan(u/2)).
 \tag{36}
\]
Here \(\cos(\theta/2)\) has a positive uniform lower bound.
Integration on \(0\le u<\pi\) bounds the loss below by
\(c(1-\cos u)\). The physical half-step changes a macroscopic
first-row profile by \(O(N^{-1})\), absorbed by a fixed prefactor.
The full independent normal is supplied by the real two-row
theorem, not by differentiating a terminating value sum.
The constant row \(F_0=1\) is also allowed, with \(M=\gamma=0\).

There is a corresponding whole-physical-envelope assertion for
actual crossed outputs, rather than merely their local model.
Fix \(|p|\ge4\), and put
\[
 H_N(w)=\phi_N^{(C)}
          \left[R^pK_N(w,C)\prod_{i=2}^rF_{j_i}(C)\right].
 \tag{37}
\]
Suppose the other physical degrees have a uniform positive total,
\(\sum_{i=2}^rj_i\ge\delta_0N\). The bounded-minimax theorem
therefore applies uniformly at every outgoing physical row,
including its original first normal. Denote its selected action
by \(M_p(x)\), where \(x\in[0,1/2]\) is the outgoing degree
parameter, and write its selected spectral argument as \(C_p(x)\).
These arguments lie in one compact subset of \(\Re C<2\).
Stationarity gives, for \(0<x<1/2\),
\[
 M_p'(x)=
  2\Re\operatorname{arsinh}
       \left(\tfrac12\sqrt{2-C_p(x)}\cot\pi x\right)>0 .
 \tag{38}
\]
For negative powers use the exact conjugate source. The argument
of (23), now on this compact family of selected arguments, gives
\[
 M_p(1/2)-M_p(x)\ge c(1/2-x)^2 .
 \tag{39}
\]
Continuity supplies \(x=0\). The actual all-row value and normal
bounds of the initializer, together with (24),(39), prove (4)
for (37), with \(M=M_p(1/2)\) and a positive \(\gamma\).
There is no asserted envelope for a canonical off-grid polynomial.

If every nonzero fixed incident degree stays in a compact subset
of \((0,1/2]\), the complete-output saddle has a buffered positive
pair domain. Exact zero rows are omitted as factors \(F_0=1\).
The implicit function theorem and the initializer's nonzero
Hessian give the small regular outgoing family required by the
crossed-block source-window theorem. That theorem supplies (6),(7)
on its exact fold window and continued domain. Thus (37) is an
independently verified member of this weaker physical/window
class on those domains. For broader incident-parameter ranges,
one must separately check the regular-family hypotheses; (39)
by itself supplies only the physical envelope.

## 7. The final original scalar

At the root there is no outgoing edge. Keep the same actual
children and their hypotheses (4)--(7), and define
\[
 Z_N=\phi_N\!\left(R^p\prod_a H_{a,N}\right),\qquad
 P_0(t)=\sum_aW_a(t),\quad
 \Phi_0(t)=P_0(t)+\frac{ip t^2}{4\pi}-it .
 \tag{40}
\]
Suppose the same rectangle has
\[
 \Re P_0''\le-\kappa,\quad
 t_0=s_0-ih,\quad |s_0|<T,\quad
 \Phi_0'(t_0)=0,\quad M_0=\Re\Phi_0(t_0),
 \tag{41}
\]
\[
 \Re P_0(T)=\Re P_0(-T)<M_0-4\delta,\qquad
 \sum_aM_a-\Bigl(\sum_a\gamma_a\Bigr)(1-\cos T)
                                      <M_0-4\delta .
 \tag{42}
\]
These are exactly the input checks with the outgoing edge omitted.

**Corollary.** Under (40)--(42), the complete original scalar
\(Z_N\) is nonzero for all sufficiently large levels, with both
parities included. Define the actual phase and its nearby saddle by
\[
 \Phi_{0,N}(t)=N^{-1}\sum_a\log f_{a,N}(t)
                   +\frac{ip t^2}{4\pi}-it,\qquad
 \Phi_{0,N}'(t_{0,N})=0,\quad t_{0,N}=t_0+o(1).
 \tag{43}
\]
Then
\[
 Z_N=
 \frac{iN^{3/2}}{\pi}C_{N,p}\sin t_{0,N}
       \sqrt{\frac{2\pi}{-\Phi_{0,N}''(t_{0,N})}}\,
       e^{N\Phi_{0,N}(t_{0,N})}(1+O(N^{-1})).
 \tag{44}
\]
The root is fixed by the original oriented horizontal descent.
All input scalar carriers and the original \(C_{N,p}\) remain
in the formula.

**Proof.** The exact source decomposition is
\[
 Z_N=O_{0,N}
  -\frac{N^2C_{N,p}}{\pi i}
     \int_{\Gamma_N^-}\sin t\,W_N(t)e^{ipNt^2/(4\pi)}
                               \prod_a f_{a,N}(t)\,dt .
 \tag{45}
\]
This follows directly from (6) and the full derivative product
rule in the original local trace (20). At an odd simple node
only the original product value is used. The outside finite sum
\(O_{0,N}\) has a fixed exponential loss by (4),(42); its
crossing and every child first normal have been retained.

Horizontal strict concavity follows from (41). The top endpoints
are paid by (42), and the lower endpoints by their positive
distance from \(s_0\). Vertical convexity and the exact rational
bound (26) pay the entire two end connectors. Equation (27)
retains and bounds every nonunit alias on the horizontal.
All errors therefore have a fixed loss from \(M_0\).
The actual phases (43) converge with buffered derivatives, so
their local Gaussian gives (44). Their critical real action is
\(M_0+o(1)\), and their sine and Hessian are units. The paid
complement is exponentially smaller, even with the permitted
subexponential input amplitudes. No closing row or endpoint
current is deleted. \(\square\)

## 8. What is closed, and what must still be checked

The output has the same type of physical envelope, even
holomorphic exact-window scalar, and subexponential unit as the
inputs. The fixed output window and disk may be smaller; no
uniform lower bound for their sizes over arbitrary trees is
claimed. At the next vertex its required rectangle must lie
inside the available scalar domains, or inside a separately
proved continuation of those same scalars.

For a fixed finite tree, apply the theorem successively whenever
(5)--(13) can be checked from the already constructed inputs.
Only finitely many subexponential errors and fixed strict gaps
are involved. The same scalar is used on its one whole matched
window, so there is no internal patch interface in (18).
The actual derivative product rule, the Ward normalization,
every alias, all outer physical rows and all endpoint currents
are retained at each contraction.
If its final root satisfies (41),(42), the corollary closes the
actual scalar, with the nonzero coefficient (44). Thus the
criterion includes the prescribed final observation, rather
than only a norm or a family of open sources.

This strictly weakens the canonical whole-strip input used in
the archived high-valence and long-power recursions: neither
(4) nor (6),(7) estimates \(H_{a,N}\) at an untraced off-grid
color. Exact source-window representatives can therefore be
used without first controlling the canonical polynomial there.
The theorem also proves the outgoing envelope from its input
conditions; that envelope is not an assumed output property.

No claim is made that every fixed short tree satisfies the
rectangle, endpoint, outer-gap or domain checks. In particular
local positive geometry or an accretive Schur complement alone
does not verify (12),(13), nor transport an input scalar beyond
its proved domain. The result gives no new manifold-volume
identification and no arbitrary complex equality with an
ordinary free-boundary polynomial.

## Complete direct sources

The proof uses the following complete texts at their final pins.

* [Compact-positive residue control](research_compact_positive_contour_residue_control.md),
  SHA256 cac1016d5f515510b95071a25c8d97345b334043492a6b430c4e924f87d82bb0:
  exact Ward--Jacobi full jets, all-row half-plane bounds,
  original phase profile, complete real two-row mixed normals.
* [Overlapping spectral window transport](research_overlapping_spectral_window_seam_transport.md),
  SHA256 b19521e052b2e5db60abed1a284600467c7df56e319f4ebd8b29213ccfd481c7:
  original closed-window/lower-lens factor, both-parity
  multiplicities, exact spectator normal and endpoint scope.
* [Short spectral window repair](research_short_spectral_window_repair.md),
  SHA256 581ccd3ec9232a6aa1f42172fcff856f94a6d76efccc001bd411cf2243de2550:
  separately even exact edge lines, fold data and quantitative
  spectral Hermite repair after fixing the error exponent.
* [Crossed-block source windows](research_crossed_block_regular_saddle_source_window.md),
  SHA256 2ae68e5a2ae8a6aeb8b6fe4e791ed7638d3814280f579b22de3551910433cf47:
  actual anchored unit edge comparison on a positive saddle
  chart, actual logarithmic calibration and fixed physical
  window interpretation.
* [Bounded crossed minimax](research_crossed_physical_products_bounded_minimax.md),
  SHA256 07ad86f4b34ff057f6f1ebfad630b6b6b464aced08be875f047609aeda8e0bcf:
  the actual all-row scalar and independent-normal estimates,
  uniform selected half-plane saddle and branch used only
  to verify the crossed input members in Section 6.

Only written mathematics, source reads and metadata hashes are used.
No mathematical program, numerical computation, test or build is run.
Frozen sources and public manuscripts are unchanged.
