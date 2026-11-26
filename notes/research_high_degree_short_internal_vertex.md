# An isolated filling in terms of degree and crossing power

Research proof, 2 November 2026. A large degree or a sufficiently large
crossing power supplies the small parameter in this argument. In
particular, a vertex with at least 128 incident edges permits every
fixed crossing power, including zero. Every crossing power is fixed
before the level tends to infinity. The frozen manuscripts are
unchanged.

## 1. The polynomial whose asymptotic is proved

Let

\[
 K_N(t,u)=\sum_{k=0}^{N-1}e_k(-2\cos t)e_k(-2\cos u)
\]

be the complete edge kernel, with the Newton polynomials and closing
functional of the
[finite contraction](../papers/circle-tree-volume/finite-bounds.tex).
Suppose an original vertex has degree \(d\ge1\). Leave its
\(d\) neighboring boundary angles \(\mathbf u=(u_1,\ldots,u_d)\)
unfilled, and put

\[
 P_{d,n,N}(\mathbf u)
 =\mathcal D_{n,N}^{(t)}
       \left[\prod_{j=1}^d K_N(t,u_j)\right],
 \qquad n\in\mathbb Z.                                  \tag{1}
\]

Here \(\mathcal D_{n,N}f=\phi_N(R^nf)\) is the original
complete-meridian trace. Reduction is performed only in this trace.
The product in brackets is the full polynomial, of degree at most
\(d(N-1)\) in \(-2\cos t\); it is not replaced by its values at
the distinct spectral roots. Thus all first normal derivatives are
retained. The resulting polynomial has degree at most \(N-1\) in
each \(-2\cos u_j\).

Use the edge phase and amplitude

\[
 \psi(0,0)=M_\infty=\frac{4G}{\pi},\qquad
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                    (\tan(t/2)\cos(u/2)),\qquad a_e(t,u),
                                                               \tag{2}
\]

where \(G=\sum_{k\ge0}(-1)^k/(2k+1)^2\), and the branches and
nonzero amplitude are those of the
[exact edge expansion](../papers/circle-tree-volume/edge-packet.tex).
Define

\[
 F_{d,n}(t,\mathbf u)
 =\sum_{j=1}^d\psi(t,u_j)+\frac{in}{4\pi}t^2-it.
                                                               \tag{3}
\]

**Theorem.** Suppose the fixed degree \(d\ge1\) and fixed integer
crossing power \(n\) satisfy

\[
             d^2+n^2\ge\max\{1024,128d\}.                \tag{C}
\]

Then the following assertions hold.

1. There is a unique critical point \(t_*=t_{d,n}(\mathbf0)\)
   of (3) in \(|t|\le1/4\). It is nonzero and lies in the lower
   half-plane. It continues holomorphically to \(t_{d,n}(\mathbf u)\)
   on a complex polydisk about \(\mathbf0\).
2. Write

\[
 S_{d,n}(\mathbf u)=F_{d,n}(t_{d,n}(\mathbf u),\mathbf u),
 \qquad M_{d,n}=\Re S_{d,n}(\mathbf0),\qquad
 C_{N,n}=\exp\left(\frac{\pi i n(N-1)^2}{4N}\right).
\]

   On a sufficiently small fixed polydisk,

\[
 P_{d,n,N}(\mathbf u)
 =C_{N,n}N^{-3(d-1)/2}A_{d,n}(\mathbf u)
             e^{NS_{d,n}(\mathbf u)}
             (1+O_{d,n}(N^{-1})),                          \tag{4}
\]

   uniformly through all sufficiently large integer levels. The
   amplitude is holomorphic and nonzero, and the normalized error is
   holomorphic. Its fixed derivatives have the same order on smaller
   polydisks.
3. There are positive constants \(c,B,b,C\) and a finite constant
   \(A\), allowed to depend on the fixed \(d,n\), such that

\[
 |P_{d,n,N}(\mathbf x+i\mathbf y)|
 \le CN^A\exp N\left\{
     M_{d,n}-c\sum_{j=1}^d(1-\cos x_j)
                         +B\sum_{j=1}^d y_j^2\right\},   \tag{5}
\]

   for \(|x_j|\le\pi\), \(|y_j|\le b\).
4. The boundary phase is separately even and has Hessian

\[
 \frac{\partial^2 S_{d,n}}{\partial u_j\partial u_k}
          (\mathbf0)
   =-\delta_{jk}\frac{\cos(t_*/2)}{2\pi}.
                                                               \tag{6}
\]

   In particular its real part is negative definite.

Condition (C) holds for every integer \(n\) when \(d\ge128\).
It also holds for every \(d\ge1\) when \(|n|\ge64\), since
\(d^2+64^2-128d=(d-64)^2\). Thus a sufficiently large degree
places no restriction on the short power. This theorem fills one
original vertex. It does not by itself justify filling adjacent short
vertices successively.

## 2. A small critical point for every signed power

For \(|t|\le1/4\), set

\[
 Q(t)=\frac{2\operatorname{arsinh}(\tan(t/2))}{t}
     =\int_0^1\sec(st/2)\,ds,\qquad Q(0)=1.
                                                               \tag{7}
\]

The integral fixes the holomorphic branch. On this disk,

\[
 |Q(t)-1|<\frac1{100},\qquad |Q'(t)|<\frac1{25}.         \tag{8}
\]

For explicit bounds, \(\cosh(1/8)-1<1/125\), so
\(|\sec z-1|<1/124<1/100\) for \(|z|\le1/8\).
Also \(|\tan z|\le\sinh(1/8)/(1-1/125)<0.128\) and
\(|\sec z|<125/124\). Differentiating the integral in (7)
then bounds \(|Q'|\) by
\((125/124)(0.128)/4<1/25\).

For a real charge \(0\le\lambda\le1\), replace the last term of
(3) by \(-i\lambda t\), and set all boundary angles to zero.
The critical equation is exactly

\[
 t=\frac{-2\pi i\lambda}{dQ(t)-in}.                      \tag{9}
\]

Put \(R=(d^2+n^2)^{1/2}\). On the disk in question the denominator
has modulus at least \(99R/100\). The right side of (9) has
modulus at most \(200\pi/(99R)<7/32<1/4\), and its derivative
has modulus at most

\[
 \frac{2\pi d}{25(99R/100)^2}<\frac{1}{128}.
\]

It is therefore a contraction. It gives a unique critical point
\(t_\lambda\), depending analytically on \(\lambda\), and every
critical point in the disk must be this fixed point. In particular
\(t_0=0\). If \(Q(t_\lambda)=a+ib\), taking the imaginary part
of (9) gives the exact identity

\[
 -\Im t_\lambda
 =\frac{2\pi\lambda d a}{|dQ(t_\lambda)-in|^2}>0
                 \qquad(\lambda>0).
\]

Using (8),

\[
 |t_\lambda|\le\frac{7\lambda}{R},\qquad
 0<-\Im t_\lambda\le\frac{7\lambda d}{R^2}.
                                                               \tag{10}
\]

The stationary value at charge \(\lambda\) has real derivative
\(\Im t_\lambda\). Integration from zero to one proves

\[
 0<dM_\infty-M_{d,n}
       \le\frac{7d}{2(d^2+n^2)}\le\frac{7}{256}
       <\frac\pi{100}.                                  \tag{11}
\]

At unit charge put \(h=-\Im t_*>0\). We have \(h\le7/128\), and
\(|\Re t_*|<7/32<a_0\), where \(a_0=6/25\). Also,

\[
 a_0^2+(7/128)^2<1/16.
\]

Thus the whole rectangle \(|\Re t|\le a_0\), \(|\Im t|\le h\)
lies strictly inside \(|t|<1/4\), and its lower side contains
the selected critical point in its interior.

Finally, throughout this rectangle,

\[
 \frac{\partial^2 F_{d,n}}{\partial t^2}(t,\mathbf0)
       =\frac{-d\sec(t/2)+in}{2\pi},\qquad
 \Re F_{d,n,tt}<0.                                      \tag{12}
\]

Indeed the real part of \(\sec(t/2)\) is positive for
\(|\Re t|<\pi\). Equation (12) also proves nondegeneracy and
the holomorphic continuation asserted in the theorem.

## 3. Discarding wire indices before taking the trace

Retain the same interval \(I=[1/5,3/10]\) in each edge kernel,
and denote the resulting exact kernel by \(K_{N,I}\). Expanding
the difference

\[
 \prod_{j=1}^dK_N(t,u_j)-\prod_{j=1}^dK_{N,I}(t,u_j)
\]

gives precisely the wire assignments with at least one index outside
\(I\). The complete Hermite norm bounds in the finite-contraction
proof apply to each factor. They include first normal derivatives,
the polynomial cost of the fixed signed power \(R^n\), and the
closing functional.

To see their rate explicitly, each low wire index \(k/N=x\)
contributes at most \(2g(x)\), where
\(g(x)=J(2x)-4J(x)\), \(2g(1/4)=M_\infty\), and
\(g''\le-4\pi\). If \(x\notin I\), its rate is at most
\(M_\infty-\pi/100\). A high wire index has only polynomial
norm and loses still more. The remaining edges have rate at most
\(M_\infty\). The number of wire assignments is polynomial in
\(N\), since \(d\) is fixed. Consequently all omitted assignments,
after the original trace, satisfy

\[
 |\text{omitted wire contribution}|
   \le C_{d,n}N^{A_{d,n}}
             e^{N(dM_\infty-\pi/100)},                   \tag{13}
\]

uniformly for every real boundary angle \(|u_j|\le\pi\).
No positivity of a quotient coefficient expansion is used.
By (11), this rate is strictly below \(M_{d,n}\).

## 4. Discarding outer real angles

The real-angle estimate in Section 3 of
[the large terminal-power proof](research_terminal_large_fixed_powers.md)
depends only on the edge kernel, not on its crossing power. It gives

\[
 |K_{N,I}(t,u)|\le CN^A e^{N\psi(a_0,0)}
 \quad(a_0\le|t|\le\pi,\ |u|\le\pi),                  \tag{14}
\]

including the first derivative in \(-2\cos t\) at polynomial
cost. Briefly, before a cosine numerator changes sign its rate is
at most \(\psi(|t|,0)\le\psi(a_0,0)\). After that sign change
it is at most
\(2J(2x)-6J(x)\le3G/\pi+(\log2)^2/(8\pi)<1\), whereas
\(\psi(a_0,0)>1\). The bound on the real interval gives the
derivative bound by the polynomial Markov inequality.

The product of the \(d\) kernels in (14), and its first derivative,
therefore has rate at most \(d\psi(a_0,0)\). The exact derivative
sampling formula for \(\mathcal D_{n,N}\) multiplies these values
only by polynomial factors and unit-modulus chirps at real angles.
Hence the entire outer part of the original trace has that rate.

Furthermore,

\[
 d\{M_\infty-\psi(a_0,0)\}
   =\frac d\pi\int_0^{a_0}\operatorname{arsinh}(\tan(t/2))\,dt
   \ge\frac{d a_0^2}{4\pi}
   >\frac{7d}{2(d^2+n^2)}.                               \tag{15}
\]

The last inequality follows from \(d^2+n^2\ge1024\) and
\(a_0^2/(4\pi)>7/(2\cdot1024)\). Equations (11) and (15) show
\(d\psi(a_0,0)<M_{d,n}\).

Choose a midpoint of the physical grid
\(a_N=\pi-2\pi m_N/N\) with \(a_N\ge a_0\) and
\(a_N-a_0=O(N^{-1})\). Discard the original trace points
\(|\tau_j|\ge a_N\) using (14). For all sufficiently large
levels, the remaining contour rectangle still lies inside
\(|t|<1/4\).

## 5. The exact central trace and its endpoint currents

Let

\[
 f_N(t,\mathbf u)=\prod_{j=1}^dK_{N,I}(t,u_j),\qquad
 g_N(t)=\sin t\,f_N(t,\mathbf u)e^{inNt^2/(4\pi)},
 \qquad \eta=(-1)^{N-1}.
\]

The midpoint version of the
[exact rational trace](research_exact_complete_trace_contour.md)
is

\[
 \begin{aligned}
 \mathcal D^{a_N}_{n,N}f_N
 ={}&-\frac{N^2C_{N,n}}{\pi i}
       \int_{-a_N-ih}^{a_N-ih}
        g_N(t)\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt\\
 &+\frac{\eta N^2C_{N,n}}\pi
       \int_{-h}^{h}\frac{g_N(a_N+iv)}{4\cosh^2(Nv/2)}\,dv.
 \end{aligned}                                           \tag{16}
\]

Every term in (16) is retained. The lower horizontal rational factor
equals \(e^{-iNt}(1+O(e^{-Nh}))\), uniformly along the segment.
It sums all positive Fourier charges, including their multiplicities
from the normal derivatives. Thus the higher charges have an
exponential loss on this same contour.

On the retained rectangle and for small complex boundary angles, the
exact edge expansion gives

\[
 f_N(t,\mathbf u)
  =N^{-3d/2}\prod_{j=1}^d a_e(t,u_j)
           e^{N\sum_j\psi(t,u_j)}(1+O_d(N^{-1})).         \tag{17}
\]

At \(\mathbf u=\mathbf0\), the real part of the phase on the lower
horizontal segment is strictly concave by (12). Its derivative vanishes
at \(t_*\), so that point is its unique maximum, with value
\(M_{d,n}\).

For the vertical current, fold its upper half to the negative lower
endpoint using the oddness of \(g_N\). At either resulting point
\(t=\pm a_N-iv\), \(0\le v\le h\), the reciprocal hyperbolic
cosine factor is at most \(e^{-Nv}\). Its rate is therefore bounded
by \(\Re F_{d,n}(\pm a_N-iv,\mathbf0)\). As a function of
\(v\), this real part is convex, since its second derivative is
\(-\Re F_{d,n,tt}>0\). At \(v=0\) its value is
\(d\psi(a_N,0)\le d\psi(a_0,0)<M_{d,n}\). At \(v=h\)
it is strictly below \(M_{d,n}\) by horizontal concavity. Convexity
places every intervening value below the larger endpoint value.
This proves a strict gap for the full vertical current.

All exterior and endpoint gaps persist on a sufficiently small complex
polydisk in \(\mathbf u\). The selected stationary point continues
there, and the local integral can be moved to its horizontal Gaussian
direction without meeting a singularity. Uniform Gaussian expansion
in (16)–(17) gives (4), with

\[
 A_{d,n}(\mathbf u)
 =i\sqrt{\frac2\pi}\,
   \frac{\sin t_{d,n}(\mathbf u)
             \prod_{j=1}^d a_e(t_{d,n}(\mathbf u),u_j)}
        {\sqrt{-\sum_{j=1}^d\psi_{tt}(t_{d,n}(\mathbf u),u_j)
                                      -in/(2\pi)}}.
                                                               \tag{18}
\]

The square root is the Gaussian branch with positive real part at
\(\mathbf u=0\), continued holomorphically. The numerator is
nonzero there: the edge amplitudes do not vanish, and (9) gives
\(t_*\ne0\), \(|t_*|<1/4\), so \(\sin t_*\ne0\).
The denominator is nonzero by (12). Shrinking the polydisk makes
the entire amplitude nonzero. The powers of \(N\) in (4) are
\(N^2\) from the trace, \(N^{-3d/2}\) from the edge kernels,
and \(N^{-1/2}\) from the remaining Gaussian.

## 6. Keeping all boundary angles and their decay

The [weighted edge-contour bound](research_weighted_edge_contour_bound.md)
holds for all real \(|u|\le\pi\), throughout \(|t|\le1/4\):

\[
 |K_{N,I}(t,u)|\le CN^{-3/2}
      e^{N\{\Re\psi(t,0)-(1-\cos u)/20\}}.             \tag{19}
\]

Multiplying (19) inserts the loss
\(\sum_j(1-\cos u_j)/20\) into every horizontal and vertical
estimate just proved. The discarded wire and outer-angle contributions
have fixed strict gaps below \(M_{d,n}\), independently of these
real boundary angles. As
\(0\le\sum_j(1-\cos u_j)\le2d\), decreasing the angular
constant absorbs those discarded contributions as well. This proves
(5) on the whole real boundary torus, with \(\mathbf y=0\).

Separate evenness of \(\psi(t,u_j)\) gives
\(\psi_{tu}(t,0)=0\). Consequently the critical-point derivative
\(\partial t_{d,n}/\partial u_j\) vanishes at \(\mathbf0\),
and differentiating the stationary action twice gives (6):
\(\psi_{uu}(t,0)=-\cos(t/2)/(2\pi)\). Since \(|t_*|<1/4\),
\(\Re\cos(t_*/2)>0\).

It remains to pass from real angles to a thin complex strip. Near
\(\mathbf0\), (4), (6), and Taylor's theorem give

\[
 \Re S_{d,n}(\mathbf x+i\mathbf y)
       \le M_{d,n}-c_1|\mathbf x|^2+B_1|\mathbf y|^2.
\]

Young's inequality absorbs the mixed real-imaginary quadratic term;
shrinking the polydisk absorbs the higher-order terms. Away from a
fixed small neighborhood of \(\mathbf0\), the real bound has a
fixed gap. To extend that gap, cover the compact real boundary torus
by finitely many products of real spectral intervals. At least one
interval in each product stays away from the complete angle, and can
be enlarged slightly while preserving a real angular gap. Apply the
polynomial Bernstein–Walsh bound in each variable on this product.
The separate degrees are at most \(N-1\), and the corresponding
Green functions tend uniformly to zero as the complex angles approach
the real product. A sufficiently thin fixed complex neighborhood
therefore preserves half the gap. Combining this estimate with the
local quadratic estimate, and reducing \(c\) once more, proves (5).

## 7. What this adds to partial fillings

The theorem supplies the full boundary polynomial of an original filling
whenever (C) holds. In particular it permits every short internal filling
at a vertex with at least 128 incident edges.
Its phase can be complex beyond quadratic order, but it has exactly the
negative real boundary Hessian required by the
[complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md).
Its global bound is of the required form as well. If no two selected
vertices are adjacent, their exact eliminations can be multiplied with
the untouched edge kernels; a neighboring free vertex may occur in
several of these separately even factors. This preserves the local
expansion and global angular loss needed for subsequent independently
long fillings, provided every free coordinate occurs in one of these
factors or in an untouched edge.

Equation (4) is an analytic theorem for the original polynomial and
trace. To conclude a knot-volume identity for such a diagram one must
also keep the original primitive peripheral curves and identify this
stationary action by the actual positive cone deformation and its
absolute volume anchor. Those geometric assertions are separate from
the estimates above. This argument does not settle the isolated short
vertices of degree between two and 127 that fail (C), nor a connected
block of adjacent short vertices. Those cases remain necessary for the
finite-exception goal.

## 8. Reproducing a check of the normalization

The script
[check_internal_vertex_asymptotic.py](../experiments/check_internal_vertex_asymptotic.py)
evaluates the complete finite trace at zero remaining boundary angles
and compares it with the leading term in (4) and (18). It does not
truncate the wire sum. Run

```sh
python3 experiments/check_internal_vertex_asymptotic.py
```

The saved
[results](../repro/results/research-internal-vertex-asymptotic.json)
contain 36 comparisons at 100 decimal digits: the six pairs
\((d,n)=(8,32),(32,56),(64,64),(128,0),(128,1),(128,-7)\)
at levels \(96,97,192,193,384,385\). They test both parities,
zero and negative powers, and the original trace normalization.
The ratios of finite values to the leading formula approach one,
with behavior consistent with the proved \(O(N^{-1})\) remainder.

The leading approximation need not be accurate at modest levels when
the degree is large. For example, at \((d,n)=(128,0)\) the ratios
at even levels \(96,192,384\) are approximately
\(3.116,1.771,1.331\). These numerical comparisons check the
formula and its normalization; the contour proof above establishes
the theorem and its range of validity.
