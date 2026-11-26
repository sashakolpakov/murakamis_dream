# The signed physical band and its moving vertical current

Private research deduction, 8 November 2026. Moving a half-grid
cut through the actual geometric point gives a nonzero Gaussian
transition for a partial physical sum minus its complete vertical
current. This follows from the original complete local source,
not from positivity of the physical residues or a replacement by
the coefficient-index Fourier packet.

Before the cut reaches the geometric neighborhood this combination
is exponentially constant. The theorem determines its change,
not its initial value. The paired left remainder therefore retains
the same unresolved additive term. No numerical evaluation or
modification of a frozen source is used.

## 1. The exact signed quantity

Use the ordinary-next reference family, old filter and notation of
[the paired-left physical reduction](research_mixed_next_paired_left_physical_reduction.md).
In particular the flags are \((0,1,\beta)\), both conditional
vertices after the first cap are ordinary, and
\[
 h=\Im y_*,\quad \alpha=\Re y_*,\quad H=1/100,\qquad
 .24<\alpha<.36,\quad -.102<h<-.001 .
 \tag{1}
\]
Keep the complete finite kernel
\[
 K_N(y)=
 \frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}{1-Y^N},
 \qquad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
 \tag{2}
\]
For a half-grid point \(c=(n+1/2)/N\) in \(P=[.22,.45]\), put
\[
 \begin{split}
 S_N(c)&=\sum_{b=0}^{n}
       \frac{F_N^{\rm mid}(w,r^b)}{P_b}C_{\beta,N}(r^b,Z),\\
 V_N(c)&=\int_{c+ih}^{c+iH}K_N(y)\,dy,\qquad
 Q_N(c)=S_N(c)-V_N(c),\\
 c_{0,N}&=\frac{\lceil .22N\rceil+1/2}{N}.
 \end{split}
 \tag{3}
\]
The old deleted nodes remain deleted. All other residues in this
partial physical band, and the entire vertical current, remain
literal. The notation \(Q_N(c)\) here denotes a signed scalar
quantity, not a conditional phase or the polynomial quotient of
another note.

For any two such half-grid points \(c<c'\), the original
counterclockwise rectangle gives exactly
\[
 \boxed{\quad
 Q_N(c')-Q_N(c)
 =\int_{[c,c']+ih}K_N(y)\,dy
       -\int_{[c,c']+iH}K_N(y)\,dy .
 \quad}
 \tag{4}
\]
Indeed its residues are precisely the terms with \(n<b\le n'\);
each residue is the corresponding summand divided by \(2\pi i\).
There is no further factor \(N\) in that sum. The right vertical
side points upward and the left side downward, so moving their
difference to the other side gives (4).

The optional full-prefix substitution in Section 4 of the
paired-left reduction is also valid here, uniformly for cuts in
\(P\). Its proof uses positive partial-band bounds for the low
nodes and the first-coordinate endpoint rectangle. No assertion
below requires that substitution.

## 2. Exponentially constant parts of the balance

Fix any \(\varepsilon>0\) small enough that
\([\alpha-\varepsilon,\alpha+\varepsilon]\subset P\) uniformly
over the actual compact families. For half-grid cuts
\[
 c_{0,N}\le c<c'\le\alpha-\varepsilon
 \quad\hbox{or}\quad
 \alpha+\varepsilon\le c<c'\le.45 ,
 \tag{5}
\]
the normalized fixed outside jets of (4) have an exponentially
small bound, uniform in the cuts.

To prove this, use the complete pointwise lower-source estimate,
equation (11) of
[the lower central theorem](research_mixed_next_complete_lower_plateau.md).
Its loss on the whole lower interval in (5) is at least
\[
             \min\{2\kappa\varepsilon^2,10^{-11}\}>0,
                 \qquad \kappa=1/2500000.
 \tag{6}
\]
Section 4 of that theorem bounds \(K_N-NF_Nd_NC_{\beta,N}\)
pointwise on the whole lower plateau, retaining the old filter
and its denominator. The upper integral in (4) is paid pointwise
by the complete selected-segment theorem and the old-filter
correction, with the identity
\(-K_N=NF_N^{\rm mid}d_NY^{-N}C_{\beta,N}/(1-Y^{-N})\).
Lengths are bounded and all additional factors are polynomial.
For example, after shrinking the original outside neighborhoods,
one may use a normalized loss
\[
        \eta_\varepsilon
           =\frac1{64}\min\{2\kappa\varepsilon^2,10^{-11}\}.
 \tag{7}
\]
Paths, heights and integer cuts are kept fixed at each base before
these jets are taken. The corresponding all-real-color upper
bound uses the original complete-color action and outgoing
allocation. No moving finite-source packet is needed on (5).

## 3. The transition on the Gaussian scale

The following asymptotic is at complete color \(w=-2\) and the
actual output \(z=z_*\). It is uniform over the compact ordinary
reference families and both level parities. It is not asserted
at independently varied complex outputs with these same
microscopic endpoints.

Let \(\mathcal P_\beta^+\), \(\mathcal A_\beta^+\ne0\), and
\[
 k_y=-\varphi_{\beta,yy}(y_*;-2,z_*),
       \qquad \Re k_y>6\pi/49,
 \tag{8}
\]
be exactly the action, coefficient and final Schur curvature
of [the local next-source theorem](research_mixed_three_four_next_local_source.md),
equations (13),(17). Its original Gaussian square root defines
\[
 \Phi_{k_y}(t)=
       \frac{\sqrt{k_y}}{\sqrt{2\pi}}
            \int_{-\infty}^{t}e^{-k_y v^2/2}\,dv
                  \qquad(t\in\mathbb R).
 \tag{9}
\]
The positive-real-part curvature makes the integral convergent.
On the same branch,
\(\Phi_{k_y}(0)=1/2\) and \(\Phi_{k_y}(+\infty)=1\).
No positivity of this complex Gaussian for general \(t\) is used.

For a bounded real parameter \(t\), choose the literal half-grid cut
\[
 c_N(t)=\frac{\lfloor N\alpha+t\sqrt N\rfloor+1/2}{N},
 \qquad t_N=\sqrt N\{c_N(t)-\alpha\}.
 \tag{10}
\]
Then \(|t_N-t|\le1/(2\sqrt N)\). For every fixed \(T<\infty\),
uniformly for \(|t|\le T\),
\[
 \boxed{\quad
 Q_N(c_N(t))-Q_N(c_{0,N})
 =N^{-2-\beta/2}\mathcal A_\beta^+
       e^{N\mathcal P_\beta^+}
          \{\Phi_{k_y}(t_N)+O_T(N^{-1/2})\}.
 \quad}
 \tag{11}
\]
The error in braces is additive; no division by
\(\Phi_{k_y}(t_N)\) is intended.

*Proof.* Apply (4). The whole upper interval is paid as in
Section 2. On the lower interval, Section 4 of the lower central
theorem permits replacement of \(K_N\) by the original
\(NF_Nd_NC_{\beta,N}\) with an exponentially smaller error,
uniformly on every subinterval. This is a pointwise source
comparison, not subtraction of two uncontrolled integrals.

Choose a fixed sufficiently short local segment
\([y_*-\varepsilon,y_*+\varepsilon]\) inside the actual ambient
neighborhood of the local next-source theorem. The lower part
from \(c_{0,N}+ih\) to \(y_*-\varepsilon\) is exponentially
smaller by (6). On the remaining segment that theorem gives the
complete product expansion
\[
 NF_Nd_NC_{\beta,N}
    =N^{-(3+\beta)/2}\mathcal B_\beta(y)
         e^{N\varphi_\beta(y;-2,z_*)}
                      (1+O_{\rm hol}(N^{-1})),
 \tag{12}
\]
where all finite rows and the actual forced Fourier polynomial
are included. Its symbol at the critical point satisfies
\[
       \mathcal A_\beta^+
          =\mathcal B_\beta(y_*)\sqrt{2\pi}/\sqrt{k_y}.
 \tag{13}
\]
These powers and symbols are the products in equations
(18)--(21) of that source; no scalar is reset.

Write \(y=y_*+v/\sqrt N\). Uniform analyticity on the fixed
local neighborhood and the original strict real curvature give
\[
 N(\varphi_\beta(y)-\mathcal P_\beta^+)
       =-\tfrac12 k_yv^2+O(N^{-1/2}|v|^3),\qquad
 \mathcal B_\beta(y)=\mathcal B_\beta(y_*)
                                      +O(N^{-1/2}|v|).
 \tag{14}
\]
On a sufficiently small fixed segment its real phase is at most
\(\Re\mathcal P_\beta^+-c|y-y_*|^2\), for one uniform \(c>0\).
Split the rescaled integral at \(|v|=N^{1/12}\).
Outside that range the quadratic upper bound is exponentially
small in \(N^{1/6}\). Inside it, the Taylor remainders are
bounded by an integrable Gaussian times
\(O(N^{-1/2})(|v|+|v|^3)\). Integration to the actual endpoint
\(t_N\) therefore has additive error \(O_T(N^{-1/2})\).
The lower endpoint can be extended to \(-\infty\) with an
exponentially small error. Multiplying the factor \(N^{-1/2}\)
from \(dy\) by (12), and using (13), proves (11).
\(\square\)

In particular the half-grid nearest \(\alpha\), namely \(c_N(0)\),
has the nonzero transition
\[
 Q_N(c_N(0))-Q_N(c_{0,N})
   =\tfrac12N^{-2-\beta/2}\mathcal A_\beta^+
        e^{N\mathcal P_\beta^+}(1+O(N^{-1/2})).
 \tag{15}
\]
If instead a cut stays a fixed distance to the right of the
local segment and inside \(P\), the full local theorem and
Section 2 give the entire original leading coefficient, with
its original relative \(O(N^{-1})\) error. Thus the change in
the complete signed quantity is nonzero at the geometric rate.

## 4. What moving the cut does not determine

The preceding theorem retains the physical sum and current
together. In particular it does not identify a coefficient-index
Fourier observation with a partial physical sum. The
[low-node family packet](research_mixed_next_low_node_family_packet.md)
concerns response coefficients \(a_j(r^b)\), with a fixed small
incoming range \(b\le\delta N\); its Gaussian and prescribed phase
correction act in \(j\). The present partial sum instead retains
the physical \(b\)-band and the full Newton observation
\(C_{\beta,N}(r^b,Z)\). The latter cost remains explicit in
[the weighted coefficient theorem, Section 4](research_mixed_next_low_weighted_coefficient_bound.md).

The paired-left reduction left precisely
\[
                         Q_N(c_{0,N})+V_N^{\rm deep}.
 \tag{16}
\]
Moving the cut changes \(Q_N\) by (4),(11), while (16) is
recovered by subtracting that same change. It therefore retains
an additive value that neither the local Gaussian nor the
exponentially constant portions in Section 2 determine.
No bound for (16), or for its three original terms separately,
is inferred here. A bound at one source-valid starting cut,
or another estimate coupling the physical band to its full
vertical current, is still needed to pay the paired left
remainder.

The result supplies actual finite-source propagation and its
nonzero Gaussian transition, not a whole next-transfer theorem.
