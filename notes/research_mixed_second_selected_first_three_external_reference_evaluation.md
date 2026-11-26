# Original-reference enclosures for a first block of type three

Research implementation specification, 6 November 2026. The separate
[provider](../experiments/mixed_second_selected_first_three_external_reference.py)
encloses the original canonical prefix for flags \((0,1,\beta)\),
\(\beta=0,1\), over one prescribed external-coordinate rectangle.
It makes no numerical call on import, writes no file and performs no
parameter traversal. No numerical result is supplied by this note.

## 1. Interface, fixed seeds and scope

The API is `initialize()` and
`evaluate(cbox, cmid, beta, seed_centers=None)`, compatible with the
preserved [first-type-four provider](../experiments/mixed_second_selected_external_reference.py).
The new module has its own explicit first-type-three gradient. It
neither imports that old provider nor calls its gradient, initialization,
reference or canonical-certificate routines. The old source is pinned
only to identify the reviewed arithmetic mechanics that were copied.
No first-type-four canonical record is read.

Initialization verifies the explicit proof/source/specification hashes
and returns these bindings, its own hash, first flag zero and the fixed
exact proposal seeds. The order is \(q=(e,\xi,a,u,z,v,b)\):
\[
 \begin{split}
 (e_0,\xi_0,a_0,u_0,z_0)
 &=(.407+.009i,\ .230+.063i,\ .3345-.0255i,
                       \ .30-.052i,\ .30-.052i),\\
 (v_0,b_0)&=
 \begin{cases}
 (.35-.01i,.35-.01i),&\beta=0,\\
 (.30-.052i,.30-.052i),&\beta=1.
 \end{cases}
 \end{split}
 \tag{1}
\]
All decimals denote exact rationals. These are fixed starting guesses,
not certified roots. Optional supplied seeds must equal the prescribed
seed exactly; there is no alternate-seed or child-seed policy.
Initialization returns copies so changing returned metadata does not
change the internal prescribed seeds.

The input `cbox` is an exact rectangle in
\(Q=[.23,.45]+i[-.12,.12]\). Its prescribed exact expansion
point `cmid` must lie in it; it need not be the Cartesian midpoint.
The certificate concerns every actual canonical reference with
\(c\in\texttt{cbox}\cap(K_3\cup K_4)\), using the external
domains in the [first-type-three theory](research_mixed_second_selected_first_three_extension.md).
The conclusion does not assert that this intersection is nonempty or
realized by a finite suffix. Full-box overhang outside \(Q\) is
inconclusive. Strict rational disk-distance, height or oblique
separation may exclude a typed alternative; only exclusion of both
alternatives excludes the cell.

Existence and uniqueness at every actual typed parameter precede any
proposal, by the original canonical-prefix theorem for first flag zero.
The seed does not need an independent existence certificate. A certified
original residual of the eventual rational proposal supplies localization.

## 2. The original gradient and analytic derivatives

Let \(j(w)=\Log(2\sin\pi w)\) in the original regular strip.
The module explicitly implements
\[
 \begin{split}
 f_e={}&-j(e-\xi)+j(e+a)+i\pi(\xi-a),\\
 f_\xi={}&2\Log\cos\pi\xi+\Log\sin\pi(e-\xi)
                     -3\Log\sin\pi\xi+i\pi e,\\
 f_a={}&j(e+a)+j(a+u)-2j(a)+i\pi(u-e),\\
 f_u={}&j(u+z)+j(a+u)-3j(u)+i\pi(a-z+u-1/2),\\
 f_z={}&j(u+z)+j(z+v)-3j(z)+i\pi(v-u+z-1/2),\\
 f_v={}&j(v+b)+j(z+v)-(2+\beta)j(v)
                         +i\pi\{z-b+\beta(v-1/2)\},\\
 f_b={}&j(v+b)+j(b+c)-(2+\beta)j(b)
                         +i\pi\{c-v+\beta(b-1/2)\}.
 \end{split}
 \tag{2}
\]
Both floating proposals and outward residuals use this same local
function, with their respective arithmetic operations supplied as
arguments. It is the original unscaled gradient, not an exponentiated
system or a first-type-four residual with omitted corrections.

Write \(k(w)=\pi\cot\pi w\). The analytic symmetric Jacobian
has the changed diagonal entries
\[
 H_{ee}=-k(e-\xi)+k(e+a),\qquad
 H_{aa}=k(e+a)+k(a+u)-2k(a).
 \tag{3}
\]
Every other entry is the original derivative of (2), as recorded in
the first-type-three theory. The only external forcing is
\[
                     f_c=e_b\{k(b+c)+i\pi\}.
 \tag{4}
\]
The affine argument inventory retains the old fifteen forms, including
the now-unused private own argument \(e\), so the same full-domain
guards and upper operation counts remain valid. The actual Taylor
row coefficients remove \(-j(e)\) and change \(-3j(a)\) to
\(-2j(a)\). The full auxiliary row remains
\(2j(1/2-\xi)-3j(\xi)+j(e-\xi)+i\pi e\), whose logarithmic
constants cancel exactly. Unused argument checks add no remainder term.

## 3. One bounded proposal and the full-box certificate

Outward precision is fixed at 256 bits. There is one proposal from (1),
with at most twenty undamped Newton steps at 50 decimal digits and
stopping tolerance \(10^{-42}\). Round the final proposed coordinates
to forty decimal places to obtain exact rational complex \(q_0\).
At that rounded point form one floating inverse of (3) and the other
analytic entries, and the predictor \(-H^{-1}f_c\); round to forty
places to obtain exact rational \(P,T\). Floating convergence,
invertibility and residual size have no certification role.

For \(\delta=c-c_0\), put \(q_{\rm aff}=q_0+T\delta\).
Its entire image must remain in the common convex product
\[
 E\times U\times Q^5,\qquad
 E=[.33,.47]+i[-.09,.08],\quad
 U=[.21,.25]+i[.01,.10].
 \tag{5}
\]
All original sine/logarithm arguments are checked on the full affine
image and the rational expansion point. Their real parts must lie
strictly between zero and one; Cartesian sine separation is checked
before division. This preserves the original branches, including the
auxiliary sine and cosine expressions.

With \(r_0=f(q_0;c_0)\), \(L_0=H_0T+f_{c,0}\), the same
termwise whole-affine-image Taylor bound as in the preserved provider
gives
\[
 \begin{split}
 \rho_i&=\sum_j |a_{ij}|
   \sup|J'''(L_{ij}(q_{\rm aff},c))|\,|L_{ij}(T,1)|^2,\\
 \varepsilon&=
  \frac{\overline{\|r_0\|_2}
       +\overline{\|L_0\|_2}\,d
       +\overline{\|\rho\|_2}\,d^2/2}{6\pi_-/49},
       \qquad d\ge\sup|\delta|.
 \end{split}
 \tag{6}
\]
Here \(J'''=-\pi^2\csc^2\pi w\), and all norms, products
and square roots have outward bounds. The unchanged coercivity
\(\mu=6\pi/49\), proved for both first types, implies
\(\|q_*(c)-q_{\rm aff}(c)\|_2\le\varepsilon\) at every
actual typed point. Every connecting segment is covered by the full
affine image. No clipped coordinate enters this Taylor estimate.

Only afterwards expand the raw affine real and imaginary intervals
by \(\varepsilon\) and intersect with necessary actual bounds.
The three changed endpoint rectangles are exactly
\[
 \begin{split}
 e&\in[.376,.438]+i[-.019,.037],\\
 \xi&\in[.218,.242]+i[.049,.077],\\
 a&\in[.278,.391]+i[-.072,.021].
 \end{split}
 \tag{7}
\]
The attached coordinate \(a\) is not assigned the ordinary-type-three
height floor \(-.065\). The ranges of \(u,z,v,b\) and the
typed external hull are unchanged from the original reference theorem.
Every intersection is necessary for actual canonical points. An empty
one excludes actual references, without prompting another proposal.

## 4. Certified response and compatible output

On the resulting pointwise canonical enclosures, evaluate the changed
original Jacobian and (4). For the rational preconditioner \(P\),
put \(E_0=I-PH\) and require an outward row-sum bound
\(\eta\ge\|E_0\|_\infty\) to be less than one. Then
\[
 \|H^{-1}-P\|_\infty\le
       \frac{\eta\|P\|_\infty}{1-\eta},\qquad
 \|q_*'-T\|_\infty\le
       \frac{\|P(HT+f_c)\|_\infty}{1-\eta}.
 \tag{8}
\]
These are the same Neumann inequalities as before, now applied to the
new original system. No clipping operation is differentiated. The
provider does not itself apply the optional componentwise refinement.

The return includes first flag zero at top level and in the witness;
eight live coordinates \(e,\xi,a,u,z,v,b,c\); seven negative-sign
shapes \(e^{-2\pi iw}\) for \(e,a,u,z,v,b,c\); seven derivatives
with respect to the external complex \(c\); and \(H\), an inverse
enclosure, JSON-safe details, the witness alias and counts. It saves
the exact seeds, \(q_0,T,P\), full raw affine and localized boxes,
necessary intersections, residual and Taylor norm factors, all response
matrices, derivative enclosures, and shape boxes.

Status `enclosed` requires all localization, regularity and Neumann
checks. An expected arithmetic failure is `inconclusive`; a strict
necessary geometric contradiction is `excluded`. Unexpected code or
API errors have status `error` and a saved `unexpected_error` field;
the caller must stop and archive them. Finite-source, scalar-budget,
alternate-seed, alternate-midpoint and retry counts remain zero.

The fixed per-call caps remain one proposal, twenty floating gradients
and Newton steps, one floating preconditioner inverse, one original
outward residual, two interval Jacobians, thirty cotangent enclosures,
fifteen third-derivative enclosures, one Neumann verification and seven
negative-shape exponentials. No repeated proposal or precision increase
is allowed. A caller must verify all returned bindings before and
after its separately reviewed traversal. This module supplies neither
a central sign nor a finite-source or whole-domain comparison.
