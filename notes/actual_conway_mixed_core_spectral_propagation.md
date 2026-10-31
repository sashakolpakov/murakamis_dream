# Spectral and physical-color propagation through mixed Conway cores

31 October 2026. source theorem. This proves the sharp
canonical spectral envelope and hereditary physical-color gap for an
unflagged component, at its actual closed-probe action. Together with the
proved decorated-character estimate, it gives a mutual induction through
fixed mixed flagged/unflagged reduced source trees. All original full
Hermite coordinates and finite targets are retained. No filled-volume
statement or change of marked geometry is inferred here.

The finite inputs are the [full-Hermite Newton and interpolation bounds](actual_conway_root_star_full_jet_localization.md),
the [exact root-character Fourier theorem](actual_conway_root_character_fourier_contraction.md),
and the [decorated-character coefficient duality](actual_conway_decorated_character_spectral_closure.md).
The separately proved [positive coefficient-cone theorem](actual_conway_unflagged_core_probe_bound.md)
supplies the original-action upper bound and strict high-sector gap. The
[reduced-hub adapter](actual_conway_reduced_hub_source_normal_form.md)
and [rigid-profile calculation](actual_conway_rigid_spine_and_flagged_tree_geometry.md)
supply the actual component typing and additive classical constants.
The [intrinsic component-probe geometry](actual_conway_unflagged_probe_geometry.md)
identifies the same pressure and the proper effective-leaf parameter ranges.

## 1. Exact finite norms and the regular-index extension

Let \(d=N-1\), \(M=\lfloor d/2\rfloor\), and use the original complete algebra, normalized
Newton polynomials \(B_r=\widehat B_r\), marked functional \(\phi\), and turn \(T\).
Write \(J(u)=\int_0^u\log(2\sin\pi t)\,dt\) and
\(g(u)=J(2u)-4J(u)\). The norm \(\|\cdot\|_{\mathcal J}\) records all nodal
values and first normals, with only the value at the odd simple node. Thus

\[
 T B_r=B_{d-r},\qquad \phi(B_rB_s)=\mathbf1_{r+s=d},\qquad
 D_j^\epsilon[E]=T(R^\epsilon L_jE),\qquad
 [B_r]D_j^\epsilon[E]=\phi(B_rR^\epsilon L_jE).
 \tag{1}
\]

Write \(w_{N,r}=B_r(-2)\) for \(r\le M\), and \(w_{N,r}=1\) for \(r>M\). All these weights are
strictly positive. The existing finite estimates are uniform at both
parities and all colors:

\[
 \|B_r\|_{\mathcal J}\le N^Cw_{N,r},\qquad
 \log w_{N,r}=Ng(r/N)+O(\log N)\ (r\le M),\qquad
 |[B_r]D_j^\epsilon[E]|\le N^C\|E\|_{\mathcal J}w_{N,r}.
 \tag{2}
\]

Here the last \(w_{N,r}\) is only the coefficient envelope: it is not a spectral
weight on the unreduced input. The canonical degree-\(<N\) representative \(H\)
obeys

\[
 |H(2\cos(\theta+iy))|\le N^C e^{N|y|}\|H\|_{\mathcal J}.
 \tag{3}
\]

The regular-index far-color estimate of the decorated-character theorem
holds on every fixed compact interval \(I\subset(0,1/2)\), including intervals away from
\(1/4\). Precisely, suppose an actual representative \(E_N\) has

\[
 |E_N(2\cos(\theta+iy))|
 \le \exp N\{c-c_E(\theta-\pi)^2+C_Ey^2+e_N\},
 \quad 0\le\theta\le2\pi,\ |y|\le y_E,
 \quad c_E\ge0,\quad e_N\to0.
 \tag{4}
\]

The empty input \(1\) is allowed. For any fixed \(I\) and \(\delta>0\), there is \(\eta>0\)
such that, uniformly in physical colors and \(\epsilon\in\{0,\pm1\}\),

\[
 r/N\in I,\quad N-j\ge\delta N
 \quad\Longrightarrow\quad
 |[B_r]D_j^\epsilon[E_N]|
 \le \exp N\{c+g(r/N)-\eta\}.
 \tag{5}
\]

Proof. The original low Newton polynomial has logarithmic strip action

\[
 b(u,\theta,y)=\int_0^u
       \log|2\cos(2\pi v)-2\cos(\theta+iy)|\,dv-2J(u).
 \tag{6}
\]

For \(u\in I\), circular rearrangement gives \(b(u,\theta,0)<g(u)\) away from
\(\theta=\pi\), uniformly on a closed angular complement. Near \(\pi\), with
\(z=\theta-\pi+iy\), its holomorphic action is

\[
 \mathcal B(u,z)=-J(1/2-u+z/(2\pi))-J(1/2-u-z/(2\pi))-2J(u),
 \qquad \mathcal B_{zz}(u,0)=-\tan(\pi u)/(2\pi)<0.
 \tag{7}
\]

The compact interval stays away from both index endpoints. The uniform
logarithmic-product upper estimate therefore gives constants \(c_I>0\),
\(C_I,y_I>0\) and \(e'_N\to0\) such that

\[
 |B_r(2\cos(\theta+iy))|
 \le w_{N,r}\exp N\{-c_I(\theta-\pi)^2+C_Iy^2+e'_N\}.
 \tag{8}
\]

This uses truncated-log Riemann upper bounds, so moving numerator zeros
are retained. Multiplying (8) by (4) supplies the exact root-character
Fourier theorem with input \(B_rE_N\) and reference \(c+g(r/N)\). Its missing
folded winding, both joining currents, and the physical R normal are
unchanged. That theorem proves (5). Fixed derivatives required there
follow by Cauchy on radius \(1/N\) in a smaller fixed strip, with polynomial
cost. For a fixed source the actual product representatives have degree
\(O(N)\); no continuation of an arbitrary physical-color array is used.

A preexisting norm loss in \(E_N\) is even simpler: (2) propagates it uniformly
at every output index, both low and high.

## 2. The proved coefficient-cone input

Let \(A\) be one fixed original unflagged component, with effective type-\(L\) inputs
\(F_i\), and set \(Q=T(A)\). The inputs retain their actual Newton coefficient
arrays, which may depend on arbitrarily many original physical colors.
Assume their uniform envelopes are

\[
 |[B_r]F_i|\le \exp N(c_i+e_N)
 \begin{cases}w_{N,r},&r\le M,\\1,&r>M.\end{cases}
 \tag{9}
\]

The original Newton multiplication constants are nonnegative; a turn is exact index
reversal. Taking coefficientwise absolute values therefore supplies a
positive state majorant without deleting any finite state or normal.
For the canonical output \(Q=\sum_rq_rB_r\), use the exact nonnegative
probe

\[
 W_N=\sum_{r\le M}w_{N,r}B_r+\sum_{r>M}B_r,
 \qquad
 \sum_rw_{N,r}|q_r|\le\phi(W_N A^{\mathrm{abs}}).
 \tag{10}
\]

Here \(A^{\mathrm{abs}}\) means the positive circuit with absolute input arrays; it
is not the absolute value of the output polynomial at a point. Equality
holds with the nonnegative majorant output coefficients. In particular
the original output reversal \(d-r\) is retained in the probe extraction.

The [independently proved cone theorem](actual_conway_unflagged_core_probe_bound.md)
gives the following input. Set

\[
 \Omega=\sum_i c_i+\Phi_{C(hA)},
 \tag{11}
\]

Here \(\Phi\) is the original complete action with unit type-\(L\) profiles \(g\); thus
\(\Omega\) is the intrinsic action \(\Omega_Q\). In (10):

* the sum of every sector with a high input index OR a high probe index
  is at most \(\exp N(\Omega-\gamma)\), for some \(\gamma>0\);
* the all-low sector has the original positive action as a uniform
  closed upper envelope on its compact finite state polytope;
* that upper-envelope action has one strict interior maximizer, of value \(\Omega\), whose
  probe index \(\beta\) and all effective input indices \(\alpha_i\) belong to
  \((0,1/2)\). Every fixed closed complement of that maximizer has a strict
  gap.

The fixed finite number of sectors and polynomial number of original
states are included in the uniform \(o(N)\) estimates. The effective modules need no independent physical alias
identity: the cone proof uses (9), the exact positive gate and the earlier
scalar supporting-plane certificates. It proves all these statements
without assuming a signed mixed-tree source bound. In particular the
upper-envelope action may have a strict maximizer even when the given
input arrays vanish identically.

## 3. Canonical Gaussian localization at the actual pressure

Using the theorem in §2, uniformly over all original physical colors,

\[
 \|Q_N\|_{\mathcal J}\le\exp N(\Omega+o(1)),
 \tag{12}
\]

and its canonical representative satisfies

\[
 |Q_N(2\cos(\theta+iy))|
 \le\exp N\{\Omega-c(\theta-\pi)^2+Cy^2+o(1)\}
 \quad (|y|\le y_0)
 \tag{13}
\]

with fixed \(c,C,y_0>0\). This is the sharp canonical spectral envelope at
\(\Omega_Q\). It does not add the uniform bare-turn cost \(2G_0\).

Proof. Equation (12) is (2) and (10). Choose a fixed compact interval \(I\)
about \(\beta\) strictly inside \((0,1/2)\). Decompose the actual state expansion
of the canonical output as \(Q=Q_{\mathrm{good}}+Q_{\mathrm{bad}}\), where \(Q_{\mathrm{good}}\) contains only
all-low states with \(r/N\in I\). The cone theorem and strict compactness
bound the weighted coefficient mass of \(Q_{\mathrm{bad}}\) by \(\exp N(\Omega-\gamma_1)\).
Hence its full-jet norm has that same gap. It is itself a canonical
polynomial, including its high-index part, so (3) gives

\[
 |Q_{\mathrm{bad}}(2\cos(\theta+iy))|
 \le\exp N\{\Omega-\gamma_1+|y|+o(1)\}.
 \tag{14}
\]

For the good part apply (8) to every output \(B_r\). The original positive
probe already contains exactly its factor \(w_{N,r}\), so summing costs
no additional exponential weight:

\[
 |Q_{\mathrm{good}}(2\cos(\theta+iy))|
 \le\exp N\{\Omega-c_I(\theta-\pi)^2+C_Iy^2+o(1)\}.
 \tag{15}
\]

Choose \(y_0<\gamma_1/4\) and \(c\le c_I\) with \(c\pi^2<\gamma_1/4\). Then (14) fits
below (13) with a fixed residual gap; (15) proves the remaining part.
Only canonical output polynomials enter (3), while input products may
remain unreduced. Thus no representative-dependent ellipse estimate has
been applied to an arbitrary quotient element.

## 4. Physical-color deficits of effective L modules

Suppose an original physical color \(j\) lies in input module \(i\). It suffices
that for every fixed compact interval \(I_i\) about its actual clean index
\(\alpha_i\), and every fixed \(\delta>0\), the module has a local coefficient loss

\[
 N-j\ge\delta N,\quad r/N\in I_i
 \ \Longrightarrow\ 
 |[B_r]F_i|\le
        \exp N\{c_i+g(r/N)-\eta_{i,\delta}\},
 \qquad \eta_{i,\delta}>0.
 \tag{16}
\]

The unconditional envelope (9) remains in force at other indices.
Then the actual unflagged output has a full-jet deficit

\[
 N-j\ge\delta N
 \quad\Longrightarrow\quad
 \|Q_N\|_{\mathcal J}\le\exp N(\Omega-\eta'_{i,\delta}),
 \qquad \eta'_{i,\delta}>0.
 \tag{17}
\]

Indeed contaminated sectors already have a fixed cone gap. In the clean
sector outside the \(\alpha_i\) window, the unique original maximizer gives
another fixed gap. Inside that window, replacing just the one input
coefficient envelope by (16) lowers every positive state weight by its
fixed exponential factor. Equations (2),(10) finish the proof. No bound
on the variance of an arbitrary spectator, no pointwise sign control,
and no independent alias provenance for the effective module is used.
There are finitely many original colors in a fixed component, so their
positive margins can be minimized.

For a genuine decorated module \(F_i=D_j^\epsilon[E]\), (9) follows from (2).
Its own character satisfies (16) by the regular-index theorem (5). A
physical-color deficit in \(E\) giving a full-jet loss yields (16), indeed a
uniform all-index loss, directly by (2). Thus descendant losses pass
through a complete unflagged component at its actual intrinsic action.
The local index \(\alpha_i\) can be above \(1/4\); no quarter-only estimate is used.

## 5. Mutual induction through the actual reduced source

The [finite reduced-hub decomposition](actual_conway_reduced_hub_source_normal_form.md)
expresses each fixed mixed strict source, rooted at a flagged character, as
alternating decorated type-\(L\) modules and unflagged components of the
kind covered by §2. The entirely unflagged case already has the completed
source estimates. Start with the empty input \(1\). At a decorated
module, multiply the actual child canonical representatives; their
full-jet rates add, their angular Gaussian envelopes multiply, and a
child deficit supplies a norm loss. Equations (2),(5) give its low/high
coefficient envelopes and all regular-index physical-color losses.
At an unflagged component, (12),(13),(17) give the output full-jet rate,
fresh Gaussian localization, and every descendant deficit. Iterate over
the fixed finite source. The classical rigid-spine identity identifies
its decorated constant with the sum of its satellites' actual \(\Omega\),
so this induction never inserts an artificial character or rate budget.

For a closing original character, the existing exact Fourier theorem
now supplies its own far-color loss and the norm bounds supply all
other color losses. The complementary-color expansion can then restore
the original all-core packet, as in the assembly.
Those final source and marked-filling adapters are not re-proved here.
The analytic induction uses the separately proved coefficient-cone theorem
and the original reduced-hub typing; it does not assume a prior full
mixed-tree source theorem.

This note does not promote a new global volume statement. All sources,
physical signs, levels and finite targets remain original. The input
and output constants may depend on the fixed finite component, and no
claim is uniform over trees whose size grows with \(N\).

## scope and preservation

The mutual induction uses exact normal-preserving probe weights and the canonical good/bad decomposition. It does not assume the signed mixed-source bound that it proves.

An arbitrary input can vanish. The propagation argument does not give a lower coefficient rate.