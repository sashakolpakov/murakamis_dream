# The complete upper continuation of the shortened second edge

Private written finite-source proof, 8 November 2026. A planar
strict-sublevel argument supplies the missing upper path for the
actual positive outer family. The argument uses the continuous
original reciprocal-factorial envelope, including its upward
normal-derivative jumps. It does not suppose that either
numerator-zero starting action is already below the saddle.

Both external endpoint groups and every Fourier denominator remain
those of the adopted joined representation. No numerical evaluation
or edit of a frozen source is used.

## 1. A planar sublevel criterion

Here is the topological assertion used below. It does not require
regular level sets along the exceptional curves.

**Lemma 1.** Let \(R=[a,b]\times[0,V]\), and let \(U\) be continuous
on \(R\) and subharmonic in its interior. Fix \(m\in\mathbb R\).
Suppose:

1. \(U>m\) on the top edge.
2. No point with \(U<m\), except possibly on the two vertical sides,
   is a local minimum relative to \(R\).
3. On each vertical side the strict sublevel trace \(U<m\) is
   nonempty and connected.
4. There is an interior point \(p\) with \(U(p)=m\), near which
   \(U\) is the real part of a holomorphic function with a
   nondegenerate critical point.

Then \(\{U<m\}\), considered relative to \(R\), has exactly two
connected components. Each meets precisely one vertical side.
The two local descending sectors at \(p\) belong to different
components. Any two interior points in one component can be joined
by a piecewise smooth path in the open rectangle on which \(U<m\).

*Proof.* The strict sublevel set is relatively open in a rectangle,
so its components are relatively open and path connected. Let \(C\)
be one component. Its closure is compact. The minimum of \(U\) on
that closure is strictly less than \(m\), since \(C\) is nonempty.
At a minimizing point \(z\), a sufficiently small relative ball is
contained in \(\{U<m\}\). That ball is connected and meets \(C\),
so it belongs to \(C\). Thus \(z\) is a local minimum relative to
the rectangle, not merely a point on a different component's
boundary. Assumptions 1--2 put \(z\) on a vertical side.

Each side trace in assumption 3 is connected, so it lies in a
single component. Every component meets one of those traces.
There are consequently at most two components.

The two local descending sectors cannot belong to the same
component. Here are explicit details of the separation argument.
In a small holomorphic coordinate \(w\) centered at \(p\), the
nondegenerate critical point gives
\[
                     U-m=\Re w^2 .
\tag{1}
\]
Indeed the holomorphic difference has the form
\((z-p)^2g(z)\), \(g(p)\ne0\), and one may take a local square
root of \(g\). The short imaginary \(w\)-axis is a simple
descending crosscut through \(p\); its two halves have \(U<m\).
The two real \(w\)-axis germs have \(U>m\).

If the descending halves belonged to one component, join points
on them by a path in that strict sublevel. The path can be chosen
simple and piecewise smooth, entirely in the open rectangle.
To justify the latter assertion even when an initial path uses
the boundary, its compact image has a positive strict-sublevel
margin; a sufficiently small affine contraction of the rectangle
toward an interior point, followed by short endpoint connectors,
pushes the path into the interior while preserving that margin.
It may then be replaced by a polygonal simple arc in the same
open set.

Perturb this arc within the strict sublevel so that it meets the
short descending crosscut transversely in finitely many points.
It stays a positive distance from \(p\). In the ordered list of
intersections, including the two endpoints, some consecutive
pair lies on opposite halves of the crosscut. The intervening
subarc has no other intersection with that crosscut. Together
with the crosscut segment through \(p\), it is a Jordan curve
in the open rectangle. Its boundary has \(U\le m\). Near \(p\),
one of the two ascending real-\(w\) germs lies inside this curve:
the descending crosscut is locally a simple arc, and those two
germs lie on its opposite sides. Hence the bounded interior has
a point with \(U>m\). This contradicts the maximum principle for
the continuous subharmonic function \(U\) on that Jordan domain.

There are therefore at least two components, and hence exactly
two. They contain the two different side traces; neither can
meet both sides. The same interior-pushing argument gives the
last path assertion. No regularity of the level set \(U=m\)
away from the small saddle neighborhood was used. \(\square\)

## 2. The actual source and its subharmonic upper rate

Keep the compact actual family and original cubic branch:
\[
 u=b-iK,\quad 0\le b\le\pi/2,\quad0\le K\le1/2,\qquad
 t=t(u)=a-iH,\quad0<a<\pi/2,\quad0<H<1 .
\tag{2}
\]
The [cubic theorem](research_mixed_next_inner_three_cubic_continuation.md)
and the [first-quarter theorem](research_mixed_next_two_angle_bare_first_quarter_contour.md)
give
\[
 \Re\cos t>0,\quad\Im\cos t>0,\qquad
 \Re\cos u\ge0,\quad\Im\cos u\ge0 .
\tag{3}
\]
All strict actual-family guards are uniform by compactness.
The [upper terminal-region theorem](research_mixed_next_shortened_edge_upper_terminal_regions.md)
also proves \(H>1/2\ge K\).

Use the unchanged interpolation and upper exponent:
\[
\begin{split}
 B_N(y,z)&=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\\
 T_N(y;t,u)&=B_N(y,t)B_N(y,u),\\
 U(y)&=\mathfrak F(y;t,u)
       =\mathfrak b(y,t)+\mathfrak b(y,u).
\end{split}
\tag{4}
\]
Here \(\mathfrak b\) is exactly the sidewise real exponent in
[the uniform factorial theorem, Section 3](research_uniform_factorial_and_boundary_decay.md).
In particular both terms of every reciprocal cosine reflection
are retained. On any compact subset of \(0<\Re y<1/2\), at
bounded heights, that theorem gives
\[
                  |T_N(y;t,u)|\le C N^{-2}e^{NU(y)} .
\tag{5}
\]
It is an upper bound, including all reciprocal-factorial zeros.

For an angular parameter \(z=\theta-iA_0\) from (2), the only
possible interior upper cut of its rate is
\[
 y=x+\frac{iA_0}{2\pi},\qquad
 \frac12-\frac{\theta}{2\pi}\le x<\frac12 .
\tag{6}
\]
If \(A_0=0\) this cut lies on the bottom edge; if \(\theta=0\)
it has no interior horizontal part. The other shifted factorial
has positive real part throughout the open half-strip.

The function \(U\) extends continuously to every closed rectangle
\(0\le x\le1/2,\ 0\le v\le V\). This includes the bottom
endpoints and both starting zeros. It is harmonic away from the
cuts. More particularly, for a negative shifted real argument \(w\)
the original reflection formula is
\[
       -\Re J_{\rm side}(w)=\Re J(-w)+\pi|\Im w| .
\tag{7}
\]
The first term on the right is harmonic there. Across (6),
the wire-height derivative of the second term jumps upward
by \(2\pi\). Thus \(U\) is subharmonic away from the finitely
many starting zeros, with nonnegative distributional Laplacian
on the cut segments. At a starting zero the integrated logarithm
is continuous and has gradient \(O(1+|\log|y-y_z||)\).
Deleting a circle of radius \(\epsilon\) around that point
therefore contributes \(O(\epsilon|\log\epsilon|)\) to the
distributional integration by parts. Its limit is zero.
There is no negative atom at the start of a cut. This proves
subharmonicity on the whole open rectangle. Intersections or
coincidences of cuts add their nonnegative jumps.

The strict horizontal descent on both cuts was proved for this
same envelope in the upper terminal-region theorem:
\[
 U(x_2+iA_0/(2\pi))-U(x_1+iA_0/(2\pi))
       \le (x_2-x_1)\log(9/10)
\tag{8}
\]
whenever the two points lie in (6). The inequality includes
the starting zero by continuity. Consequently no interior
point of a cut, including its starting point, can be a local
minimum. No action comparison at that starting point is needed.

## 3. Bottom, left and right boundaries

These boundary facts are needed for the component count, not
merely for a comparison at small wire height.

On the real bottom, let \(\zeta=\cos(2\pi x)\). The original
one-leg force satisfies
\[
              e^{b_y(x,z)}
                    =\frac{\zeta+\cos z}{1-\zeta}.
\tag{9}
\]
For a strictly lower angular height and \(0<\theta\le\pi/2\),
its original imaginary logarithmic part is the principal
argument in \((0,\pi)\). This follows directly from the two
original shifted sine logarithms: the numerator of (9) has
positive imaginary part, the denominator is positive, and
continuation in \(x\) from zero has no zero or winding.
For a purely imaginary angular parameter it is zero.
The \(t\) leg always has the strict case. If \(K>0\), therefore,
\[
                          U_v(x,0+)<0
                  \qquad(0<x<1/2).
\tag{10}
\]
For \(K=0\), the same assertion holds before the real \(u\)
zero \(x_u=1/2-b/(2\pi)\), with the outgoing imaginary
logarithmic part zero. On and after that zero, use (8)
instead: the bottom cut decreases strictly to the right.
At its starting zero this is still a strict descent direction.
When \(b=0\), the zero is only the right corner, so there
is no exceptional open bottom interval. Thus no bottom point
away from the two side corners is a local minimum.
In particular (10) is not being asserted on the real-\(u\)
bottom cut after its zero.

The left boundary is strictly increasing in height. One
direct check avoids any logarithmic-lift ambiguity. Put
\[
 r=\frac{\theta}{2\pi}\in[0,1/4],\qquad
 s=\frac{A_0}{2\pi}\ge0,\qquad
 \vartheta_r(w)=\arctan\{\tan(\pi r)\tanh(\pi w)\}.
\]
Differentiating the original shifted logarithms at \(y=iv\),
\(v>0\), gives
\[
 \partial_v\mathfrak b(iv,z)
       =\pi-\vartheta_r(s+v)-\vartheta_r(s-v)>0 .
\tag{11}
\]
Indeed \(|\vartheta_r(w)|\le\pi r\) at finite \(w\), and
\(2\pi r\le\pi/2\). The own sine logarithm has argument
\(\pi/2\), which supplies the displayed \(\pi\).
The reflection identity \(J(1-w)=-J(w)\) gives
\(\mathfrak b(0,z)=0\). Hence
\[
                  U(0,0)=0,\qquad U(0,v)
                         \text{ is strictly increasing}.
\tag{12}
\]
Its strict sublevel trace below any positive \(m\) is an interval
containing the lower left corner.

For the complete right boundary use the exact formula established
in the upper terminal-region theorem. Write
\[
 L(r,\sigma)=\Re J(r+i\sigma),\quad \sigma\ge0,\qquad
 \theta_r(\sigma)=\Arg\sin\pi(r+i\sigma).
\]
For \(0<r\le1/4\), \(\theta_r\) increases from zero and
belongs to \([0,\pi/2)\); this also follows from
\(\theta_r'=\pi\Re\cot\pi(r+i\sigma)>0\).
Then
\[
 \mathfrak b(1/2+iv,z)
       =-L(r,s+v)+L(r,|s-v|)+\pi|s-v|.
\tag{13}
\]
For \(0<v<s\) and \(v>s\), respectively,
\[
\begin{split}
 \partial_v\mathfrak b
     &=\theta_r(s+v)+\theta_r(s-v)-\pi
                                      \in(-\pi,0),\\
 \partial_v\mathfrak b
     &=\theta_r(s+v)-\theta_r(v-s)+\pi
                                      \ge\pi .
\end{split}
\tag{14}
\]
For \(r=0\), the limiting values are zero before \(s\)
and \(\pi\) after \(s\). For \(s=0\), the second derivative
formula is simply \(\pi\) for every \(v>0\).
The formulas are used on open intervals; continuity supplies
their monotonic conclusions at a cut height or a boundary zero.

Since \(H>K\), the \(t\) cut is the later one. Below \(K/(2\pi)\)
both legs decrease, with the \(t\) leg strict. Above that height,
the crossed \(u\) leg has derivative at least \(\pi\), while
an un-crossed \(t\) leg has derivative strictly greater than
\(-\pi\); after the \(t\) cut both derivatives are positive.
It follows that
\[
\begin{gathered}
 U(1/2,v)\text{ decreases on }[0,K/(2\pi)],\\
 U(1/2,v)\text{ increases strictly on }[K/(2\pi),\infty),\\
                         U(1/2,0)=(H+K)/2 .
\end{gathered}
\tag{15}
\]
When \(K=0\), the first interval is a point. This covers all
intermediate heights as well as the two degenerate outgoing
angles. Thus every strict sublevel above \(U(1/2,0)\) has a
connected right-side trace containing the lower right corner.

## 4. A finite top and the two saddle sectors

The original action satisfies
\[
            m=\Re\psi(t,u)>(H+K)/2+1/25>0
\tag{16}
\]
by the [endpoint action theorem](research_mixed_next_shortened_edge_endpoint_gap.md).
Both side traces in Lemma 1 are therefore nonempty and
connected, by (12),(15).

There is a fixed finite height \(V\) at which \(U>m+1\)
for all \(0\le x\le1/2\) and all actual parameters.
For completeness, the original sidewise sine primitive has
the formulas
\[
\begin{split}
 J_+(w)&=-\frac{i\pi}{2}(w^2-w+1/6)
                +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iw}),\\
 J_-(w)&=\frac{i\pi}{2}(w^2-w+1/6)
                -\frac{i}{2\pi}\operatorname{Li}_2(e^{-2\pi iw}).
\end{split}
\tag{17}
\]
Their constants are fixed by \(J(0)=0\), as in the
[complete lower-continuation proof](research_mixed_next_shortened_edge_lower_continuation.md).
For \(y=x+iv\) at large positive \(v\), both shifted arguments
have negative imaginary part, while \(y\) has positive imaginary
part. Substitution in the unchanged one-leg phase gives
\[
 \mathfrak b(x+iv,\theta-iA_0)
      =\pi v-\frac{\theta A_0}{2\pi}
                       +O(e^{A_0-2\pi v}).
\tag{18}
\]
The error is uniform in \(x\) and the compact angular family:
each dilogarithm argument has the indicated exponentially
small modulus, and its absolute series is bounded by
\(|w|/(1-|w|)\). Both legs together tend uniformly to
\(+\infty\). Since \(m\) is bounded on the compact family,
the claimed fixed \(V\) exists. Enlarge it to exceed every
selected height \(h_*=\Im y_*\) and the external cap height.

Away from cuts, \(U\) is a nonconstant harmonic function.
One can also check directly that the selected saddle is its
only possible interior regular stationary point. In the
tangent coordinate \(z=\tan(\pi y)\), the original exponential
force has
\[
 e^{F_y}-1
   =-\frac{(z^2+1)(D_0z^2-AB)}{z^4},\quad
 A=\cos^2(t/2),\ B=\cos^2(u/2),\ D_0=A+B-AB .
\tag{19}
\]
For \(0<x<1/2,\ v>0\), \(z\) lies in the first quadrant.
The root \(z^2=-1\) occurs only at infinite height, not in
this rectangle. The sole remaining root is the established
\(z^2=W=AB/D_0\), giving \(y_*\) in the first quarter,
with the original lift \(F_y(y_*)=0\). Different sidewise
logarithmic charges cannot introduce any additional stationary
point since their exponential would still have to equal one.

In its regular neighborhood the original first-quarter theorem
gives
\[
                      \Re F_{yy}(y_*;t,u)<0 .
\tag{20}
\]
This is a nondegenerate harmonic saddle. Its horizontal
left and right germs have \(U<m\), and its vertical germs
have \(U>m\). Harmonicity excludes a local minimum at every
other regular point. Equation (8) excludes a minimum on
the cuts, including their starting zeros, and Section 3
excludes one on the open bottom edge. Thus all hypotheses
of Lemma 1 hold on the fixed rectangle
\([0,1/2]\times[0,V]\).

## 5. Identifying the right component and uniform paths

Retain the original fixed first-quarter cuts
\(\alpha<\Re y_*<\beta<1/4\), the endpoint cut
\(\gamma=1/2-\delta/2\), and the fixed small cap height
\(h_c>0\) from
[the joined-contour theorem](research_mixed_next_shortened_edge_joined_contour.md).
They may be decreased there as specified, without changing
the physical sampling source. In particular \(h_c<\min h_*/2\).
Decrease \(h_c\) once more, if necessary, so that the paid
right real interval \([\gamma,1/2]\) has a whole collar
\(0\le v\le h_c\) below the action. This follows from its
uniform strict real gap and joint continuity, including
the case \(K=0\). Take a slightly larger real interval
inside the original paid endpoint interval to include all
large-level shifts \(\gamma_N\).

The left descending germ lies in the left-side component.
Indeed the horizontal from that germ to \(\alpha+ih_*\)
has \(U<m\) by the strict first-quarter horizontal concavity.
The vertical from \(\alpha+ih_*\) to \(\alpha\) has \(U<m\)
because its height profile is convex, and both its real and
upper endpoints have the established strict gaps. Finally
the real interval from \(\alpha\) to zero has the paid
left endpoint gap. All these statements concern the same
original exponent. Lemma 1 therefore places the right
descending germ, and in particular \(\beta+ih_*\), in the
right-side component.

The point \(\gamma+ih_c\) lies in that right-side component
by this paid collar, which connects it to the right side.
Equivalently its short vertical to \(\gamma\) and the
real interval from \(\gamma\) to \(1/2\) are below the action.
Lemma 1 gives
a piecewise smooth path in the open upper half-strip from
\(\beta+ih_*\) to \(\gamma+ih_c\) on which \(U<m\).
It can cross a reciprocal-factorial cut; the envelope is
continuous there and the exact source is holomorphic.

The resulting paths can be chosen with uniform quantitative
controls, even though a continuously varying path selection
is unnecessary. For each fixed \(u_0\), choose one such
compact path. It has a positive minimum height, a positive
distance from the two vertical boundary lines, bounded
length, and a positive deficit below \(m(u_0)\).
Joint continuity of \(U(y;t(u),u)\), \(m(u)\), and \(h_*(u)\)
preserves a smaller deficit on that same path for all \(u\)
in a neighborhood of \(u_0\). A short vertical connector at
\(\beta\) adjusts its initial height to \(h_*(u)\), still
with a strict deficit, by the original horizontal endpoint
gap and continuity.

A finite cover of the compact actual family now supplies
fixed constants \(v_{\min}>0,V_{\max}<\infty,L<\infty\)
and \(\epsilon_0>0\), together with paths satisfying
\[
\begin{gathered}
 \beta+ih_*(u)\longrightarrow\gamma+ih_c,\qquad
 \text{length}\le L,\qquad v_{\min}\le\Im y\le V_{\max},\\
       0<\Re y<1/2,\qquad U(y;t(u),u)\le m(u)-\epsilon_0 ,
\end{gathered}
\tag{21}
\]
all in one fixed compact subset of the open half-strip.
No regular level-set foliation at a cut has been assumed.

Use exactly the original half-grid cuts
\[
 \beta_N=(\lfloor N\beta\rfloor+1/2)/N,\qquad
 \gamma_N=(\lceil N\gamma\rceil-1/2)/N .
\tag{22}
\]
Their \(O(N^{-1})\) shifts are accommodated by short horizontal
segments at the two path endpoints. Uniform continuity and
the fixed compact deficits preserve (21), with slightly smaller
constants, for all sufficiently large levels of both parities.

## 6. The complete upper current and shortened-edge packet

Define the literal upper continuation from the joined formula:
\[
 \mathcal R_N^+
   =N\int_{\Upsilon_+}
       \frac{T_N(y;t(u),u)}{1-e^{2\pi iNy}}\,dy,\qquad
 \Upsilon_+:\ \beta_N+ih_*\longrightarrow\gamma_N+ih_c .
\tag{23}
\]
Every chosen path in Section 5 lies in the open upper half-strip.
The canonical interpolation is holomorphic there, including all
its reciprocal-factorial zeros. The exact denominator has no pole
there. Cauchy's theorem makes (23) independent of that path;
there is no real sampling residue or artificial middle side.

On these paths,
\[
 |1-e^{2\pi iNy}|^{-1}
       \le(1-e^{-2\pi Nv_{\min}})^{-1}\le2
\tag{24}
\]
for all sufficiently large \(N\). Combining (5),(21),(24),
the bounded length and the original prefactor \(N\), and
then absorbing the polynomial factor into a smaller gap,
gives a fixed \(\epsilon_+>0\) such that
\[
 \boxed{\qquad
 |\mathcal R_N^+|
       \le C e^{N(\Re\psi(t(u),u)-\epsilon_+)},
                      \qquad u\in\mathcal U_+ .
 \qquad}
\tag{25}
\]
This pays the whole exact upper Fourier denominator, not
just its zero-frequency part.

Combining (25) with the adopted joined identity and the
complete lower-continuation bound gives, at both parities,
\[
 \boxed{\begin{split}
 K_N^{<}(t(u),u)
   &= I_N^{\rm edge}
          +O(e^{N(\Re\psi(t(u),u)-\epsilon)}),\\
 I_N^{\rm edge}
   &=N^{-3/2}a_e(t(u),u)e^{N\psi(t(u),u)}
                                      (1+O(N^{-1})),\\
 a_e(t,u)
   &=\frac{\sqrt{2\pi}}
     {4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*;t,u)}}\ne0 .
 \end{split}}
\tag{26}
\]
The square root and all additive phase constants are the
original ones. The algebraic relative error stays in
\(I_N^{\rm edge}\); it has not been relabeled as an exponential
error. The precise finite source is
\[
 K_N^{<}(t,u)=
 \sum_{j=0}^{\lfloor N/2\rfloor-1}
                  e_j(-2\cos t)e_j(-2\cos u).
\tag{27}
\]
Both removed physical endpoint groups, the two complete external
caps, the local Gaussian normalization \(N\cdot N^{-2}\cdot
N^{-1/2}\), and every original Fourier correction are accounted
for by the cited exact joined representation.

## 7. Independent complex neighborhoods and normalized derivatives

The result also supplies the local complex control needed before
a later integration in the first angular variable. This consequence
uses continuity of already strict contour gaps; it does not assert
that the boundary topology hypotheses hold on an unrelated
independent angular box.

Let
\[
 \mathcal G=\{(t(u),u):u\in\mathcal U_+\}\subset\mathbb C^2 .
\tag{28}
\]
There are fixed open neighborhoods
\(\mathcal O'\) and \(\mathcal O\) of this compact graph, with
\(\overline{\mathcal O'}\subset\mathcal O\), on which the
original wire saddle, action and coefficient continue
holomorphically as functions of the two independent variables
\((t,u)\). To see that the continuations are compatible, use
the explicit formula
\[
 W(t,u)=\frac{\cos^2(t/2)\cos^2(u/2)}
 {\cos^2(t/2)+\cos^2(u/2)-\cos^2(t/2)\cos^2(u/2)},\qquad
 y_*(t,u)=\pi^{-1}\arctan\sqrt{W(t,u)} .
\tag{29}
\]
On the graph, \(W\) lies in a compact subset of the first
quadrant and \(1/3<|W|<1\). These strict guards persist in
a fixed neighborhood. The square root and inverse tangent
in (29) therefore give one holomorphic choice there.
All factorial arguments in the saddle's first-quarter
neighborhood remain in their original regular strips.
Consequently \(\psi(t,u)=F(y_*(t,u);t,u)\) has its unchanged
additive constant. The uniform inequality
\(\Re(-F_{yy}(y_*;t,u))>0\) persists after shrinking the
neighborhood and fixes the same holomorphic Gaussian root.
In particular \(a_e(t,u)\) is holomorphic and bounded away
from zero on a smaller fixed neighborhood.

For each base pair on \(\mathcal G\), keep one of the finite
upper paths constructed in Section 5, and the complete lower
path and external caps of the cited source proofs. Every
remote piece has a uniform strict gap on the graph once
the finite cover is chosen. The sidewise upper exponents
and their lower Fourier-penalized versions are jointly
continuous in the independent angular variables, including
at the moving factorial zeros. The original zero-safe
factorial bounds hold on the same fixed compact wire paths
and for the nearby angular variables. Thus the strict
remote gaps persist on a small independent neighborhood
of each base pair.

The omitted real physical intervals also retain their strict
gaps, with an eligible uniform finite estimate in the enlarged
parameter neighborhood. Explicitly, put \(x=j/N\), \(1\le j\le U\).
The real parts of both shifted arguments
\(1/2-x\pm z/(2\pi)\), for nearby \(z=t,u\), remain in a fixed
compact subinterval of \((-1,1)\). The reciprocal bound (4)
of the uniform factorial theorem therefore applies to both,
including their moving zeros. Apply its lower midpoint bound
(1) to the own factorial with argument \(w=x+1/(2N)\);
this is exactly \(G_N(Nx)\). Uniformly for \(0\le x\le1/2\),
\[
 N\,|J(x+1/(2N))-J(x)|=O(1+\log N),
\]
as follows by integrating the original logarithmic sine near
zero and its bounded derivative away from zero. The unchanged
formula (4) consequently gives
\[
 |e_j(-2\cos z)|=|B_N(j/N,z)|
       \le C N^A\exp\{N\mathfrak b(j/N,z)\}
                    \qquad(1\le j\le U)
\]
uniformly on the fixed independent angular neighborhood.
The row \(j=0\) is exactly one and is retained separately.
These estimates are the same original uniform factorial bounds,
not an extrapolation of quadrant-sign inequalities.

Their real row rates are jointly continuous on the compact
physical endpoint intervals. The already strict graph gaps
thus persist nearby, and summing at most \(N\) physical rows
only changes the polynomial factor. The estimates also include
the small half-grid displacements. This is an extension of
absolute endpoint bounds, not of a relative symbol across a zero.

For the central Gaussian piece, move its horizontal height
to \(\Im y_*(t,u)\). Short vertical connectors at \(\alpha\)
and \(\beta\) join it to the saved upper path; their endpoints
and their small neighborhoods have the established strict
gaps. On the Gaussian neighborhood, the regular factorial
expansion and the strict horizontal curvature persist.
The entire lower path may be kept at its saved base position;
its penalized strict gap persists by the same continuity.
No derivative of a parameter-dependent path choice is needed,
because the exact canonical integrals are path independent.

A finite cover of \(\mathcal G\), followed by shrinking
\(\mathcal O\), gives (26) uniformly for independent
\((t,u)\in\mathcal O\), with the same original finite kernel
and some fixed exponential gap. In particular
\[
 E_N(t,u):=
  N^{3/2}e^{-N\psi(t,u)}K_N^{<}(t,u)-a_e(t,u)
       \quad\hbox{satisfies}\quad
 \sup_{\mathcal O}|E_N|\le C/N .
\tag{30}
\]
This function is holomorphic: the finite kernel is an
entire polynomial expression in the two angular cosines,
and the other factors have the fixed holomorphic branches
just described. Cauchy's formula on the smaller fixed
neighborhood gives, for each fixed pair of nonnegative
integers \(r,s\),
\[
 \sup_{\mathcal O'}
   |\partial_t^r\partial_u^s E_N(t,u)|
          \le C_{r,s}/N .
\tag{31}
\]
The derivatives are taken after the displayed exponential
normalization. They do not assert bounds on unnormalized
derivatives without their resulting powers of \(N\).

Equations (26),(30)--(31) are a complete shortened-edge
packet near the actual positive cubic graph. No negative
outer-half family, complete inner three-kernel trace, or
remaining outer signed-observation estimate follows from
them alone. Those further original finite-source integrations
still have to be proved.
