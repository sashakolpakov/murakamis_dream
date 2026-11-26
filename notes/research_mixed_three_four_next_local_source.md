# The local finite-source contribution of the next three or four

Research deduction, 7 November 2026. The complete transformed
three/four prefix can be integrated through the next original
geometric critical point. On both the ordinary and terminal
reference families, this local integral has a nonzero asymptotic
expansion. Its integrand retains the entire prefix polynomial,
the actual Fourier weight and every row of the next conditional
kernel. Thus the result includes the already controlled
noncentral contributions inside these factors.

Only a local part of the next unwrapped coefficient is evaluated.
The remaining coefficient contour and the second Fourier sector
are not removed. No new ordinary closing or knot theorem follows.
No numerical evaluation is used.

## 1. The next exact source and its two sectors

Put
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(X)=(rX;r)_j,\quad D=N-1,\quad
 \kappa_N=e^{\pi iD^2/(2N)} .
 \tag{1}
\]
Let \(F_N(w,Y)=f_{34,N}(w,Y)\) be precisely the polynomial of
[the complete following-prefix theorem](research_mixed_three_four_following_complete_prefix.md).
For \(\beta\in\{0,1\}\), retain
\[
 \begin{split}
 C_{\beta,N}(Y,Z)
   &=\sum_{j=0}^{D}
       \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},\\
 \mathcal F_{\beta,N}(w,Z)
   &=N\operatorname{CT}_Y
       [F_N(w,Y)d_N(Y)(1+Y^{-N})C_{\beta,N}(Y,Z)] .
 \end{split}                                                   \tag{2}
\]
The old last vertex is four, so the weight in (2) is present for
both next letters. The [exact attachment identity](research_mixed_three_four_next_conditional_attachment.md),
Sections 1--3, gives
\[
 \begin{split}
 \mathcal F_{\beta,N}&=N[Y^0]G_N+N[Y^N]G_N,\qquad
 G_N=F_Nd_NC_{\beta,N},\\
 \mathcal F_{\beta,N}(w,Z)
   &=\sum_{a=0}^{D}\frac{F_N(w,r^a)}{P_a}
                              C_{\beta,N}(r^a,Z),\\
 (k_{\beta,N})_b
   &=\kappa_N^{4+\beta}N^{1+\beta}
                         P_b^{1-\beta}\mathcal F_{\beta,N}(w,r^b).
 \end{split}                                                   \tag{3}
\]
Here \(k_{\beta,N}=b_N(w)^TB_3\Gamma B_4\Gamma B_{3+\beta}\)
is the original row before its final Gram contraction.
In particular no new Gram matrix belongs between the factors of
\(G_N\). Its \(Y\)-band is contained in \([-D,2D]\).

For any fixed height \(h\), the unwrapped coefficient has the
increasing-coordinate representation
\[
       N[Y^0]G_N(Y,Z)
         =N\int_{ih}^{1+ih}G_N(e^{-2\pi iy},Z)\,dy .
 \tag{4}
\]
This is the Fourier average of a finite one-periodic Laurent
polynomial. Equation (4) fixes the orientation and its scalar.
The second sector has the additional factor \(e^{2\pi iNy}\).
Nothing below estimates that sector.

## 2. Which next references are eligible

Use the original \(P_3,P_4,O_3,O_4,A_3,A_4\) from
[actual last-row reference domains](research_mixed_actual_last_row_reference_domains.md).
Write the last three retained coordinates as
\[
                       y=t_2,\qquad s=s_3,\qquad z=t_3 .
 \tag{5}
\]
The inverse leg connecting the old prefix to the next vertex is
\(s\), not \(z\). Denote the old following curve by \(q_{34}\).

**Ordinary next vertex.** Fix an external leg
\(b\in P_{3+\nu}\), \(\nu\in\{0,1\}\), and take the unique
cap-initialized half-chain of the word \(34(3+\beta)\) with its
final incidence \(G(z,b)\). Existence, the original logarithmic
lift and holomorphy near each closed input disk follow from
[cap-phase entrance, Lemma 1](research_mixed_alternating_cap_phase_entrance.md)
and the [arbitrary-prefix curve theorem](research_mixed_arbitrary_prefix_pregram_curve.md).
The actual equations give
\[
       y=q_{34}(s),\qquad
       (s,z)=F_{3+\beta}(y,b),\qquad
       y\in O_4,\quad s,z\in O_{3+\beta}.                 \tag{6}
\]
To see the first identity, freeze \(s\). The five earlier
coordinates solve exactly the original \(34\) half-chain
equations with external parameter \(s\). Uniqueness in their
common convex product identifies that solution with the old
following curve. The second identity is the original two-leg
block equation, and the strict full-map image bounds give the
last inclusions.

Consequently \(y\in q_{34}(O_{3+\beta})\), where the whole
prefix expansion is proved. The
[reduced-disk conditional theorem](research_mixed_reduced_disk_conditional_packets.md)
applies to the next kernel with external inputs
\((y,b)\in P_4\times P_{3+\nu}\) and orientation \((s;y,z)\).
It gives the complete \(C_{\beta,N}\) expansion on an ambient
neighborhood of \((y,z)\). The output \(z\) is the correlated
value in (6); no independent box of output coordinates is used.
This canonical family includes every actual ordinary third
vertex in a longer open word beginning \(34(3+\beta)\), because
its following leg \(b=s_4\) belongs to its attached or ordinary
typed domain, hence to the corresponding reduced disk.

**Terminal next vertex.** Take the actual complete-ended word
\(34(3+\beta)\). Its last endpoint map has
\[
       (z,s,u_R)=\mathcal E_{3+\beta}(y),\qquad
       s\in A_{3+\beta},\quad y=q_{34}(s)\in O_4.         \tag{7}
\]
Here \(z\) is private. In particular it is not required to lie
in an ordinary reduced disk. The terminal source graph is
\(\mathcal K_{\beta,1}\), since the preceding input \(y\) has
type four. [Terminal conditional packets, Theorem 1](research_mixed_terminal_conditional_packet.md)
supplies the whole \(C_{\beta,N}\) expansion on an ambient
neighborhood of that graph. The complete prefix applies through
\(q_{34}(A_{3+\beta})\). Existence and uniqueness of (7), with
the other coordinates, are those of
[ordinary open-word localization](research_mixed_open_word_critical_localization.md).

There are two terminal base points, one for each \(\beta\).
Their ordinary-color continuations are provided by the
[marked boundary germ](research_mixed_geometric_boundary_germ.md).
The assertions below hold for independent \(w,z\) on a small
neighborhood of each base. They therefore also hold after
substitution of this actual color-dependent terminal map.
An arbitrary point of the whole endpoint graph is not asserted
to satisfy the matching equation \(y=q_{34}(s)\).

All the ordinary base families in (6) are compact, and all
source neighborhoods just invoked are ambient complex
neighborhoods. The strict image margins and compactness permit
uniform small neighborhoods and local integration lengths
over the four ordinary type choices and the two terminal bases.
No unspecified continuation from the old isolated-pair private
coordinate is used.

## 3. The action and its nondegenerate reduction

Retain the original primitive and actions
\[
 \begin{split}
 g(v)&=J(v)+i\pi(v-v^2)/2,\\
 G(y,s)&=g(y+s)-2g(y)-2g(s)+2\pi iys,\\
 V_\beta(s,z)&=g(s+z)-\beta\{g(s)+g(z)\},\\
 Q_\beta(s;y,z)&=g(y+s)+g(z+s)
       -(2+\beta)g(s)-g(y)-g(z)+2\pi iys .
 \end{split}                                                   \tag{8}
\]
Here \(Q_\beta\) is the phase of a literal conditional row.
It includes the two outer factorial divisions, in contrast to
the phase of the marked source \(\mathcal L_{\beta,N}\).
Let \(\mathcal P_{34}(w,y)\) be the action of the whole prefix
expansion. Set
\[
 \begin{split}
 \Psi_\beta(y,s;w,z)
    &=\mathcal P_{34}(w,y)-g(y)+Q_\beta(s;y,z)\\
    &=\mathcal P_{34}(w,y)+G(y,s)+V_\beta(s,z)
                                      -(1-\beta)g(z).
 \end{split}                                                   \tag{9}
\]
The second equality is an identity of the original primitives,
with their constants. In particular the extra \(-g(y)\)
belongs to the actual old-four weight \(d_N\).

At either reference (6) or (7),
\[
 \partial_y\Psi_\beta
       =\mathcal P_{34,y}+G_y=0,\qquad
 \partial_s\Psi_\beta=G_s+V_{\beta,s}=0.                \tag{10}
\]
These are the original unwrapped equations. For nearby \(w,z\)
write their continued solution as
\((y^\#,s^\#)\), and put
\[
        \mathcal P_\beta^+(w,z)
          =\Psi_\beta(y^\#,s^\#;w,z).                   \tag{11}
\]

**Lemma 1.** At the complete-color bases the matrix
\[
       K=-\partial_{(y,s)}^2\Psi_\beta
                        \big|_{(y^\#,s^\#)}
 \tag{12}
\]
has Hermitian real part greater than \(\mu I\), where
\(\mu=6\pi/49\). It is the complex Schur complement of the
original internal Hessian. Both its \(s\)-entry and the
subsequent \(y\)-Schur complement are nonzero, with real
part greater than \(\mu\).

*Proof.* In the ordinary case start with the full original
half-chain action for \(34(3+\beta)\), and freeze \(z,b\).
In the terminal case start with the complete open action,
and freeze \(z,u_R\). In each case retain the six variables
\((u_L,s_1,t_1,s_2,y,s)\). The corresponding principal
negative Hessian has real part greater than \(\mu I\),
by cap-phase entrance or the
[open-word Hessian theorem](research_mixed_open_word_hessian.md).
The frozen final incidence or endpoint has no derivative
in these six variables. Eliminating the first four variables
gives precisely (9), by the prefix's absolute action identity.
The term depending only on \(z\) has no effect.

For a block matrix \(M\) with \(\Re M\succ\mu I\), its
Schur complement \(S=M_{22}-M_{21}M_{11}^{-1}M_{12}\)
satisfies the same lower bound: for
\(v=(-M_{11}^{-1}M_{12}\xi,\xi)\),
\(v^*Mv=\xi^*S\xi\), and \(\|v\|\ge\|\xi\|\).
Apply this first to the four eliminated coordinates and
then to \(s\). No Schur complement of entrywise real parts
is substituted. This proves the lemma. \(\square\)

Let \(s=s_\beta(y,z)\) be the conditional root and define
\[
 \begin{split}
 \psi_\beta(y,z)&=Q_\beta(s_\beta(y,z);y,z),\\
 \varphi_\beta(y;w,z)&=\mathcal P_{34}(w,y)-g(y)
                                                +\psi_\beta(y,z),\\
 k_s&=-Q_{\beta,ss}(s^\#;y^\#,z),\qquad
 k_y=-\varphi_{\beta,yy}(y^\#;w,z).
 \end{split}                                                   \tag{13}
\]
Then \(\det K=k_s k_y\). All these reductions and the
original Gaussian branches persist on smaller parameter
neighborhoods. In the ordinary family the action calibration is
\[
 \mathcal P_\beta^+(-2,z(b))
   =H_{34(3+\beta)}(b)-G(z(b),b)-(1-\beta)g(z(b)).
 \tag{14}
\]
Thus the conditional action is the original pre-Gram action
minus \((1-\beta)g(z)\). At a terminal base, adding that
same term and the original right endpoint action reconstructs
the full open action before eliminating its remaining
private coordinate. No absolute action constant is reset.

## 4. An actual central integral with all inner rows retained

Fix one of the bases above, with incoming coordinate \(y_0\).
Choose a sufficiently small, fixed \(\varepsilon>0\).
Orient the segment
\(\gamma_{y_0}=[y_0-\varepsilon,y_0+\varepsilon]\)
in increasing real coordinate, and define the exact finite integral
\[
 \mathcal J_{\beta,N}^{y_0}(w,z)
    =N\int_{\gamma_{y_0}}
       F_N(w,e^{-2\pi iy})\,d_N(e^{-2\pi iy})\,
       C_{\beta,N}(e^{-2\pi iy},e^{-2\pi iz})\,dy .
 \tag{15}
\]
It is a portion of (4) on a full period through \(y_0\).
All endpoints in (15) remain fixed while \(w,z\) vary.

Define the original nonzero factorial symbol
\[
 a_0(v)=\sqrt{2\sin\pi v}\,e^{-i\pi v/2},\qquad
 b_\beta(s;y,z)=
 \frac{a_0(s+y)a_0(s+z)}
      {a_0(s)^{2+\beta}a_0(y)a_0(z)} .
 \tag{16}
\]
The symbols use continuation from the positive real sine
chamber. Every argument in (16) stays in a compact regular
strip on the neighborhoods under consideration.

**Theorem 2.** The exact integral (15) satisfies
\[
 \begin{split}
 \mathcal J_{\beta,N}^{y_0}(w,z)
   &=N^{-2-\beta/2}\,
        \mathcal A_\beta^+(w,z)
        e^{N\mathcal P_\beta^+(w,z)}
                             (1+O_{\mathrm{hol}}(N^{-1})),\\
 \mathcal A_\beta^+
   &=\frac{2\pi\,
          \mathcal A_{34}(w,y^\#)\,
          a_0(y^\#)^{-1}\,
          b_\beta(s^\#;y^\#,z)}
           {\sqrt{k_s}\sqrt{k_y}}\ne0 .
 \end{split}                                                   \tag{17}
\]
The product of square roots is the determinant branch
obtained by the two successive original Gaussian integrations.
The assertion is uniform on fixed smaller neighborhoods of
the compact base families, for both level parities. Every fixed
mixed derivative of the relative error is \(O(N^{-1})\).

*Proof.* The completed prefix supplies its expansion uniformly
on the entire short segment and a fixed surrounding
neighborhood:
\[
 F_N(w,e^{-2\pi iy})
   =N^{-3/2}\mathcal A_{34}(w,y)
                 e^{N\mathcal P_{34}(w,y)}(1+O_{\rm hol}(N^{-1})).
 \tag{18}
\]
Here \(y_0\in O_4\subset E_4\), where \(E_4\) is the full
rectangle of
[Fourier-weight continuation, Corollary 2](research_mixed_fourier_weight_continuation.md).
That theorem concerns the actual polynomial, including its
finite forcing, and gives
\[
       d_N(e^{-2\pi iy})
        =N^{-1/2}a_0(y)^{-1}e^{-Ng(y)}
                                      (1+O_{\rm hol}(N^{-1})).
 \tag{19}
\]
Its difference from the original reciprocal factorial is
exponentially small there.

In the ordinary or terminal case, use the respective
whole conditional theorem from Section 2. In the convention
of (8) and (16), both give exactly
\[
 C_{\beta,N}(e^{-2\pi iy},e^{-2\pi iz})
  =N^{-(1+\beta)/2}
     \frac{\sqrt{2\pi}\,b_\beta(s_\beta;y,z)}
          {\sqrt{-Q_{\beta,ss}(s_\beta;y,z)}}
       e^{N\psi_\beta(y,z)}(1+O_{\rm hol}(N^{-1})).
 \tag{20}
\]
This is the complete finite kernel, including its two
end rows and all rows revived by complex \(y,z\).
There is no division by a whole neighboring source or by
a value at a physical zero.

At the base, Lemma 1 gives strict horizontal concavity of
\(\varphi_\beta\) on a sufficiently small neighborhood of
the segment, with a nonzero critical point at \(y_0\).
Choose \(\varepsilon\) uniformly by compactness and then
shrink the parameter neighborhoods. The shifted critical
point stays within \(\varepsilon/4\) of \(y_0\).
The fixed segment in (15) can be deformed to a horizontal
segment through that point, together with its two short
endpoint connectors. The entire exact finite integrand
makes this an exact deformation. The endpoint connectors
stay in neighborhoods with a fixed strict loss from the
critical action. This follows first at the base from
strict concavity, and then by continuity on their compact
neighborhoods. Equations (18)--(20) give their exponential
bounds in the same absolute normalization.

The remaining one-dimensional Gaussian has factor
\(\sqrt{2\pi}/\sqrt{Nk_y}\), with the increasing
orientation in (15). The exact powers are
\[
 N\cdot N^{-3/2}\cdot N^{-1/2}\cdot
       N^{-(1+\beta)/2}\cdot N^{-1/2}
                         =N^{-2-\beta/2}.              \tag{21}
\]
Combining the two Gaussian coefficients gives (17).
Every factor in its numerator is nonzero; Lemma 1 supplies
both nonzero denominators. The usual local analytic
Gaussian expansion and the holomorphic errors in
(18)--(20) give the stated relative \(O(N^{-1})\).
Uniform Cauchy estimates on nested fixed neighborhoods
give its fixed mixed derivatives. The contours defining
the exact integrals remain those fixed at the base.
\(\square\)

The theorem controls a stronger local finite source than
simultaneously selecting short inner contours in every
factor: all earlier Fourier contributions already present
in \(F_N\), and all conditional-index currents already
present in \(C_{\beta,N}\), are retained in (15).
Only the new outer variable \(y\) is restricted.

There is also a nonzero leading term for each fixed incoming
ordinary normal. Let \(u_L(z)\) be the original left endpoint
auxiliary coordinate at \(w=-2\) on this branch. Stationarity
in (11), followed by the original first-cap derivative identity
in [the complete cap theorem, Section 2, equation (8)](research_mixed_complete_first_cap_packet.md),
gives
\[
 \partial_w\mathcal P_\beta^+(-2,z)
   =\partial_w\mathcal P_{34}(-2,y^\#)
   =-\frac{\tan(\pi u_L(z))}{4\pi}\ne0 .
 \tag{21a}
\]
At the base \(u_L\in\mathcal U\), so the displayed factor
does not vanish; it remains nonzero on a smaller neighborhood.
For every fixed integer \(j\ge0\), the signed ordinary derivative
therefore satisfies
\[
 \left.(-1)^j\partial_w^j
           \mathcal J_{\beta,N}^{y_0}(w,z)\right|_{w=-2}
 =N^{j-2-\beta/2}\mathcal A_\beta^+(-2,z)
   \left(\frac{\tan(\pi u_L(z))}{4\pi}\right)^j
   e^{N\mathcal P_\beta^+(-2,z)}
                          (1+O_j(N^{-1})).
 \tag{21b}
\]
To obtain (21b), differentiate (17) using its holomorphic
relative error. The term in which every derivative hits the
exponential through its first phase derivative has order
\(N^j\); every other term has a lower power. The fixed-base
integral differentiates the actual ordinary polynomial in
(15). This statement concerns incoming ordinary derivatives,
not a replacement of the outgoing observation by a raw
retained-coordinate derivative.

## 5. Restoring the original row and preserving the observation

At a physical outgoing node \(z=b/N\), the central
contribution to the row normalization in (3) is exactly
\[
       \kappa_N^{4+\beta}N^{1+\beta}
                   P_b^{1-\beta}\mathcal J_{\beta,N}^{y_0}(w,b/N).
 \tag{22}
\]
On a regular outgoing neighborhood one may use the original
factorial \(\widehat P_N(Nz)\) for this normalization.
Its expansion is
\(\widehat P_N(Nz)=N^{1/2}a_0(z)e^{Ng(z)}(1+O_{\rm hol}(N^{-1}))\).
Thus the corresponding locally normalized current is
\[
 \kappa_N^{4+\beta}N^{-1/2}
       a_0(z)^{1-\beta}\mathcal A_\beta^+(w,z)
       e^{N\{\mathcal P_\beta^+(w,z)+(1-\beta)g(z)\}}
                              (1+O_{\rm hol}(N^{-1})).
 \tag{23}
\]
This is a normalization of the local integral, not an
identification of a new off-grid interpolation of the
whole original row.

The exact ordinary observation remains
\[
 v(w)^TA_3A_4A_{3+\beta}v(w_R)
   =\kappa_N^{4+\beta}N^{1+\beta}
       \sum_{b=0}^{D}\mathcal F_{\beta,N}(w,r^b)
                        \frac{H_N(w_R,r^{-b})}{P_b^\beta}.
 \tag{24}
\]
Equation (17) does not replace \(\mathcal F_{\beta,N}\)
by its local part throughout this sum. Fixed ordinary
derivatives act on the original ordinary polynomials;
fixed outgoing derivatives in (17) are local holomorphic
derivatives. No raw retained-coordinate derivative is
substituted for an ordinary Hermite normal.

The unwrapped contribution outside (15), and the complete
\(N[Y^N]G_N\) coefficient, still require estimates against
the action in (11). In particular the second sector adds
\(2\pi iy\) to (9); it is not a relative error in (19).
The remaining ordinary observation in (24) also retains
its prescribed source and scalar. These are the distinct
obligations before any whole next-prefix or closing theorem.
