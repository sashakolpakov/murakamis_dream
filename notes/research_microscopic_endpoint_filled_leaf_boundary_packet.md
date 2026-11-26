# A complex output packet for a filled leaf with microscopic insertions

Private written proof, 16 November 2026.

The actual shortened edge has a uniform two-variable Gaussian packet
near every selected terminal saddle of fixed magnitude at least three.
An extension of the existing wire-ray argument includes the saddle
outside that argument's stated angular domain. Combining this packet
with the strict complementary-current bounds gives a fixed complex
output neighborhood for the whole microscopic-product leaf source.

The nonzero coefficient is uniform for bounded real microscopic
parameters. It may oscillate and depend polynomially on the level.
Complex microscopic parameters have an upper bound only. The source
also retains a whole-output-period Gaussian upper envelope on a fixed
thin strip. No arbitrary-tree closure or volume identification is
asserted.

## 1. Source and theorem

Put \(h=N^{-1}\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 c_j=2\cos((2j+1)\pi/N),\quad
 S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N),\quad
 e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C).
 \tag{1}
\]
The full and shortened kernels are
\[
 K_N(C,Z)=\sum_{k=0}^{D}e_k(C)e_k(Z),\qquad
 K_N^<(C,Z)=\sum_{k<\lfloor N/2\rfloor}e_k(C)e_k(Z).
 \tag{2}
\]
Use the original full-Hermite trace
\[
 \phi_N(f)=\eta\sum_{j<\lfloor N/2\rfloor}
       [(4-c_j^2)f'(c_j)-c_jf(c_j)]
       +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{3}
\]
For fixed \(r\ge0\) and \(n=\sigma m\), \(m\ge3\),
\(\sigma\in\{+1,-1\}\), the actual source is
\[
 B_N(C;\boldsymbol\alpha)=
       \prod_{i=1}^rK_N(2\cosh(\alpha_i/N),C),\qquad
 L_{N,n}(Z;\boldsymbol\alpha)=
       \phi_N[R_N^n B_N K_N(\cdot,Z)].
 \tag{4}
\]
Its original crossing is represented on physical values and first
normals by
\[
 \mathfrak c_{N,n}e^{inNt^2/(4\pi)},\qquad
 \mathfrak c_{N,n}=e^{\pi i nD^2/(4N)},\qquad C=-2\cos t.
 \tag{5}
\]

Let \(J'(y)=\Log(2\sin\pi y)\), \(J(0)=0\), on the original
factorial branches, and set
\[
 b(y,t)=-J(1/2-y+t/(2\pi))-J(1/2-y-t/(2\pi))-2J(y),
 \qquad F(y;t,u)=b(y,t)+b(y,u).
 \tag{6}
\]
The selected wire critical point \(y_*(t,u)\) and its critical
value define
\[
 \psi(t,u)=F(y_*(t,u);t,u),\qquad
 a_e(t,u)=
 \frac{\sqrt{2\pi}}{4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*;t,u)}}.
 \tag{7}
\]
The square root uses the orientation of the wire ray below. It is
positive at positive real \(k=\cos(t/2)\) and \(u=0\).
The additive constant is the original one; in particular
\[
 \psi(t,0)=\int_0^{1/2}
 2\operatorname{asinh}(\cos(t/2)\cot(\pi v))\,dv.
 \tag{8}
\]

Write the positive-power selected point as
\(t_m=2A_m-2iB_m\). For signed \(n\), put \(t_n(0)=2A_m-2i\sigma B_m\).
The implicit equation
\[
 \psi_t(t_n(u),u)+\frac{in}{2\pi}t_n(u)-i\sigma=0
 \tag{9}
\]
defines its holomorphic continuation near \(u=0\). Set
\[
 W_n(u)=\psi(t_n(u),u)+\frac{in}{4\pi}t_n(u)^2-i\sigma t_n(u),
 \qquad
 \lambda_n(u)=-\psi_{tt}(t_n(u),u)-\frac{in}{2\pi}.
 \tag{10}
\]
Thus \(\Re W_n(0)=\mathcal I_n>\mathcal I_2=2G/\pi>0\), where
\(G=\int_0^{\pi/4}\log\cot v\,dv\).
Choose \(\sqrt{\lambda_n(0)}\) with positive real part and continue
it holomorphically on the small output domain.

**Theorem.** Fix \(n,r\) as above and a real bound \(A<\infty\).
There is a fixed complex neighborhood \(\mathcal U\) of the
ordinary output color \(-2\) on which the following holds uniformly
for real \(\alpha_i\in[-A,A]\), including level-dependent choices.
Writing \(Z=-2\cos u\), one has
\[
 \boxed{\quad
 L_{N,n}(-2\cos u;\boldsymbol\alpha)=
 \mathfrak c_{N,n}e^{NW_n(u)}
 A_n(u)\,\mathcal B_N(u;\boldsymbol\alpha)\,[1+\varepsilon_N(u;\boldsymbol\alpha)],
 \quad}
 \tag{11}
\]
where
\[
 A_n(u)=\frac{\sigma i}{\pi}\sin t_n(u)\,
             a_e(t_n(u),u)\sqrt{\frac{2\pi}{\lambda_n(u)}},
 \qquad
 \mathcal B_N(u;\boldsymbol\alpha)=
 \prod_{i=1}^r H_{i,N}^{\sigma}
       \left(\frac{\pi-\pi/N-t_n(u)}{2\pi},\alpha_i\right).
 \tag{12}
\]
The \(H_{i,N}^{\sigma}\) are the actual designated-half endpoint
representatives, normalized at the common bulk reference used in
the whole scalar source. On a smaller fixed neighborhood,
\[
 A_n\ne0,\qquad
 cN^{-r}\le|\mathcal B_N|\le
                  C[(1+\log N)/N]^r,\qquad
 \varepsilon_N=O((1+\log N)^{r+1}/\sqrt N).
 \tag{13}
\]
The error is holomorphic in the output color; all its fixed output
derivatives satisfy the same estimate on smaller neighborhoods.
Every term in (11) is even in \(u\) and descends holomorphically
to \(Z\). In particular the actual source is zero-free on a fixed
output neighborhood for all sufficiently large levels.

For any bounded complex microscopic parameter set, the corresponding
upper assertion is
\[
 \left|e^{-NW_n(u)}
       L_{N,n}(-2\cos u;\boldsymbol\alpha)\right|\le CN^p.
 \tag{14}
\]
All fixed output and microscopic-parameter derivatives of this
normalized function have polynomial bounds on smaller domains.
There is no complex-parameter lower assertion.

There are constants \(c,B,h_0>0\), depending on the fixed data, such
that the same bounded complex parameter sets satisfy
\[
 |L_{N,n}(-2\cos(u+iv);\boldsymbol\alpha)|
 \le CN^p\exp N\{\mathcal I_n-c(1-\cos u)+Bv^2\},
 \quad -\pi\le u\le\pi,\quad |v|\le h_0.
 \tag{14a}
\]
Fixed ordinary output and microscopic-parameter derivatives satisfy
the same type of estimate, with polynomial losses and smaller domains.

The actual local amplitude
\(\mathcal A_{N,n}=A_n\mathcal B_N\) is level-dependent. For real
parameters it is zero-free on the output disk and its fixed logarithmic
output derivatives obey
\[
       |\partial_Z^k\log\mathcal A_{N,n}|
                         \le C_k(1+\log N)^k,\qquad k\ge1.
 \tag{14b}
\]
No level-independent \(A(Z)(1+O(N^{-1}))\) representation of this
decorated amplitude is claimed. The exact normalized amplitude
\(\mathfrak c_{N,n}^{-1}e^{-NW_n}L_{N,n}
 =\mathcal A_{N,n}(1+\varepsilon_N)\) has the same polynomial
upper/lower and logarithmic derivative bounds.

The phase is the calibrated bare terminal boundary action. Its
local curvature is
\[
 W_n'(0)=0,\qquad
 W_n''(0)=-\frac{\cos(t_n(0)/2)}{2\pi},\qquad
                         -\Re W_n''(0)>0.
 \tag{15}
\]
These phase statements do not identify the microscopic boundary
specialization with a filled geometric manifold.

## 2. A ray criterion covering all selected powers

It suffices first to treat the positive-power point. Write
\[
 k=\cos(A_m-iB_m),\quad A=k^2,\quad
 a=\Re A,\quad s=|A|,\quad \gamma=\arg k,\quad
 X=\sin^2 A_m,\quad Y=\sinh^2 B_m.
 \tag{16}
\]
The stationary-geometry source proves
\[
 X<5/8,\quad Y<1/8,\quad 0<A_m<\pi/m,\quad
 \sin A_m=\cosh B_m\tanh(mB_m).
 \tag{17}
\]
It also gives \(k_3=(\sqrt7+i)/4\). For \(m\ge4\),
\(A_m<\pi/4\). Consequently all selected points satisfy
\[
 a\ge3/8,\qquad 1/2\le s<1,\qquad
                      0<\gamma<\pi/6,\qquad a>s^2.
 \tag{18}
\]
Here the first two lower bounds follow from the stated value at
three and, for \(m\ge4\), from
\(a=1-X+(1-2X)Y>1/2\), \(s=1-X+Y>1/2\).
For completeness the remaining inequalities have one uniform proof.
The stationary equation gives \(X>Y\), hence \(s<1\), and
\[
 \tan^2\gamma=\frac{XY}{(1-X)(1+Y)}<\frac5{27}<\frac13.
 \tag{19}
\]
Moreover
\[
 X\ge Y\frac{(3+4Y)^2}{(1+4Y)^2}\ge\frac{49}{9}Y,
 \quad
 a-s^2=X(1-X)-Y(1+Y)>
              X\left(\frac38-\frac{81}{392}\right)>0.
 \tag{20}
\]
These bounds verify one ray criterion for the entire selected
family; no separate contour is chosen for an individual power.

At \(u=0\) put \(z=\tan(\pi y)\). The exact phase equation is
\[
 e^{F_y}=\frac{A-(1-A)z^2}{z^4}.
 \tag{21}
\]
The selected point is \(z=k\). Use the oriented ray
\[
 z=kr,\quad 0<r<\infty,\qquad
 y=\pi^{-1}\arctan(kr)=x+i\omega(x),\quad
 \sinh(2\pi\omega(x))=\tan\gamma\sin(2\pi x).
 \tag{22}
\]
Its endpoints are \(0,1/2\). Along it,
\[
 F_r=\frac{k}{\pi(1+Ar^2)}\Log R(r),\qquad
 R(r)=\frac{1-(1-A)r^2}{Ar^4}.
 \tag{23}
\]
We prove that \(\Re F\) increases strictly to \(r=1\) and decreases
strictly thereafter, using the original logarithm.

For \(r<1\), \(a>s^2\) gives \(\Re(1/A)>1\).
Writing \(R=r^{-4}[r^2+(1-r^2)/A]\), its modulus exceeds one
and its argument is negative. The tangent in (23) has positive
real and imaginary parts, since \(sr^2<1\). Hence \(\Re F_r>0\).

For \(r>1\), \(R\) has positive argument and modulus less than one.
The latter follows by writing \(v=r^2>1\):
\[
 |A|^2v^4-|1-(1-A)v|^2
 =(v-1)[s^2(v^3+v^2)+(2a-1)v+1]>0,
 \tag{24}
\]
because the bracket is at least
\((v^3+v^2-v)/4+1\). Until \(r=s^{-1/2}\) the tangent
has nonnegative imaginary part, so \(\Re F_r<0\).

On the rest of the ray set \(v=r^{-2}\le s<1\). Then
\[
 R=v(A-1+v)/A,\quad 0<\arg R<\pi-2\gamma,\quad
 \frac{|\Im(k/(v+A))|}{\Re(k/(v+A))}
             =\tan\gamma\,\frac{s-v}{s+v}.
 \tag{25}
\]
If \(v\ge1-2a\), then \(|A-1+v|\le s\), so
\[
 -\log|R|\ge-\log v\ge\frac{2(1-v)}{1+v}
                       \ge\frac{2(s-v)}{s+v}.
 \tag{26}
\]
This strictly dominates the argument contribution in (25), since
\(\tan\gamma(\pi-2\gamma)<2\).
The remaining case has \(0<v<1-2a\le1/4\). Now
\[
 |R|^2
 =v^2\left[1+\frac{(1-v)(1-v-2a)}{s^2}\right]
 \le v^2(2-5v+4v^2)\le\frac1{16}.
 \tag{27}
\]
The last polynomial increases on \([0,1/4]\): its derivative is
\(v(4-15v+16v^2)>0\).
Thus \(-\log|R|\ge\log4>4/3\), whereas
\[
 \tan\gamma(\pi-2\gamma)
       <\frac{2\pi}{3\sqrt3}<\frac43.
 \tag{28}
\]
For the last inequality use \(\pi<22/7<2\sqrt3\).
Also \(\log2=2\operatorname{artanh}(1/3)>2/3\).
This proves the strict decrease in the last case.
At the unique maximum,
\[
 F_{rr}(1)=-\frac2{\pi k},\qquad
                 F_{yy}(y_*;t,0)=-\frac{2\pi(1+A)^2}{k^3}.
 \tag{29}
\]
The oriented Gaussian square root in (7) is equivalently defined
using \(\Re(2/(\pi k))>0\) in this real \(r\)-parameterization.

## 3. Reflected aliases and the exact finite shortened sum

The reflected wire ray must also be controlled. Write
\(\cos t=c+id=2A-1\). For \(0\le v\le\omega(x)\), let
\[
 R_v=\cos(2\pi x)\cosh(2\pi v)+c,\qquad
 B_v=\sin(2\pi x)\sinh(2\pi v).
 \tag{30}
\]
Here \(c\) is allowed to be negative. Nevertheless
\[
 B_v\le\tan\gamma,\qquad
 \frac d{\tan\gamma}=4(\Re k)^2
       =4(1-X)(1+Y)>\frac32.
 \tag{31}
\]
Both \(R_v+i(d+B_v)\) and \(R_v+i(d-B_v)\) therefore have positive
imaginary part throughout this region. For
\[
 D_x(v)=\Re F(x-iv;t,0)-\Re F(x+iv;t,0),
\]
the exact differentiation identity from the wire source is
\[
 D_x'(v)=\arg[R_v+i(d+B_v)]+\arg[R_v+i(d-B_v)]<2\pi.
 \tag{32}
\]
Their arguments stay in \((0,\pi)\) without winding. Since
\(D_x(0)=0\), the lower reflected ray with its sampling penalty
has strictly smaller rate than the upper ray:
\[
 \Re F(x-i\omega(x);t,0)-2\pi\omega(x)
                 <\Re F(x+i\omega(x);t,0)\le\Re\psi(t,0).
 \tag{33}
\]
The upper nonconstant sampling term also loses \(2\pi\omega(x)\).
All these inequalities have uniform strict margins on compact
subarcs away from the endpoints.

There is no unaccounted numerator zero in the swept region.
The possible zero in the upper wire strip is
\[
 y_0=1/2-t/(2\pi),\qquad \tan(\pi y_0)=k/\sin(t/2).
 \tag{34}
\]
Since \(\sin(t/2)\) is in the fourth quadrant, its tangent has
argument strictly greater than \(\gamma\); it lies above (22).
The other zero has real part greater than \(1/2\).
The exact factorial continuation therefore uses one consistent
branch on the region between the two truncated rays.

The side of its reflected factorial is fixed as well. Since
\(\tan\gamma=\tan A_m\tanh B_m\) and
\(\tan A_m<\sqrt3<2\cosh^2 B_m\),
\[
 \max_x\omega(x)=\frac{\operatorname{asinh}(\tan\gamma)}{2\pi}
                         <\frac{B_m}{\pi}.
 \tag{34a}
\]
Throughout the region between the two rays,
\(\Im(1/2-y-t_m/(2\pi))=B_m/\pi-\Im y>0\).
In particular a negative real part of that argument always uses
the upper continuation in (38). The other shifted argument has
positive real part and negative imaginary part there.

At the endpoints the original continued phase is
\[
 F(0;t,0)=0,\qquad F(1/2;t,0)=it/2.
 \tag{35}
\]
Its real endpoint rates are \(0\) and \(B_m\).
They are strictly smaller than the selected rate:
\[
 \Re\psi(t_m,0)=\mathcal I_m+
        (1-mA_m/\pi)\,2B_m>\mathcal I_2>1/2>B_m.
 \tag{36}
\]
The last inequality follows already from
\(\sinh B_m<1/2\), or from (17).
As in the scalar source, \(2G/\pi>1/2\) follows from
\(G=\int_0^1\arctan v\,dv/v>\pi/4\).

Choose fixed cuts \(0<\alpha<\beta<1/2\), near the two endpoints,
and move them by \(O(h)\) to grid midpoints. The short endpoint arcs,
their vertical connectors and the omitted real index intervals all
retain strict gaps by (35)--(36) and continuity.
The exact interpolation of each original Newton factor is
\[
 \mathcal E_N(y,t)=
 \frac{N}{
 G_N(N(1/2-y+t/(2\pi))-1/2)
 G_N(N(1/2-y-t/(2\pi))-1/2)G_N(Ny)^2}.
 \tag{37}
\]
It satisfies \(\mathcal E_N(j/N,t)=e_j(-2\cos t)\) as an
ordinary identity, including all parameter derivatives. This uses
the specified factorial reflection \(G_N(z)G_N(N-1-z)=N\).
The reciprocal-factorial identity
\[
 \frac1{G_N(Nw-1/2)}
 =\frac{e^{-i\pi Nw}}N(1+e^{2\pi iNw})G_N(-Nw-1/2)
 \tag{38}
\]
retains both terms whenever a shifted argument enters the upper
negative-real continuation. On the present compact contours their
real parts stay strictly between \(-1\) and \(1\). The midpoint
factorial bounds apply through zero, including all omitted endpoints.
No reciprocal-factorial zero is divided out.

Near the selected wire saddle all factorial real parts lie strictly
in the original positive bulk. Here is the required inequality
explicitly, rather than an inference from the old ray domain:
\[
                 \Re y_*+\frac{A_m}{\pi}<\frac12.
 \tag{38a}
\]
Indeed \(|k|<1\), \(\Re k>0\), and \(\Im k>0\) give
\(0<\Re\arctan k<\pi/4\). For \(m\ge4\), combine this with
\(A_m<\pi/m\le\pi/4\). At the remaining endpoint of the family,
\(k_3=(\sqrt7+i)/4\) gives
\[
 \Re\arctan k_3=\tfrac12\arctan\sqrt7<\pi/5,\qquad
 \cos^2 A_3=(3-\sqrt2)/4,\quad A_3<3\pi/10.
 \tag{38b}
\]
The inequalities follow respectively from
\(\tan^2(2\pi/5)=5+2\sqrt5>7\) and comparison with
\(\cos^2(3\pi/10)=(5-\sqrt5)/8\).
Thus (38a) is strict at every selected point and persists on
its complex neighborhood. The outside arguments \(1/2-y_*\)
are also in the positive bulk. The source-normalized expansion is
\[
 \mathcal E_N(y,t)\mathcal E_N(y,u)=
  \frac{e^{NF(y;t,u)}}{4N^2\sin^2(\pi y)}
                         [1+O_{\rm hol}(N^{-1})].
 \tag{39}
\]
Enclose exactly the retained indices between the cuts by
\(\pi N\cot(\pi Ny)\). Its two constant terms give \(+N\) times
the oriented principal wire integral. The nonconstant terms have
the strict gaps (33), and all connectors have the endpoint gaps.
The original omitted indices obey the midpoint upper bound
\(N^p e^{N\Re F(j/N;t,0)}\), uniformly to both ends, hence their
finite sums are smaller as well.
Equations (29),(39) give the nonzero Gaussian coefficient (7).

All strict contour and endpoint bounds persist on a sufficiently
small complex neighborhood of \(t_m\) and \(u=0\). This uses the
continuous upper factorial exponent at the moving zero faces,
not continuation of an error known only at \(u=0\).
The selected wire saddle moves holomorphically, and the principal
integral is locally deformed through it. The resulting exact packet is
\[
 \boxed{\quad
 K_N^<(-2\cos t,-2\cos u)=
 N^{-3/2}a_e(t,u)e^{N\psi(t,u)}
                         [1+O_{\rm hol}(N^{-1})].
 \quad}
 \tag{40}
\]
Its relative error has every fixed derivative on smaller domains.
At odd \(N=2m_0+1\), the often-used low sum through \(m_0\)
contains one more term than (2). That term has real-end rate
\(B_m\) at \(u=0\), since \(e_{m_0}(-2)=1\) and its degree is
\(m_0\). It belongs to the omitted endpoint interval just bounded.
Thus (40) is for precisely the shortened sum (2), at both parities.
Negative powers follow by coefficientwise conjugation and the
reflected angular chart. No assertion about the full kernel away
from the physical traced rows is needed.

## 4. Preserving every complementary current on an output disk

Fix the actual finite patch partition, fold anchor comparison,
mirror convention and contours of the whole scalar theorem.
Reserve a small fixed horizontal neighborhood of its paired
favored saddles. Let \(I_N^{\rm loc}(Z)\) be precisely those fixed
local integrals, before allowing the saddle to move with \(Z\).
The exact difference
\[
                    \mathcal R_N(Z)=L_{N,n}(Z)-I_N^{\rm loc}(Z)
 \tag{41}
\]
is a polynomial in \(Z\) of degree at most \(D\).
The representatives and these fixed contours are independent of
the output color.

The complementary estimates can be kept uniform for
\(Z\in[-2,2]\):

* Each high Newton polynomial has polynomial real norm; Markov
  and the original full trace bound its whole high-sector source,
  including the odd middle and all traced normals.
* The positive-endpoint window has its actual two-channel estimate
  uniform on the real output interval, with rate \(h_0(2\epsilon)\to0\).
* The shortened slit-kernel theorem bounds
  \(\sup_{Z\in[-2,2]}|K_N^<(C,Z)|\) by
  \(e^{N(\Re\Psi(C)+\epsilon)}\). Thus the compact interfaces,
  seams, outer sides, opposite halves and horizontal remainders
  retain the same strict gaps, with a smaller fixed tolerance.
* On the fold contours the corresponding half-plane estimate has
  polynomial prefactor and no tolerance, uniformly for real \(Z\).
  The actual mirror-counted join, including its anchor conversion,
  is unchanged. Choose its fixed width so
  \(\mathcal I_2+CT^4<\mathcal I_n\).

Consequently, for some fixed \(\delta>0\),
\[
 \sup_{Z\in[-2,2]}|\mathcal R_N(Z)|
                \le CN^p e^{N(\mathcal I_n-\delta)}.
 \tag{42}
\]
This retains the full original source before taking an upper bound.
In particular the outgoing high sector is not continued as though
it had the low geometric phase.

For a polynomial \(P\) of degree at most \(D\), cosine
orthogonality bounds each Chebyshev coefficient by
\(2\|P\|_{[-2,2]}\). On the filled ellipse of parameter \(\rho>1\),
\[
 |P(Z)|\le2(D+1)\rho^D\|P\|_{[-2,2]}.
 \tag{43}
\]
Choose \(\log\rho<\delta/4\), then a sufficiently small fixed
ordinary-color disk about \(-2\) inside that ellipse.
Equations (42)--(43) preserve a strict gap on this disk.
Also shrink it so
\(|\Re W_n(u)-\mathcal I_n|<\delta/4\).
Thus the whole complement in (41) is exponentially smaller than
\(e^{N\Re W_n(u)}\), uniformly on the output disk.
This step uses a real-interval polynomial bound, not a derivative
estimate at its endpoint.

## 5. The moving local integral and its actual multiplier

The exact two reflected local contributions have the single
positive-only prefactor of the scalar theorem:
\[
 \frac{\sigma iN^2}{\pi}\mathfrak c_{N,n}
 \int_{\Gamma}
 \sin t\,K_N^<(-2\cos t,-2\cos u)\,\mathcal H_N(t)
 \frac{e^{inNt^2/(4\pi)-i\sigma Nt}}
      {(1-\eta e^{-i\sigma Nt})^2}\,dt.
 \tag{44}
\]
Here \(\mathcal H_N(t)\) is the product of the actual designated-half
representatives and \(\Gamma\) is the fixed local horizontal segment.
The reflected integrals add: the sine and \(dx\) each reverse sign,
while the two mirror half-prefactors sum to the displayed one.
All rational sampling aliases remain in (44).

On a smaller output disk deform the middle of \(\Gamma\) through
\(t_n(u)\). A local horizontal coordinate there has a uniformly
negative real quadratic part. Connect it to the old endpoints
inside the reserved neighborhood; those connectors retain a
strict gap from the original local endpoint gap.
Insert (40) into (44). Its ordinary amplitude \(a_e(t,u)\sin t\)
is holomorphic and nonzero near the moving saddle. The actual
microscopic insertion satisfies uniformly there
\[
 |\mathcal H_N(t_n(u))|\ge cN^{-r},\qquad
 |\partial_t^k\mathcal H_N(t)|
                    \le C_k[(1+\log N)/N]^r
 \tag{45}
\]
for bounded real parameters. Indeed the moving point
\((\pi-h-t_n(u))/(2\pi)\) stays in the same designated nonreal
compact as at \(u=0\); its \(\Im\Log\sin(\pi x)\) remains
bounded away from zero. The actual nonreal insertion theorem is
uniform on this compact. No endpoint-parameter continuation of
a lower bound is used.

The rational factor after removing its selected character is
\(1+O(e^{-cN})\), with fixed derivatives costing powers of \(N\).
Divide the insertion by its value at the moving saddle. Its
variation is \(O((1+\log N)^r|t-t_n(u)|)\).
Gaussian integration therefore gives a relative
\(O((1+\log N)^{r+1}/\sqrt N)\) error, uniformly on the output
disk. The wire relative error in (40) is \(O(N^{-1})\);
the nonquadratic terminal phase gives \(O(N^{-1/2})\).
The powers from (44), (40) and the terminal Gaussian are
\(N^2N^{-3/2}N^{-1/2}=1\), yielding exactly (11)--(12).
The complementary bound (42)--(43) is exponentially small even
after division by the polynomial lower bound in (45).

For complex microscopic parameters, the same finite atlas and
designated-half construction give polynomial amplitudes on these
contours. Absolute Gaussian bounds and the preserved complement
gap prove (14); no division by a possibly vanishing insertion is
used. Buffered Cauchy estimates prove the stated normalized
derivative upper bounds.

The functions in (6)--(7) are even in \(u\), and the unique
implicit solution in (9) is even. The actual local representative
depends on \(u\) only through \(t_n(u)\). Thus all displayed factors
and the relative error descend through
\(-2\cos u=-2+u^2+O(u^4)\).
Their nonvanishing on a fixed output disk follows from (7),(45)
and the relative error tending to zero, rather than from their
values at the center.
Finally \(\psi_u(t,0)=0\) and
\(\psi_{uu}(t,0)=-\cos(t/2)/(2\pi)\); stationarity proves (15).

For (14b), each inserted factor is bounded below by \(c/N\) and
has all fixed output derivatives bounded by \(C_k(1+\log N)/N\)
on smaller disks. Thus every quotient of such a derivative by the
factor is \(O(1+\log N)\). The elementary formula for the \(k\)-th
derivative of a logarithm is a polynomial of degree at most \(k\)
in these quotients. Sum it over the fixed number of factors and
include the bounded logarithmic derivatives of \(A_n\).

## 6. The whole real angular envelope and its strip

The enlarged wire construction also retains the original free-boundary
factorial estimate. On every compact part of its retained wire
contours and connectors, with \(0<\Re y<1/2\),
\[
 |\mathcal E_N(y,u)|\le \frac CN
   \exp N\{\Re b(y,0)-c_0(1-\cos u)\},
                       \qquad -\pi\le u\le\pi.
 \tag{46}
\]
This is the uniform midpoint-factorial boundary inequality, including
all reciprocal-factorial terms. Its positive constant is uniform on
the finitely many chosen contours and their small parameter
neighborhoods. Applying it to every term of the exact wire contour
retains its old phase bound, with the displayed angular loss.

For the omitted original indices, \(2j<N\), the exact positive
Fourier expansion of the low Newton polynomials gives
\[
                 |e_j(-2\cos u)|\le e_j(-2)
                         \quad(u\in\mathbb R).
 \tag{47}
\]
Thus their strict endpoint gap at \(u=0\) remains valid throughout
the real period. Since \(1-\cos u\le2\), reduce \(c_0\) if necessary
to absorb this gap. The same finite contour proof used in (40),
without taking a relative expansion away from the origin, yields
\[
 |K_N^<(-2\cos t,-2\cos u)|
 \le CN^p e^{N\{\Re\psi(t,0)-c_1(1-\cos u)\}}
 \tag{48}
\]
for real \(u\) in its whole period and \(t\) near the selected saddle.
Small complex changes of \(t\) use the locally deformed wire contour;
all nonlocal gaps and the uniform constant in (46) persist.

Use (48) on the fixed local terminal segment in (44).
The insertion is polynomially bounded there for bounded complex
parameters, and the actual signed terminal phase has maximum
\(\mathcal I_n\). Its rational sampling kernel is unchanged.
Together with (42), and another reduction of \(c_1\), this proves
\[
 |L_{N,n}(-2\cos u;\boldsymbol\alpha)|
 \le CN^p e^{N\{\mathcal I_n-c_2(1-\cos u)\}}
                          \quad(-\pi\le u\le\pi).
 \tag{49}
\]
All high-sector, fold, window, and seam contributions are included
through (42). An off-grid upper bound on the full high kernel has
not been substituted into this argument.

Near \(u=0\), (14)--(15) and even holomorphy give
\[
 \Re W_n(u+iv)\le
                \mathcal I_n-\kappa u^2+B_0v^2
 \tag{50}
\]
on a fixed small rectangle. Young's inequality absorbs the mixed
term from the complex quadratic coefficient. This proves (14a)
there.
For the complementary real angles use the exact Laurent degree
at most \(D\) in \(e^{iz}\). Applying the disk Poisson bound to
\(e^{iDz}L_{N,n}(-2\cos z)\), and the reciprocal polynomial for
the other half-plane, gives from (49)
\[
 \log|e^{-N\mathcal I_n}L_{N,n}(-2\cos(u+iv))|
 \le\log(CN^p)+D|v|
              -c_2N(1-e^{-|v|}\cos u)
\]
\[
 \hspace{35mm}\le\log(CN^p)+
       N\{-c_2(1-\cos u)+(1+c_2)|v|\}.
 \tag{51}
\]
Outside a smaller neighborhood of \(u=0\), the angular loss has
a positive lower bound. Choosing a sufficiently small fixed strip
absorbs the last term into half that loss. Combining with (50)
proves (14a). The argument is valid in the presence of zeros.

Cauchy's formula on larger microscopic parameter sets retains
their derivatives. Angular circles of radius \(O(N^{-1})\), or
ordinary color circles of radius \(O(N^{-2})\), change the exponent
in (14a) by \(O(1)\) uniformly on a smaller strip. The latter statement
includes both quadratic angular branch points. The actual output is
an ordinary color polynomial, so the color circles introduce no
choice of branch. This proves the asserted ordinary-normal upper
bounds with polynomial costs.

## 7. Coverage and limitations

The prior free-boundary kernel theorem already proves (40), and
more, on its stated smaller ray domain. The new ray inequalities
(24)--(32) enlarge the source-valid region to every selected
terminal saddle of magnitude at least three. Only the shortened
kernel is required here; the full off-grid high sector keeps its
original trace placement.

The bare case \(r=0\) already has a fixed output disk in the
uniform terminal-family theorem. The present extension concerns
arbitrary fixed microscopic products at the traced vertex.
It supplies a relative nonzero boundary coefficient for real
microscopic parameters and a polynomial normalized bound for complex
ones, together with the whole-period upper envelope (14a).
It does not give uniformity in growing powers, a power-two theorem,
or closure under receiving an already exponentially large transformed
factor. Its level-dependent amplitude must be retained in any
subsequent composition.

The geometric phase in (10) is the old bare terminal phase.
Its nondegenerate moving saddle and curvature are controlled, but
the positive-angle realization of the additional microscopic
boundary incidences is a separate geometric question.

## 8. Complete direct sources

The following complete source texts were read at their matching pins;
their directly used finite normalization, contour, and source-budget
implications were checked:

* [Actual free-boundary wire packet](research_pair_free_boundary_kernel.md),
  SHA256 e62ae0c2701388a7e9bf3ad171d7005b845098542e48dffb1a36c4bc95ee745f.
* [All-power stationary geometry](research_terminal_powers_three_and_above.md),
  SHA256 393618c7de5f9a2d8f0c816b568abf97f63419cd834cf7b56eccbb300fd608cd.
* [Uniform midpoint factorial bounds](research_uniform_factorial_and_boundary_decay.md),
  SHA256 4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
* [Whole scalar microscopic leaf](research_microscopic_endpoint_filled_leaf_scalar_asymptotic.md),
  SHA256 33ef2e3ee2090fa69c58df03bc141f6249dcaa35b0ae62598213a88ce65979d0.
* [Compact interfaces and seams](research_sharp_endpoint_compact_interface_and_seams.md),
  SHA256 178e49b99b51fe767bc29ceadafb00159c179cd42f9ba5469921f64a6eabdde9.
* [Uniform fold cap](research_endpoint_uniform_fold_cap.md),
  SHA256 5cdb59337b9e9cccac8bc94fb250106ed6cfc63db7f023ba564e715d8d2900eb.
* [Incoming-color kernel upper bounds](research_mixed_next_incoming_color_kernel_upper_bounds.md),
  SHA256 9ffa400456a8439d55352156707fab0aacfb8f1f8b0f622fd66824c9f1e553db.
* [Actual positive-endpoint window](research_unturned_endpoint_complex_baseline_and_window.md),
  SHA256 9d233d9bb11c2842e62d5523f97e9621a3bd22532e3b527ceaab8125782c1cc1.
* [Actual nonreal insertion](research_endpoint_nonreal_insertion_lower_bound.md),
  SHA256 ab3b4687b53c2168d22342c0e822b243a563f716d2a7a0de18d87c372546d7d0.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Adopted notes and public manuscripts are unchanged.
