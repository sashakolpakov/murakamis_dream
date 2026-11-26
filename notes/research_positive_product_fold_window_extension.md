# Full physical fold windows on a positive product chart

Private written proof, 16 November 2026.

The common product baseline can be normalized through the simultaneous
complete fold using the actual three-fifths kernel theorem. This supplies
the missing nearby physical values and independent first normals, with
exponentially small normalized errors. The comparison uses the canonical
kernel only on a small complete bidisk. Outside that bidisk it uses the
actual physical-row bounds, rather than an off-grid bound for the canonical
kernel.

An exact two-line repair then includes a whole fixed fold window. A closed
contour around both angular lifts, with its factor one-half, retains every
double spectral normal and the odd simple value. No evenness of the
repaired representative or equality of arbitrary free-color functions is
asserted. Exterior sides and real interfaces remain.

## 1. Original data and the common baseline

Use the original normalization
\[
 N\ge2,\quad h=N^{-1},\quad \eta=(-1)^{N-1},\quad
 X_j=(j+\tfrac12)h,\quad C(X)=2\cos(2\pi X),\quad
 t(X)=\pi-2\pi X,\quad
 P_N(z)=2T_N(z/2)+2,
 \tag{1}
\]
and \(K_N(z,w)=\sum_{k=0}^{N-1}e_k(z)e_k(w)\). Put
\(J_N=\lfloor(N-1)/2\rfloor\). Its distinct physical rows are
\[
 c_a=C(X_a),\qquad F_a(w)=K_N(c_a,w),\qquad 0\le a\le J_N.
 \tag{2}
\]
For \(a\le\lfloor(N-2)/2\rfloor\), the original independent
normal is \(G_a(w)=\partial_zK_N(c_a,w)\). Retain the pinned
pole-free representative \(\widehat G_a(w)\). It has exactly the
value and required first spectral normal of \(G_a\) at every
physical second endpoint. It is holomorphic on
\(\mathbb C\setminus[2,\infty)\); it is not the canonical normal
polynomial at an arbitrary untraced endpoint.

Fix a positive pair and its product domains from the pinned product
gluing theorem. Shrink to buffered inner angular domains
\(\mathcal U_t,\mathcal U_u\) containing zero and the target.
They are bounded and connected, lie in the original angular strips,
and retain the single original phase \(\psi(t,u)\). All compact
estimates below are taken with fixed larger buffers in those domains.
The baseline of that theorem is denoted by \(H_N(t,u)\); it is
already phase normalized:
\[
 U_N(t,u)=e^{N\psi(t,u)}H_N(t,u),\qquad
 \sup_K|H_N|\le e^{o_K(N)}.
 \tag{3}
\]
The baseline is holomorphic through \((0,0)\), but this fact alone
does not prescribe any fold data.

Choose the common positive real seed intervals used to construct
\(H_N\) inside a sufficiently small complete disk. More precisely,
choose fixed numbers
\[
 0<\rho_0<\rho_1<R<3/5
 \tag{4}
\]
such that the closed \(R\)-disk lies inside both buffered inner
angular domains. The two positive real seed intervals lie in
\((0,\rho_0)\), with fixed positive length and all required
buffers. These choices are possible because the product domains
contain a neighborhood of zero. The common baseline theorem then
gives exponentially small errors in its two original bulk row
families, as holomorphic functions of the other parameter.

## 2. Actual complete-disk comparison

The pinned three-fifths theorem concerns the full canonical polynomial:
\[
 K_N(-2\cos t,-2\cos u)
   =N^{-3/2}a(t,u)e^{N\psi(t,u)}
                         (1+O_{\rm hol}(N^{-1})),
 \qquad a(t,u)\ne0.
 \tag{5}
\]
It holds on a neighborhood of the closed three-fifths bidisk, at both
parities and with all fixed ordinary spectral derivatives, including
the ramification at \(t=0\) or \(u=0\). In particular its normalized
value and fixed derivatives have polynomial bounds on our complete
bidisk.

**Lemma 1.** With fixed buffers for the radii in (4), there is
\(c>0\) such that
\[
 \partial_t^p\partial_u^q
 \left[H_N(t,u)-e^{-N\psi(t,u)}
                 K_N(-2\cos t,-2\cos u)\right]
                  =O_{p,q}(e^{-cN})
 \tag{6}
\]
uniformly for \(|t|,|u|\le\rho_1\), for every fixed \(p,q\).

**Proof.** On the two real seed grids the normalized difference
has exponentially small values, because the baseline's actual line
data are \(F_a\), and \(F_a(w)=K_N(c_a,w)\) exactly. Both
functions in (6) are bounded by \(e^{o(N)}\) on the buffered
complete bidisk, by (3) and (5).

Apply the two successive dense-grid estimates of the pinned endpoint-role
comparison. At the first stage subtract its exponentially small finite
sinc correction and use the disk Blaschke product for the remaining
exact zeros. Do the same in the second variable. The fixed angular
spacing is \(2\pi/N\), rather than \(1/N\); the affine coordinate
change (1) gives exactly the same estimate. This yields an exponentially
small bound on an open seed product, with a positive exponent independent
of \(N\). The common complete bidisk is connected and both normalized
functions have the required bounds there. A finite chain of buffered
complex balls propagates the estimate to its smaller closed bidisk.
Buffered Cauchy estimates prove all fixed derivatives. This is a
comparison of these two bounded functions, not uniqueness inferred
from finitely many samples alone. \(\square\)

For later use write \(\tau_a=\pi-(2a+1)\pi/N\ge0\). The
all-row theorem gives, uniformly over every physical row, the upper
bound with its own phase
\[
 |F_a(-2\cos u)|+|\widehat G_a(-2\cos u)|
                 \le e^{N\Re\psi(\tau_a,u)+o(N)}
 \tag{7}
\]
on every fixed compact second-angle domain in the original strip.
The normal term is used only at double rows. Fixed ordinary spectral
derivatives satisfy the same estimate. On a compact with
\(\Re(-2\cos u)<2\), the \(o(N)\) loss can be replaced by a
fixed power of \(N\). The actual midpoint relation in that source is
\(\Psi_{a/N}(-2\cos u)=\psi(\tau_a+\pi/N,u)\); its monotone
upper comparison gives (7) with \(\tau_a\), including the fold.
There is no replacement of the row action by its complete maximum.

**Lemma 2.** Uniformly over every double physical row with
\(0\le\tau_a\le\rho_0\),
\[
 e^{-N\psi(\tau_a,u)}
        [\widehat G_a(-2\cos u)-G_a(-2\cos u)]
                         =O(e^{-cN})
 \tag{8}
\]
on a fixed smaller complete disk in \(u\), with fixed buffered
derivatives. The positive exponent is uniform in the row and in parity.

**Proof.** Choose the disk in (8) with a larger buffer still inside
\(|u|<R\), and keep \(\tau_a\le\rho_0<\rho_1\). This is a
compact subset of \(\Re(-2\cos u)<2\). Formula (7), including its
polynomial normal loss, bounds the first term after normalization.
The ordinary first-color derivative assertion of (5) bounds the
canonical \(G_a\) by the same phase with a polynomial loss, uniformly
even as \(\tau_a\to0\).

The normalized difference is holomorphic and polynomially bounded
on this disk. At every physical second color it vanishes exactly.
There are \(c_0N\) distinct such angular points in a fixed positive
real subinterval of the disk. A disk Blaschke estimate gives
exponential smallness on an open interior disk; finite buffered
propagation reaches any smaller complete disk. All constants are
uniform in \(a\), since the bounds and zero set are uniform.
Cauchy estimates give the derivative statement. The difference
and phase are even in \(u\), so ordinary spectral derivatives
through \(u=0\) also follow on a smaller disk by even holomorphic
descent. No equality off the physical grid was used. \(\square\)

## 3. Uniform fold-line data on the whole parameter domain

Write \(\mathcal H_N(X,Y)=H_N(t(X),t(Y))\) and
\(\Psi(X,Y)=\psi(t(X),t(Y))\). Use all centered angular
nodes satisfying
\[
                         |t(X_j)|<\rho_0 .
 \tag{9}
\]
For such a node set
\[
                         a(j)=\min(j,N-1-j).
 \tag{10}
\]
Thus its color is the original distinct color \(c_{a(j)}\).
In particular a reflected index is not inserted as a new high
Jacobi degree into \(\widehat G\). Its angular derivative has
the actual sign \(C'(1-X_a)=-C'(X_a)\).

Define the normalized target line data
\[
 T_{j,0}(Y)=e^{-N\Psi(X_j,Y)}F_{a(j)}(C(Y)),
 \tag{11}
\]
and, at every double row,
\[
 T_{j,1}(Y)=e^{-N\Psi(X_j,Y)}
  \{C'(X_j)\widehat G_{a(j)}(C(Y))
                         -N\Psi_X(X_j,Y)F_{a(j)}(C(Y))\}.
 \tag{12}
\]
At the odd center \(X_j=1/2\) define \(T_{j,1}=0\).
This is a convenient auxiliary angular completion: \(C'=0\) and
\(\Psi_X=0\) there. Only \(T_{j,0}\) is prescribed by the
original simple spectral node. In particular (12) does not define
an additional spectral normal there. Define the second line data
\(S_{k,0},S_{k,1}\) by interchanging the endpoints.

**Theorem 3.** On every fixed smaller connected second-parameter
domain, uniformly for all nodes (9),
\[
 T_{j,a}(Y)-\partial_X^a\mathcal H_N(X_j,Y)
                        =O(e^{-cN}),\qquad a=0,1.
 \tag{13}
\]
The symmetric assertion holds for \(S_{k,b}\). All fixed
parameter derivatives retain this bound after fixed buffers.

**Proof.** First restrict the other parameter to a small complete
disk. Lemma 1 gives the value estimate, because the canonical
kernel's physical row is exactly \(F_{a(j)}\). At a double
row it also compares the angular derivative of the baseline with
the canonical derivative \(C'(X_j)G_{a(j)}\). Lemma 2 replaces
that canonical normal by \(C'(X_j)\widehat G_{a(j)}\), with
an exponential error. Derivatives of the normalizing exponential
produce only fixed powers of \(N\). At the odd center the canonical
angular derivative and \(\Psi_X\) are zero, so Lemma 1 gives
the auxiliary derivative estimate as well. Reflection changes
only the sign of \(C'\); the phase and colors are even.

For fixed \(j\), regard each difference in (13) as a holomorphic
function of the other angle. On every buffered parameter compact
it is bounded by \(e^{o(N)}\), uniformly over all the rows (9).
For the target terms this follows from (7), the fixed compact
phase derivative, and \(|C'|\le4\pi\). For the baseline and
its first derivative it follows from (3) and a fixed first-variable
Cauchy buffer around the entire small real fold interval. Its
normalized derivative is the derivative of \(H_N\) itself;
the \(N\Psi_X\) term has already been included in (12).

Starting with the uniform open-disk estimate just proved, use a
finite chain of buffered disks in the connected second-parameter
domain. At each step the three-circles estimate combines an
exponential bound with a uniform \(e^{o(N)}\) outer bound,
leaving a positive exponential exponent. The same finite chains
work for every \(j\); their constants depend on the fixed domains,
not on the moving physical row. This proves (13). Buffered Cauchy
estimates give fixed derivatives. No canonical-kernel bound is
used outside the small complete bidisk. \(\square\)

At a double row, conversion of an angular derivative error to a
spectral first-normal error costs only a polynomial. Indeed
\[
 |C'(X_j)|=4\pi|\sin(2\pi X_j)|\ge c/N
 \tag{14}
\]
for the fold-near double nodes. The odd center is excluded from
this division. No evenness or spectral descent of the off-grid
baseline is inferred from (14).

## 4. Exact two-line fold repair

Choose centered mirror windows with midpoint boundaries
\[
 a_N=k_N/N\longrightarrow\tfrac12-\rho/(2\pi),\qquad
 b_N=1-a_N,\qquad 0<\rho<\rho_0,
 \tag{15}
\]
and similarly in \(Y\). Include every grid node strictly between
the boundaries. All these nodes satisfy (9) for large \(N\).
The chosen original real seed windows can be retained inside
these windows by making their initial choice smaller if necessary.

At a joint selected node the target functions have the exact
compatibility
\[
 \partial_Y^b T_{j,a}(Y_k)
                 =\partial_X^a S_{k,b}(X_j),
                         \qquad 0\le a,b\le1.
 \tag{16}
\]
For two double rows this is the original four angular jets of
\(e^{-N\Psi}K_N(C(X),C(Y))\), including both independent
spectral normals and their mixed normal. If one row is the odd
center, its angular derivative is zero. The transposed target
functions are even at that center because they are functions of
its spectral color and the even phase. Thus (16) also holds there.
This is only angular compatibility at a simple spectral node.

For clarity use the explicit one-sided cardinal pairs
\[
 L_j^\sigma(X)=e^{\sigma2\pi iN(X-X_j)}
                       \operatorname{sinc}^2(N(X-X_j)),
 \quad
 V_{j,0}^\sigma=[1-\sigma2\pi iN(X-X_j)]L_j^\sigma,
 \quad V_{j,1}^\sigma=(X-X_j)L_j^\sigma.
 \tag{17}
\]
They have the required unit value/derivative jets at their own
node and double zeros at all other centered nodes. Write
\(W_{k,b}^\tau\) for the second-coordinate pairs. Set
\[
 d_{j,a}=T_{j,a}-\partial_X^a\mathcal H_N(X_j,Y),\qquad
 e_{k,b}=S_{k,b}-\partial_Y^b\mathcal H_N(X,Y_k),
\]
\[
 c_{jk}^{ab}=\partial_Y^bd_{j,a}(Y_k)
                         =\partial_X^ae_{k,b}(X_j),
 \tag{18}
\]
and define
\[
 \mathcal K_N^{\sigma,\tau}=e^{N\Psi}\left[
 \mathcal H_N+\sum_{j,a}d_{j,a}V_{j,a}^\sigma
 +\sum_{k,b}e_{k,b}W_{k,b}^\tau
 -\sum_{j,k,a,b}c_{jk}^{ab}V_{j,a}^\sigma W_{k,b}^\tau
 \right].
 \tag{19}
\]
All sums are over the selected mirror windows and \(a,b\in\{0,1\}\).
The same subtraction as in the product gluing theorem cancels the
second correction against the mixed correction on a first row,
and conversely. Consequently (19) has exactly the targets
(11)--(12) on both line families.

In particular its unnormalized value is \(F_{a(j)}(C(Y))\);
its angular derivative is \(C'(X_j)\widehat G_{a(j)}(C(Y))\)
at double rows. At an odd center its value is the actual simple
row and its imposed angular derivative is zero. The latter is
not used as an independent spectral datum.

The errors in (18) are exponentially small by Theorem 3. The
cardinal pairs and fixed derivatives are polynomially bounded on
bounded parts of their designated half-planes. There are only
\(O(N^2)\) summands. Hence on the corresponding inner product
compacts,
\[
 e^{-N\Psi}\mathcal K_N^{\sigma,\tau}
       =\mathcal H_N+O(e^{-c_1N}),\qquad
 |\mathcal K_N^{\sigma,\tau}|
       \le\exp\{N\Re\Psi+o(N)\},
 \quad \sigma\Im X\ge0,\quad\tau\Im Y\ge0.
 \tag{20}
\]
Fixed sufficiently thin opposite collars and all fixed buffered
angular derivatives are allowed. Their only extra cardinal cost
is \(\exp(4\pi N[(-\sigma\Im X)_++(-\tau\Im Y)_+])\);
choose the collars after the positive error exponent. These
claims do not assert evenness of (19).

## 5. The closed mirror trace and its odd simple node

Here is the exact multiplicity, separate from the analytic estimates.
Let \(\mathcal A_N\) consist of the distinct double spectral rows
whose two angular lifts lie in (15). For an original spectral
spectator \(P(Z;\ldots)\), keep its value and derivative, all
crossing carriers and all shared variables. Define
\[
 \begin{split}
 \Phi^\sharp_{N,\mathrm{fold}}(w;\ldots)
 ={}&\eta\sum_{a\in\mathcal A_N}
 \{(4-c_a^2)[\widehat G_a(w)P(c_a)
                         +F_a(w)P_Z(c_a)]-c_aF_a(w)P(c_a)\}\\
 &+\mathbf1_{\{N\ {\rm odd}\}}F_{J_N}(w)P(-2).
 \end{split}
 \tag{21}
\]
The last term is a single value. There is no normal at the odd
simple node. The original fold trace has the same expression with
\(G_a\) instead of \(\widehat G_a\).

Put \(D_h(X)=(\pi N)^2\sec^2(\pi NX)\), fix the second
representative sign \(\tau\), and let
\[
 g_\sigma(X)=\sin(2\pi X)
       \mathcal K_N^{\sigma,\tau}(X,Y)P(C(X);\ldots).
 \tag{22}
\]
Take closed lower and upper window halves with the original
orientations: \(E_-\) goes down the left side, across the lower
side and up the right; \(E_+\) goes up the right side, across
the upper side and down the left. Then
\[
 \boxed{\quad
 \Phi^\sharp_{N,\mathrm{fold}}(w(Y);\ldots)
 =-\frac{\eta}{4\pi^2i}
 \left\{\int_{E_-}D_hg_-\,dX+\int_{E_+}D_hg_+\,dX
       +\int_{a_N}^{b_N}D_h(g_+-g_-)\,dX\right\}.
 \quad}
 \tag{23}
\]
The contours must remain in the domains where the representatives
are defined. All vertical half-sides and the real interface are
part of this identity.

**Proof.** Each centered pole of \(D_h\) has principal part
\((X-X_j)^{-2}\), so its residue against \(g\) is \(g'(X_j)\).
At a double spectral row the actual angular jets give
\[
 g'(X_j)=-\pi\{(4-c_a^2)
       [\widehat G_a(w)P(c_a)+F_a(w)P_Z(c_a)]
                             -c_aF_a(w)P(c_a)\}.
 \tag{24}
\]
Both reflected lifts give the same expression: the two factors
\(\sin(2\pi X_j)\) and \(C'(X_j)\) change signs together.
Multiplication of their residue sum by
\(-\eta/(2\pi)\), the closed coefficient in (23), gives
exactly the corresponding term of (21).

At the odd center \(X_j=1/2\),
\(\sin(2\pi X)=-2\pi(X-1/2)+O((X-1/2)^3)\).
Its residue is therefore \(-2\pi F_{J_N}(w)P(-2)\), regardless
of the finite angular derivative of the representative. Since
\(\eta=1\) at odd level, (23) gives exactly the final term of
(21). Equivalently, \(P_N(C(X))=4\cos^2(\pi NX)\), and
\(C\) has degree two at this angular lift of the simple
spectral node. The factor one-half in (23) is compulsory there.

For two different half-plane representatives the real-interface
term is the usual split of the closed residue contour. Their full
angular jets agree at all selected nodes, so its singularities
are removable. This proves (23) without a first-angle parity
assumption. \(\square\)

The difference between (21) and the original free-\(w\) fold
trace is \(P_N(w)\) times a holomorphic slit function, by the
exact full-jet property of \(\widehat G_a\). Thus equality
with the original follows after its required subsequent complete
second trace, including arbitrary original spectators and their
normal products. At two selected fold windows, the exact mixed
jets of (19) give the original double-window trace directly, with
the same mirror factor in each variable. A local parameter chart
is not itself a contour for every remaining second row: the full
trace is taken on the global finite expression (21), or on a
covering retaining those rows.

## 6. Scope and direct sources

This extends the matched data from fixed bulk windows to a fixed
neighborhood of the simultaneous complete fold, including every
nearby even last normal and the odd simple value. It does not
extend to the original positive-color endpoint \(t=\pm\pi\),
identify an arbitrary free polynomial with (19), assert spectral
descent of the repaired functions, or replace a whole open lens
by an uneven representative. All shared products retain their
actual mixed product rules. The common baseline cancels from
differences of the designated representatives, but the original
trace kernels, spectators, interfaces and exterior sides remain;
no parent-action or scalar noncancellation conclusion is inferred.

Complete direct source texts and used implications were read at:

* [Positive product gluing](research_positive_product_window_gluing.md),
  SHA256 ace4f667038c494e2690a77496ce32e8bc8538535356b78600e8ad8ced8183d5:
  common normalized Cauchy baseline, exact bulk line errors,
  designated cardinal pairs and mixed repair, and precise sharp-trace scope.
* [Endpoint-role comparison](research_physical_row_endpoint_role_overlap.md),
  SHA256 67478e66259712bc648c23241c3c3e93bc4342c54b2dbcea39be97ee7b83edec:
  approximate-zero dense-grid estimates and finite complex propagation.
* [All-row full-normal control](research_compact_positive_contour_residue_control.md),
  SHA256 cac1016d5f515510b95071a25c8d97345b334043492a6b430c4e924f87d82bb0:
  exact pole-free normal, every physical mixed jet, own-row slit and
  half-plane bounds, midpoint calibration, and original simple-node trace.
* [Full complete-disk kernel](research_bare_kernel_three_fifths_disk.md),
  SHA256 fe2479fb7436a061f6fd5dda9a59ab22f3c10a9e79d5105b1f95361053196d3f:
  actual full canonical kernel expansion and all fixed ordinary spectral
  derivatives on the three-fifths bidisk, including both folded parities.

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical computation, test or compilation was run.
Adopted notes and public manuscripts were unchanged.
