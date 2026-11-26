# Conditional roots along the actual first-attached taper

Research deduction, 7 November 2026. Every pair consisting of the
first attached coordinate and the next ordinary outgoing coordinate
has its original conditional root throughout the unselected
minimum-cutoff taper. The proof uses the existing coupled endpoint
height bound when the first two types are 43. An asymmetric strip
handles the wider first type-three height in the 33 case.

This establishes the phase branch and its ambient curvature. It does
not extend a complete finite conditional packet, prove the neighboring
transport inequality, or pay the compensated boundary functional.
No analytic function or saved certificate is evaluated.

## 1. Elementary taper inclusions

Use the original cutoff from
[the minimum-neighbor contour](research_mixed_minimum_neighbor_contour.md):
\[
 \rho(x)=
 \begin{cases}
 0,&0\le x\le .1,\\
 (x-.1)/.12,&.1\le x\le .22,\\
 1,&.22\le x\le .45,\\
 20(.5-x),&.45\le x\le .5.
 \end{cases}
 \tag{1}
\]
Only this half-period is used below. Its physical complement is not
assigned a conditional phase by this note.

**Lemma 1.** If \(0<x\le .5\) and
\(|h|\le C\rho(x)\), then
\[
 \begin{array}{c|c}
 C& |\Im\cot\pi(x+ih)|<M\\\hline
 7/100&1/2\\
 9/125&64/125\\
 17/250&487/1000
 \end{array}
 \tag{2}
\]
Also \(\Re\cot\pi(x+ih)\ge0\), with equality only at
\(x=.5\), where \(h=0\).

*Proof.* Put \(d=x-.1\) on the early interval, and
\(k=2\pi C/.12\). The exact formula reduces the desired
inequality to
\[
 M\{\cosh u-\cos(2\pi x)\}-\sinh u>0,
             \qquad 0\le u=2\pi|h|\le kd.
 \tag{3}
\]
For \(M<1\), the left side decreases with \(u\).
It therefore suffices to use \(u=kd\). Write the resulting
function as \(F(x)\). Then
\[
 F'(x)=-k\{\cosh(kd)-M\sinh(kd)\}
                           +2\pi M\sin(2\pi x).
 \tag{4}
\]
For the three rows choose respectively
\[
 (\widehat u,S)=
 (11/25,91/200),\quad(453/1000,469/1000),\quad
 (107/250,221/500).
 \tag{5}
\]
Here \(2\pi C<\widehat u<M\) and
\(\sinh\widehat u<S\). Since
\(\cosh u-M\sinh u\) decreases for \(0\le u\le\widehat u\),
\[
 \cosh(kd)-M\sinh(kd)
       >1+\widehat u^2/2-MS.
\]
Direct rational comparisons give, in every row,
\[
 \frac C{.12}\{1+\widehat u^2/2-MS\}>M.
 \tag{6}
\]
Equations (4)--(6) imply \(F'<0\), so only \(x=.22\)
needs checking. Explicit rational endpoint witnesses are
\[
 \begin{array}{c|cc}
 C&\cosh(2\pi C)>A&\sinh(2\pi C)<B\\\hline
 7/100&10981/10000&2272/5000\\
 9/125&11039/10000&4683/10000\\
 17/250&437/400&2203/5000
 \end{array}
 \qquad \cos(.44\pi)<3/16.
 \tag{7}
\]
These follow from \(157/50<\pi<22/7\) and
\[
 \cosh v\ge1+v^2/2+v^4/24,\qquad
 \sinh v\le v+v^3/6+
               \frac{v^5}{120(1-v^2/42)}\quad(0\le v<1),
 \tag{8}
\]
and \(\sin v\le v-v^3/6+v^5/120\) at
\(v=3\pi/50<33/175\). The second inequality in (8) also
proves the three \(S\) bounds in (5). Its geometric remainder
is valid because successive sinh terms after \(v^5/120\)
have ratio at most \(v^2/42\). Finally
\[
 M(A-3/16)-B=
 \frac9{10000},\quad
 \frac{1121}{1250000},\quad
 \frac{27}{200000}>0.
 \tag{9}
\]
For \(x\ge .22\), use \(|h|\le C\) and
\(\cos(2\pi x)\le\cos(.44\pi)\) in (3).
For \(0<x\le .1\), the height vanishes. The real-part
statement follows from the exact cotangent formula. \(\square\)

The larger negative first-cap range has a one-sided inclusion.
From [the skew-strip theorem](research_mixed_skew_cotangent_root_domain.md),
\[
 -.108\rho(x)\le h\le .021\rho(x),\quad 0<x\le .5
 \quad\Longrightarrow\quad
             -1/6<\Im\cot\pi(x+ih)<37/50.
 \tag{10}
\]
The cited theorem proves this for \(.1\le x\le .22\).
For \(x\ge .22\), use (3) separately with
\((C,M)=(.108,37/50)\) and \((.021,1/6)\).
Its left side decreases with \(u\), and the angular cosine
only decreases, so the cited strict endpoint witnesses suffice.
For \(x\le .1\), use zero height.

## 2. The slightly asymmetric root strip

Besides the skew interval in (10), put
\[
                         I=[-487/1000,64/125].
 \tag{11}
\]
For outer cotangents \(P=p+i\alpha,Q=q+i\beta\),
\(p,q\ge0\), \(\alpha,\beta\in I\), both original
conditional polynomials have exactly one simple root in
\(\Re S>0,\ |\Im S|<1\), with their original zero lift.
The same statement holds for the skew interval
\([-1/6,37/50]\), including \(p=0\) or \(q=0\).

Here are the new boundary checks for (11). The quadratic left-side
bound in [the original theorem](research_mixed_global_cotangent_roots.md)
is
\[
 \Re F_0(iv)\le -1+(u-l)+(u+l)^2/4
                  =-27/32000<0,
 \quad l=-487/1000,\quad u=64/125.
 \tag{12}
\]
For the cubic the two equal-sign corners have negative constants
\(2(l^2-1)\), \(2(u^2-1)\) and a nonpositive remaining term.
The larger mixed constant is \(2(u-1)(l+1)\). Where the
remaining product is positive, it is at most
\((1-l)(u-l)^2/4<3/8\). Therefore
\[
 2(u-1)(l+1)+(1-l)(u-l)^2/4
 < -62586/125000+3/8<-1/8.
 \tag{13}
\]
The other mixed constant is smaller. The horizontal boundary
arguments use only \(-1<\alpha,\beta<1\) and are unchanged.
Monic continuation to \(P=Q=1\), the original base counts and
the continuous integer logarithmic lift prove the assertion.

Allowing nonnegative outer real parts weakens none of these
exclusions. On \(S=v\pm i\), \(v>0\), the quadratic
inequalities remain strict when \(p\) or \(q\) is zero.
The cubic upper-side numerator contains \(v(\beta+1)^2>0\);
the lower-side factor arguments still belong to \((0,\pi/2)\)
and \((-\pi,0)\). Use the \(\Log_{(0,2\pi)}\)
inverse cotangent from
[the closed-boundary theorem](research_mixed_closed_cotangent_roots.md).
It agrees with the original inverse in the interior and is regular
at the negative real ratios on \(p=0\) or \(q=0\).
Thus simplicity, original lift and local holomorphic extension
hold there too.

The pair determinants stay positive: the selected inner cotangent
has positive real part and imaginary part of modulus less than
one, while each outer cotangent has nonnegative real part and
imaginary part of modulus less than one. The original own
factorials and allocated halfweights add nonnegative real diagonal
terms. The original full and Schur Hessians are therefore accretive,
uniformly on each compact target product here. This is fixed-height
ambient curvature, not concavity after substituting a varying-height
graph.

## 3. Actual first-attached references

Consider either an ordinary-ended open word with an ordinary second
vertex, or a positive three/four Fourier prefix of length \(m\ge2\)
ending in four. Write \(a=t_{1,*}\), \(b=s_{2,*}\),
\(t=t_{2,*}\). The actual first-cap and full-bidisk images give
\[
 \begin{array}{c|c}
 \text{coordinate type}&\text{reference height}\\\hline
 a\text{ of type three}&(-.072,.021)\\
 a\text{ of type four}&(-.108,-.020)\\
 t\text{ ordinary type three}&(-.065,.068)\\
 t\text{ ordinary type four}&(-.102,-.001).
 \end{array}
 \tag{14}
\]
The sources are the
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md),
[full-bidisk image theorem](research_mixed_cyclic_critical_height_bounds.md),
and their actual Fourier-reference identification in Section 1 of
[the coherent main-sheet theorem](research_mixed_fourier_prefix_coherent_main_sheet.md).
No refined cyclic rectangle is used at this boundary.

When the first two types are 43, the existing
[coupled attached-height theorem](research_mixed_first_four_attached_height_bound.md),
Theorem 1, gives
\[
                              \Im a>-.070.
 \tag{15}
\]
Its proof concerns compatibility of the endpoint map
\(a=E_4(b)\) and the ordinary map
\(B_0(a,c)=(b,t)\), with \(c=s_{3,*}\in K_3\cup K_4\).
These are exactly the actual Fourier-prefix equations too. A
four-ending Fourier prefix with initial types 43 has \(m\ge3\).
At \(m=3\), its third vertex has type four and its left leg
is in \(O_4\subset K_4\), by the already established ordinary
update with the Fourier inverse leg. At larger lengths the same
typed inclusion follows from the ordinary maps. Thus the same
compatibility extraction proves (15), with no new saved arithmetic.
This does not claim (15) on the whole independent endpoint input
disk or at an ordinary two-endpoint word of length two.

For the minimum-cutoff graph of (1), each retained height is its
reference height times a minimum that includes its own cutoff.
The actual hybrid graph in
[the shallow-taper theorem](research_mixed_left_boundary_shallow_taper.md),
equation (9), instead uses the upper cutoff
\(R(x)=400(.5-x)^2\) on \([.45,.5]\).
It obeys \(R(x)\le20(.5-x)=\rho(x)\), because
\(0\le.5-x\le1/20\). Thus (1) is a containing envelope
for that graph too, rather than an assertion that the two graphs
coincide. In either case,
\(|h_j|\le |\Im z_{j,*}|\rho(x_j)\), with the original
sign retained. Additional fixed factors in \([0,1]\) preserve
this statement.

**Theorem 2.** If \(.1\le x_1\le .22\) and
\(0<x_2\le .5\), the ordinary conditional factor between
these targets has its unique original zero-lift root and accretive
allocated phase for every actual reference in (14). The four cases
are covered as follows:

| First type / second type | Cotangent domain used |
|---|---|
| 33 | First imaginary cotangent lies in \((-1/6,64/125)\), second in \((-487/1000,487/1000)\); both lie in (11). |
| 34 | Both lie in the skew interval of (10). |
| 43 | By (15), both heights are bounded by \(.070\rho\); Lemma 1 gives the old open half-strip. |
| 44 | Both lie in the skew interval of (10). |

These branches identify the actual reference, not just some root
at the target. The actual private coordinate \(s_{2,*}\)
lies in the selected inner cotangent strip. For type three,
\(\Re s_{2,*}>.267>1/4\) makes
\(|\Im\cot\pi s_{2,*}|<1\) automatic. For type four,
\(\Re s_{2,*}>.24\), \(|\Im s_{2,*}|<.102\), and
\[
 \cos(.48\pi)=\sin(.02\pi)<11/175
       <1-.204(22/7)<e^{-.204\pi}
\]
give the same conclusion by the exact cotangent criterion.
The actual original conditional equation therefore has its root
in the uniquely selected strip. The reference outer coordinates
also belong to their respective taper domains, since their real
parts lie in \((.22,.45)\), where the cutoff equals one.

At \(x_2=.5\) use the closed-real-part extension in Section 2.
On compact subsets with \(x_2>0\), all root, branch and
curvature margins are uniform. The original chirp, incoming and
outgoing halfweights and actual complex reference marginals are
unchanged.

This proves conditional-root eligibility for the full first-attached
taper heights, including the positive type-three neighbor heights
outside the earlier skew strip. It does not import the older finite
conditional-source packets, whose target rectangles have smaller
heights and lower real endpoints. The compensated left-boundary sign
still requires a complete source bound on these targets and the
adjoining ordinary derivative and allocation comparison, with the
middle energy and relative pinning fee retained. Root existence alone
supplies none of those signs.
