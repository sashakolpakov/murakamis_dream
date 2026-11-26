# The original outgoing zero lift and its paired period root

Private exact-source phase deduction, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source edit
is used.

The original outgoing conditional phase has one critical point in
its upper physical index strip along the entire real middle input
arc. Its logarithmic lift is zero. Under the signed transpose,
this selected critical point pairs with the period root outside
the sine-weight circle. The rational trace coordinate \(F^2/E^2\)
is the other outgoing critical root. Keeping this interchange is
essential.

This supplies a source-specific filter on the rational trace locus.
It does not exclude that filtered locus, prove a contributing
contour, or estimate the remaining coherent observation.

## 1. Original coordinates and the two exponential conventions

Let the real incoming coordinate be
\[
 a\in[1/2,5/6],\qquad
 x=e^{2\pi ia},\qquad Y=x^{-1}=e^{-2\pi ia}.
                                                                    \tag{1}
\]
For the actual words in powers three and four beginning \(343\),
of length at least five, the original outgoing source has
\[
 z_*=u+ih,\qquad
 3/10\le u\le39/100,\qquad -3/100\le h\le1/50,\qquad
 Z=e^{-2\pi iz_*}.
                                                                    \tag{2}
\]
These closed containing ranges obey
\(\Re Z<0,\Im Z<0,\ 4/5<|Z|<8/7\), by the original
[weighted outgoing domain](research_mixed_next_middle_weighted_outgoing_kernel.md).
The strict radius witnesses remain valid at the displayed closed
height endpoints.

Use its unchanged phase
\[
 Q(s;a,z_*)=
 g(a+s)+g(z_*+s)-2g(s)-g(a)-g(z_*)+2\pi ias,
 \qquad g'(v)=\Log(1-e^{-2\pi iv})
                                                                    \tag{3}
\]
on the original regular strips. Distinguish
\[
 U=e^{-2\pi is},\qquad T=U^{-1}=e^{2\pi is}.
                                                                    \tag{4}
\]
The exponentiated critical equation and its reciprocal are,
respectively,
\[
\begin{split}
 &(1-YU)(1-ZU)=Y(1-U)^2,\\
 &(1-Y)+(Y-Z)U+Y(Z-1)U^2=0,\\
 &(1-Y)T^2+(Y-Z)T+Y(Z-1)=0.
\end{split}                                                       \tag{5}
\]
Consequently, for the \(T\)-coordinate,
\[
 Z=\frac{1-T+(1-x)T^2}{1-xT}.
                                                                    \tag{6}
\]
The coefficient reversal in (5) is part of the convention.

## 2. One critical point in the original upper physical strip

Put
\[
 P=\cot(\pi a)\in[-\sqrt3,0],\qquad
 Q_0=\cot(\pi z_*)=q_0+i\beta,\qquad S=\cot(\pi s).
\]
The original cotangent calculation in
[global conditional roots, (4)](research_mixed_global_cotangent_roots.md)
is an algebraic identity and gives
\[
 f(S)=S^2+(P+Q_0)S-1+i(Q_0-P)=0.
                                                                    \tag{7}
\]
It remains valid for the present nonpositive real \(P\).

The actual output satisfies
\[
                       q_0>|\beta|,\qquad |\beta|<1/2.
                                                                    \tag{8}
\]
Indeed its positive cotangent denominator is
\(\cosh(2\pi h)-\cos(2\pi u)>1\), and
\[
q_0=\frac{\sin(2\pi u)}{\cosh(2\pi h)-\cos(2\pi u)},\qquad
|\beta|=\frac{\sinh(2\pi|h|)}
                 {\cosh(2\pi h)-\cos(2\pi u)}.
\]
Here \(\sin(2\pi u)\ge\sin(11\pi/50)>1/2\).
Also \(2\pi|h|\le3\pi/50<1/5\), and
\(\sinh(1/5)<1/4\). For the last elementary witness,
the ratios of successive positive terms after \(1/5\)
are at most \(1/150\), so
\(\sinh(1/5)\le(1/5)/(1-1/150)=30/149<1/4\).
This proves (8) with room to spare.

For real \(v\),
\[
 \Re f(iv)=-1-v^2-\beta(1+v)
 \le \frac{\beta^2}{4}-1-\beta<0
                         \qquad(|\beta|<1/2).
                                                                    \tag{9}
\]
The final maximum on \([-1/2,1/2]\) is \(-7/16\).
Thus no root crosses the imaginary \(S\)-axis. When
\(\beta=0\), the discriminant
\((P+q_0)^2+4-4i(q_0-P)\) has a square root with positive
real part strictly larger than \(|P+q_0|\).
Exactly one root is in each open \(S\)-half-plane.
The same remains true throughout the connected domain (8):
on every compact homotopy the monic polynomial's roots stay
bounded, and (9) excludes every boundary crossing.
In particular the right root is simple and varies holomorphically
in a neighborhood of each admitted parameter.

The right root has strictly negative imaginary part.
At \(\beta=0\), the displayed discriminant shows this directly.
A crossing through a positive real root \(S=r>0\) would require
\[
 P=q_0+\beta r,\qquad
 (1+\beta)r^2+2q_0r=1+\beta.
\]
The second identity forces \(0<r<1\), so the first gives
\(P>q_0-|\beta|>0\), a contradiction.

For this root use the original inverse cotangent,
\[
 T=\frac{S+i}{S-i},\qquad
 s=\frac1{2\pi i}\Log T,\qquad 0<\arg T<\pi .
                                                                    \tag{10}
\]
Then
\[
             \Im T>0,\quad |T|<1,\quad
             0<\Re s<1/2,\quad \Im s>0.
                                                                    \tag{11}
\]
The other root of (7) lies in the left \(S\)-half-plane;
its corresponding \(T\) lies in the lower half-plane.

### The incoming factorial wall

We next prove the sharper physical guard
\[
                         0<\Re s<1-a.                            \tag{12}
\]
At \(a=1/2\) it follows from (11). Hold the actual output
fixed and continue in \(a\). A proposed first crossing of
\(\Re s=1-a\) has
\[
 \phi=2\pi(1-a)\in[\pi/3,\pi],\qquad
 x=e^{-i\phi},\qquad T=\rho e^{i\phi},\quad 0<\rho<1.
\]
The denominator of (6) is \(1-\rho>0\). Thus
\[
 Z=\frac{1-\rho(1+\rho)e^{i\phi}
                         +\rho^2e^{2i\phi}}{1-\rho}.
                                                                    \tag{13}
\]
Let \(c=\cos\phi\in[-1,1/2]\). The numerator of its real
part is
\[
             N_c(\rho)=1-c\rho+(2c^2-c-1)\rho^2.
\]
For \(c\le-1/2\), every nonconstant term is nonnegative.
For \(-1/2<c\le0\), this is a concave quadratic, whose
endpoint values are \(1\) and \(2c(c-1)\ge0\).
It is strictly positive for \(0<\rho<1\).
Both cases contradict \(\Re Z<0\).

For \(0<c\le1/2\), the condition \(\Re Z\le0\) would imply
\[
 1\le c\rho+(1+c-2c^2)\rho^2
                 \le\frac{\rho}{2}+\frac98\rho^2.
\]
If \(\rho\le2/3\), the last expression is at most \(5/6\).
Hence \(\rho>2/3\). But then (13) gives
\[
 |\Im Z|
 =\frac{\rho\sin\phi(1+\rho-2\rho c)}{1-\rho}
 \ge\frac{\rho\sin\phi}{1-\rho}
 >\sqrt3>\frac87,
\]
contradicting the original radius bound. This excludes the
wall everywhere and proves (12).

All five single and shifted arguments in (3) now remain in
their original regular strips:
\[
0<\Re s,\quad 0<a+\Re s<1,\quad
0<u+\Re s<89/100<1.
\]
At \(a=1/2,h=0\), the
[original half-endpoint theorem](research_mixed_half_endpoint_conditional_packet.md)
identifies the right cotangent root with the zero logarithmic
lift. Continuation first in \(h\), then in \(a\), retains all
these strips. Since (5) makes \(Q_s\) an integer multiple of
\(2\pi i\), its continuous lift stays zero:
\[
                            Q_s(s;a,z_*)=0.                       \tag{14}
\]
This proof identifies the original phase branch, not just a
root of its exponentiation. On the compact domain (1)--(2),
all strict guards have uniform margins.

At a physical incoming node \(a=b/N\), the complete outgoing
sum stops exactly at \(k=N-1-b\). The difference between this
endpoint divided by \(N\) and \(1-a\) is \(1/N\), so (12)
places the critical point before that endpoint for large \(N\).
No assertion about dominance, a retained small-\(k\) cut,
or a complete finite packet follows from this location.

## 3. Which period root is paired with that saddle?

Use \(z\) now for the period shift in the original signed
transpose, exactly as in
[paired Newton characteristics, (26)--(27)](research_mixed_next_outer_paired_newton_characteristics.md).
The outgoing parameter is still denoted by the capital \(Z\).
At the critical point, the original incoming derivative is
\[
 \exp(\partial_a Q)
     =T\frac{1-Y/T}{1-Y}
     =\frac{T-Y}{1-Y}.                                             \tag{15}
\]
The signed outgoing coefficient is \((-q)^b C_b\), with
\(q=e^{\pi i/N}\).
Its formal characteristic ratio is therefore the negative of (15);
the paired period ratio is its reciprocal. The exact
characteristic correspondence is
\[
 \boxed{\qquad z=-\frac{1-Y}{T-Y},\qquad
                  T=Y-\frac{1-Y}{z}.\qquad}                       \tag{16}
\]
This is also verified without assuming a finite asymptotic:
substitute \(L=(T-Y)/(1-Y)\) into
\[
 Z=\frac{Y(Y-1)}{L}+3Y-2Y^2+(1-Y)^2L.
\]
It yields exactly (5). Substituting \(L=-1/z\) gives the
original signed transpose
\[
 Z=\frac{3x-2+(x-1)z-(x-1)^2/z}{x^2}.
                                                                    \tag{17}
\]
Thus (16) is a principal algebraic pairing rule; it does not
assert that the actual finite sum has a ratio asymptotic.

## 4. The trace coordinate represents the other root

Keep the polynomials \(A,B,C,D,E,F\) of
[the rational trace locus, (5)--(8)](research_mixed_next_outer_principal_rational_trace_locus.md).
At a common principal root,
\[
 x=D/F,\qquad z=-A^2/E^2,\qquad
 Z=F^2+1-AF/E.
\]
Set
\[
                         w_0=F^2/E^2.
\]
The determinant identities in that theorem give
\[
 z+1=xw_0,\qquad A^2=(1-x)^2w_0,\qquad
 Z=\frac{1-w_0+(1-x)w_0^2}{1-xw_0}.                               \tag{18}
\]
Here \(1-xw_0=A^2/E^2\ne0\).
Thus \(w_0\) is a critical coordinate of the type in (4),
but (16) pairs the period root with
\[
 \boxed{\qquad
 T=\frac{1-w_0}{1-xw_0}
       =\frac{E^2-F^2}{A^2}=1-\frac{EF}{A}.
 \qquad}                                                         \tag{19}
\]
The two values in (18)--(19) are the two roots of the same
quadratic (5): their product is
\((Z-1)/(x-1)\), as follows directly from (18).
They are distinct on the actual domain, since the cotangent
roots have opposite real-part signs.

Consequently the selected original outgoing sheet corresponds
to \(\Im T>0\), or equivalently
\[
                         \Im(F^2/E^2)<0.                         \tag{20}
\]
Using the upper-half-plane condition on \(F^2/E^2\) instead
would select the opposite period root. For example at \(x=-1\),
\[
 T=\frac{1-w_0}{1+w_0},
\]
which reverses the two half-planes.

## 5. The selected period root is outside the weighted circle

The
[outgoing weighted energy theorem](research_mixed_next_outgoing_weighted_energy.md)
excludes any root of the principal signed outgoing symbol on
its sine-weight circle. Explicitly, put
\[
                       \sigma=|x-1|=2\sin(\pi a).
\]
The outgoing sequence-ratio circle is \(|L_{\rm signed}|=
\sigma^{-1/2}\); the paired period-ratio circle is
\[
                              |z|=\sqrt{\sigma}.                  \tag{21}
\]
To see the exclusion directly in the source proof, its
limiting unit row normalization makes the two weighted
off-diagonal terms conjugates of magnitude \(\sigma^{3/2}\).
On a unit Fourier character the real part after the fixed
rotation \(1+3i\) is therefore bounded below by its diagonal
real part minus \(2\sigma^{3/2}\). This is exactly the
strict energy expression (13)--(14) in that theorem.
It is positive throughout the actual containing \(Z\) region.
Thus the principal symbol cannot vanish on (21).

At \(a=1/2\), the selected root \(T\) satisfies
\[
 Z=2T-3+\frac4{1+T},\qquad
 \Im Z=\Im T\left(2-\frac4{|1+T|^2}\right).
\]
Since \(\Im Z<0<\Im T\), one has \(|1+T|<\sqrt2\).
Equation (16), not \(z=-1-T\), gives
\[
                       z=-\frac2{1+T},\qquad |z|>\sqrt2.
                                                                    \tag{22}
\]
The product of the two period-root moduli is
\(|x-1|=\sigma\), from the original quadratic
\[
(x-1)z^2+(3x-2-x^2Z)z-(x-1)^2=0.
\]
The other root is therefore strictly inside the circle at
\(x=-1\). As \(a\) varies, the circle exclusion prevents
either root from crossing it. No root is zero or escapes
to infinity on the compact arc; a double root would have
modulus \(\sqrt{\sigma}\), also excluded. It follows that
there is exactly one root on each side of (21), and the
selected outgoing zero lift pairs with the outside root
throughout:
\[
                  \boxed{\quad |z|>\sqrt{|x-1|}.\quad}             \tag{23}
\]

On the rational trace locus this last condition is exactly
\[
                            |A|^6|F|^2>|E|^{10},                 \tag{24}
\]
using \(z=-A^2/E^2\) and \(x-1=-AE/F\).
Equations (20) and (24) are equivalent sheet filters when
the outgoing image lies in the actual domain (2).

The remaining separation problem is now precise: exclude,
or locate, points of the original compact trace locus
\(\Gamma\) whose outgoing image is actual and which satisfy
(20), equivalently (24). No inequality here excludes those
points. The inside period root is the other outgoing sheet;
discarding it does not prove avoidance of the outside root,
control transformed forcings or endpoints, or bound the
remaining coherent sum.

