# The next exact attachment of the transformed three/four prefix

Research deduction, 7 November 2026. The completed transformed prefix
can be attached directly to either a three or a four. No additional
Fourier transform is required. The intervening Gram contraction is
an explicit finite triangular moment of the prefix. This also identifies
the moving reference and the factorial gauge of the next conditional
message. It does not supply the whole-source estimate at that moving
reference. No numerical evaluation is used.

## 1. Both next letters carry the old four-weight

Put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 P_j=(r;r)_j,\quad p_j(Y)=(rY;r)_j,\quad
 \kappa=q^{D^2/2},\qquad N\ge2.
 \tag{1}
\]
Use the entire polynomial proved in
[the complete transformed-prefix theorem](research_mixed_three_four_complete_transformed_prefix.md):
\[
 F_N(w,Y)=f_{34,N}(w,Y)
       =N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)].
 \tag{2}
\]
Its separate degrees in \(w,Y\) are at most \(D\). For
\(\beta\in\{0,1\}\), the next letter is \(3+\beta\). Define
\[
 \begin{split}
 F_{\beta,N}^{+}(w,Z)
  &=N\operatorname{CT}_Y[
       F_N(w,Y)d_N(Y)(1+Y^{-N})C_{\beta,N}(Y,Z)]\\
  &=\sum_{a=0}^{D}
       \frac{F_N(w,r^a)}{P_a}C_{\beta,N}(r^a,Z).
 \end{split}
 \tag{3}
\]
This is the exact transfer \(\mathcal T_{1\beta}\) of the
[conditional/Fourier bridge](research_mixed_conditional_fourier_message_bridge.md),
not a proposed continuation. Its output and ordinary-color degrees
are at most \(D\). The weight in (3) is present for **both**
\(343\) and \(344\): it is determined by the old last letter,
which is four, rather than by \(\beta\).

For clarity, set
\[
 G_N(Y,Z)=F_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z).
\]
Its \(Y\)-band is contained in \([-D,2D]\). Therefore
\[
 F_{\beta,N}^{+}
       =N[Y^0]G_N+N[Y^N]G_N.                         \tag{4}
\]
These are the two complete sectors, including the original finite
forcing of \(d_N\). Root averaging applies to \(G_N\):
\(N^{-1}\sum_aG_N(r^a,Z)=[Y^0]G_N+[Y^N]G_N\).
It does not apply to the already multiplied expression
\((1+Y^{-N})G_N\) without an additional alias calculation.
In particular setting \(1+Y^{-N}=2\) at the roots and then using
the same root quadrature would count (3) twice.

All circles for the two constant terms in
\[
 F_{\beta,N}^{+}
 =N^2\operatorname{CT}_{X,Y}
  [U_{0,N}(w,X)C_{1,N}(X,Y)
     d_N(Y)(1+Y^{-N})C_{\beta,N}(Y,Z)]                 \tag{5}
\]
may have arbitrary positive radii. These are finite Laurent
polynomials, so sequential or simultaneous constant-term extraction
is exact. This statement alone does not pay any contour sector.

## 2. The Gram contraction is one explicit triangular moment

Define
\[
 \mathcal M_{j,N}(w)=
   \sum_{a=0}^{D-j}
       \frac{r^{-aj}P_{a+j}}{P_a^2}\,F_N(w,r^a),
                 \qquad 0\le j\le D.                 \tag{6}
\]

**Proposition 1.** The whole next source is
\[
 \boxed{\displaystyle
 F_{\beta,N}^{+}(w,Z)
       =\sum_{j=0}^{D}
           \frac{\mathcal M_{j,N}(w)p_j(Z)}
                         {P_j^{2+\beta}}.}
 \tag{7}
\]
Let \(b_N(w)=Sv(w)\) be the original ordinary boundary column, and
let the actual rows before and after the final Gram contraction be
\[
 k_{34,N}=b_N(w)^TB_3\Gamma B_4,\qquad
 d_{34,N}=k_{34,N}\Gamma .
 \tag{8}
\]
Then, with no extra matrix or scalar,
\[
 \begin{split}
 (k_{34,N})_a&=\kappa^3N F_N(w,r^a),\\
 (d_{34,N})_j&=\kappa^3N
                       \mathcal M_{j,N}(w)/P_j^2,\\
 F_{\beta,N}^{+}(w,Z)&=
       \frac1{\kappa^3N}
          \sum_{j=0}^{D}(d_{34,N})_j
                              \frac{p_j(Z)}{P_j^\beta}.
 \end{split}                                                   \tag{9}
\]

*Proof.* The literal conditional kernel is
\[
 C_{\beta,N}(Y,Z)
       =\sum_{j=0}^{D}
                   \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}}.
 \tag{10}
\]
At \(Y=r^a\), its first numerator equals \(P_{a+j}/P_a\)
when \(a+j<N\), and is exactly zero otherwise. Inserting (10)
into the second line of (3) gives (6)--(7).
The first line of (9) is the exact row identity in the transformed
prefix and message-bridge theorems. The original Gram entry is
\[
 \Gamma_{aj}=
 \begin{cases}
  r^{-aj}P_{a+j}/(P_a^2P_j^2),&a+j<N,\\
  0,&a+j\ge N.
 \end{cases}
 \tag{11}
\]
Multiplying the first line of (9) by (11) gives its second line,
and (7) gives the third. \(\square\)

Thus (7) combines the two sectors in (4) exactly into the actual
post-Gram row. It does not discard their difference or approximate
\(d_N\) by a homogeneous reciprocal factorial. Formula (9) is
the original first-cap transform with its ordinary column replaced
by the actual row \(d_{34,N}/(\kappa^3N)\). Existing first-cap
bounds for \(b_N(w)\) do not automatically apply to this new row.

The two physical support inequalities after a physical output
\(Z=r^b\) are
\[
                       a+j<N,\qquad j+b<N.             \tag{12}
\]
There is no additional condition \(a+b<N\). For nonphysical
\(Z\), the second inequality must not be imposed: all terms in
(7) remain, including the high rows revived by \(p_j(Z)\).
Every denominator in (6)--(11) has index less than \(N\) and is
nonzero. Both level parities and both true endpoint indices are
therefore included.

## 3. Original outgoing observations and all their scalars

Let
\[
 k_{\beta,N}^{+}
       =b_N(w)^TB_3\Gamma B_4\Gamma B_{3+\beta}.
\]
The bridge identity, or multiplication of (9) by the original
\(B_{3+\beta}\), gives
\[
 (k_{\beta,N}^{+})_b
   =\kappa^{4+\beta}N^{1+\beta}
          P_b^{1-\beta}F_{\beta,N}^{+}(w,r^b).
 \tag{13}
\]
In particular the actual ordinary two-boundary source is
\[
 \begin{split}
 v(w)^TA_3A_4A_{3+\beta}v(w_R)
   =\kappa^{4+\beta}N^{1+\beta}
      \sum_{b=0}^{D}
       F_{\beta,N}^{+}(w,r^b)
                   \frac{H_N(w_R,r^{-b})}{P_b^\beta}.
 \end{split}
 \tag{14}
\]
All fixed ordinary derivatives differentiate precisely these
polynomials. There is no replacement of a Hermite normal by a raw
derivative in a complex retained-leg coordinate.

Equivalently, with the actual half-band Fourier transform
\(\mathcal E_\beta\) of the message bridge,
\[
 \mathcal E_\beta F_{\beta,N}^{+}
    =\frac{v(w)^TA_3A_4A_{3+\beta}h}
                  {\kappa^{4+\beta}N^{1+\beta}}.
 \tag{15}
\]
An additional attachment in the retained row chart multiplies
\(k_{\beta,N}^{+}\) by \(\Gamma B_{\rm next}\).
If one instead keeps the post-Gram row
\(d_{\beta,N}^{+}=k_{\beta,N}^{+}\Gamma\), the next operation
is \(d_{\beta,N}^{+}B_{\rm next}\Gamma\).
These are the same original products with different cut locations.
Neither prescription inserts a second Gram at the same interface.

## 4. The exact phase gauge at this cut

Use the original branches from
[the actual prefix phase theorem](research_mixed_actual_prefix_finite_step_phase_transport.md):
\[
 \begin{split}
 V_\beta(s,z)&=g(s+z)-\beta\{g(s)+g(z)\},\\
 G(y,s)&=g(y+s)-2g(y)-2g(s)+2\pi iys,\\
 Q_\beta(s;y,z)&=g(y+s)+g(z+s)
       -(2+\beta)g(s)-g(y)-g(z)+2\pi iys.
 \end{split}
 \tag{16}
\]
On every common original regular chart there is the absolute identity
\[
       G(y,s)+V_\beta(s,z)
        =Q_\beta(s;y,z)-g(y)+(1-\beta)g(z).
 \tag{17}
\]
It follows by cancellation of the displayed primitives, so it has
no undetermined additive constant or logarithmic lift.

Let \(\mathcal P_{34}(w,y)\) be the conditional action of the
completed prefix. Since this prefix ends in four, it is also its
pre-Gram row action. Its post-Gram geometric action is
\[
 \mathcal H_{34}(w,s)
      =\operatorname{stat}_{y}
            [\mathcal P_{34}(w,y)+G(y,s)].
 \tag{18}
\]
This is the actual cut action of (8), not the ordinary endpoint
action removed when proving the prefix.
At another actual reference, the same notation denotes the local
reduction of the original primitive action with \(y\) fixed.
Its internal Hessian is an invertible principal block of the
original accretive Hessian, so this geometric germ exists by the
implicit function theorem. This does not continue the proved
finite-source asymptotic to that other reference.
On the original critical branch, (17) identifies the next
conditional geometric action as
\[
 \mathcal P_\beta^{+}(w,z)
   =\operatorname{stat}_{y,s}
        [\mathcal P_{34}(w,y)-g(y)+Q_\beta(s;y,z)].
 \tag{19}
\]
The corresponding pre-Gram row action is
\(\mathcal P_\beta^{+}+(1-\beta)g(z)\).
Eliminating \(y\) first in (19) gives exactly (18) followed by
the original \(V_\beta\) attachment. Thus computing a full
Fourier message and then inverting it is unnecessary for the
finite operation (3).

Equation (19) labels the unwrapped geometric component. The second
sector in (4), where a reciprocal-factorial approximation is
legitimate, has action
\[
 \mathcal P_{34}(w,y)-g(y)+Q_\beta(s;y,z)+2\pi iy .
 \tag{20}
\]
The exact \(d_N\) and both sectors are still required in (3).
In particular (19) alone is not a whole-source asymptotic.

There is also a useful normalization check. A conditional row of
type \(\beta\) has regular power \(N^{-1-\beta/2}\);
the actual \(d_N\) packet contributes \(N^{-1/2}\).
If a local stationary contribution uses the proved
\(N^{-3/2}\) prefix packet at an eligible input and has two
nondegenerate integrated coordinates \(y,s\), then its power in
the normalized conditional output is
\[
 N^{-3/2}N^{-1/2}N^{-1-\beta/2}
        \underbrace{N^2}_{\text{outer CT and index density}}
        \underbrace{N^{-1}}_{\text{two-dimensional Gaussian}}
              =N^{-2-\beta/2}.                        \tag{21}
\]
The factors in (13), including
\(P_b^{1-\beta}\) with regular power \(N^{(1-\beta)/2}\),
restore the same \(N^{-1/2}\) pre-Gram row order for either letter.
Thus \(N^{-3/2}\) is not an invariant normalization of the
conditional polynomial under this update. Equation (21) is
power bookkeeping for an eligible local contribution, not an
assertion that its hypotheses or whole-source dominance are
already proved for \(343\) or \(344\).

## 5. The next actual reference is an ordinary four-leg image

The completed prefix packet is centered at the right private leg
\(z_*\) of the complete ordinary pair. In a word with a following
vertex, that coordinate becomes \(t_2\), an ordinary type-four
leg. The Gram output coordinate in (18) is \(s_3\).
These are different coordinate roles.

Use exactly the clipped domains \(A_3,A_4,O_3,O_4\) of
[actual last-row reference domains](research_mixed_actual_last_row_reference_domains.md).
For a three-vertex word \(34(3+\beta)\), vertex two has own type
four and the original two-leg external parameters
\[
             a=t_1\in A_3,\qquad c=s_3\in A_{3+\beta}.
 \tag{22}
\]
Write \(B_1(a,c)=(s_2(a,c),t_2(a,c))\) for that original
zero-lift two-leg map. Its two outputs lie in \(O_4\), by the
whole-bidisk ordinary image theorem. The required old-prefix
input is the correlated value
\[
             y=t_2(a,c),\qquad
             (a,c)\in A_3\times A_{3+\beta}.            \tag{23}
\]
The complete endpoint equations further restrict this sufficient
product to the actual realized inputs. In particular the outgoing
type affects the reference family in (23), while the weight in
(3) remains the old type-four weight.

If vertex three is itself ordinary in a longer open word, its
left leg instead belongs to \(O_{3+\beta}\). The corresponding
sufficient family for the first two vertices is
\[
             y=t_2(a,c),\qquad
             (a,c)\in A_3\times O_{3+\beta}.            \tag{24}
\]
These two families are independent of the remaining word length,
but no assertion is made that every point of either product is
realized. They retain the output correlation of the original
map. Replacing \(t_2(a,c)\) by an arbitrary independent point in
\(O_4\) gives a larger sufficient domain, not an exact description.

The arbitrary-letter phase theorem supplies the original stationary
branch and its nondegeneracy at these actual references. It does
not enlarge the complete finite-prefix packet from its present
neighborhood of \((-2,z_*)\) to (23) or (24). Even a packet at
all such centers would still require estimates for the remainder
of the full moment (6), or equivalently the complete two-sector
cycle (3), relative to the new action (19). The exact reduction
here removes an unnecessary change to Fourier coordinates and
fixes the next finite source; it does not remove that analytic
obligation or establish another short-filling knot family.
