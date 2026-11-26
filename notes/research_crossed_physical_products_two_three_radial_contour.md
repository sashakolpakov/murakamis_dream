# Crossed physical products at powers two and three

Private written proof, 17 November 2026.

The original radial contour extends to signed powers of magnitude
two and three under the strict macroscopic support condition.
The radial phase need not be convex at every height. An explicit
barrier nevertheless places its unique minimum in the convex
region and keeps the selected spectral point in \(\Re C<2\).
At power two the radial graph ends at the original angular
endpoint; the complete endpoint caps are estimated separately.

The resulting theorem concerns the complete original scalar,
all its mixed first boundary normals, and a local common scalar
packet. It does not assert closure under another trace or turn.

## 1. Actual source and conclusions

Use
\[
 N\ge3,\quad D=N-1,\quad J=\lfloor D/2\rfloor,\quad
 q=e^{\pi i/N},\quad \eta=(-1)^D,\quad
 c_j=2\cos((2j+1)\pi/N),
\]
\[
 P_N(C)=2T_N(C/2)+2,\qquad
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f,
 \quad F_j(C)=K_N(c_j,C),\quad
 G_j(C)=\left.\partial_wK_N(w,C)\right|_{w=c_j}.
 \tag{1}
\]
Only double physical nodes have a prescribed \(G_j\); the odd
simple node has its one value. Fix \(m\ge3\), \(\varepsilon>0\),
and \(p\in\{2,3\}\). The indices satisfy
\[
       0\le j_i\le J,\qquad
       \sum_i j_i-D\ge\varepsilon N .
 \tag{2}
\]
For a subset \(I\) of the double-node positions put
\[
 Z_{p,N,I}(\mathbf j)=
 \phi_N\left(R^p\prod_{i\in I}G_{j_i}
                         \prod_{i\notin I}F_{j_i}\right),
 \qquad Z_{p,N}=Z_{p,N,\varnothing}.
 \tag{3}
\]
The product is ordinary before the original canonical closing.
In particular all closing normals are retained.

On the original slit branches define
\[
 \Psi_x(C)=2\int_0^x
  \operatorname{arsinh}
       \left(\tfrac12\sqrt{2-C}\cot(\pi u)\right)\,du,
 \qquad 0\le x\le\tfrac12,
\]
\[
 S_{\mathbf x}(t)=\sum_i\Psi_{x_i}(-2\cos t),\qquad
 \Phi_{p,\mathbf x}(t)=S_{\mathbf x}(t)
                              +\frac{ipt^2}{4\pi}-it .
 \tag{4}
\]
The branches are positive on \(C<2\), and their angular lift
is the original one on \(|\Re t|<\pi\).

**Theorem 1.** Uniformly in (2), the contour constructed below
selects a unique critical point
\[
 t_p(\mathbf x)=s_p-ih_p,\qquad
 0<s_p<2\pi/p,\quad h_p>0,\qquad \mathbf x=\mathbf j/N.
 \tag{5}
\]
Its depth and its distances from both ends in (5) are bounded
below, its height is bounded above, and
\[
 M_p(\mathbf x)=\Re\Phi_{p,\mathbf x}(t_p)>0,\qquad
 -\Re\Phi_{p,\mathbf x}''(t_p)>0
 \tag{6}
\]
have uniform positive lower bounds. The spectral saddle family
lies in a fixed compact subset of \(\Re C<2\).

Let \(\mathscr L_{j,N}=\log F_j\) have its actual normalization
real on \(C<c_0\), and put near the selected saddle
\[
 \Phi_{p,N}(t)=N^{-1}\sum_i\mathscr L_{j_i,N}(-2\cos t)
                              +\frac{ipt^2}{4\pi}-it.
 \tag{7}
\]
It has a unique nearby critical point
\(t_{p,N}=t_p(\mathbf j/N)+O(\log N/N)\). With the square root
having positive real part,
\[
 \boxed{
 Z_{p,N}=
 \frac{iN^{3/2}}{\pi}\,q^{pD^2/4}\sin(t_{p,N})
 \sqrt{\frac{2\pi}{-\Phi_{p,N}''(t_{p,N})}}\,
 e^{N\Phi_{p,N}(t_{p,N})}\bigl(1+O(N^{-1})\bigr).
 }
 \tag{8}
\]
In particular the coefficient is nonzero and
\[
                    \log|Z_{p,N}|=NM_p+O(\log N).
 \tag{9}
\]
All constants may depend on the fixed \(m,\varepsilon,p\).
The theorem includes zero and last value rows and both parities.
Negative powers \(-2,-3\) follow by exact conjugacy.

**Theorem 2.** All conclusions of the full-normal packet source
extend to the range (2), \(p=2,3\). Explicitly,
\[
             |Z_{p,N,I}|\le C N^B e^{NM_p}
                              \le C N^{B'}|Z_{p,N}|.
 \tag{10}
\]
If each selected \(j_i/N\), \(i\in I\), stays in a fixed compact
subinterval of \((0,1/2)\), then, with \(C_{p,N}=-2\cos t_{p,N}\),
\[
 \frac{Z_{p,N,I}}{Z_{p,N}}
   =N^{|I|}
      \left[\prod_{i\in I}g(j_i/N,C_{p,N})
                                      +O(\log N/N)\right],
\]
\[
 g(x,C)=-
 \frac{2\operatorname{arsinh}
       \bigl(\tfrac12\sqrt{2-C}\cot(\pi x)\bigr)}
                         {4\pi\sin(2\pi x)} .
 \tag{11}
\]
Every displayed \(g\) is a uniform unit. Unselected value
indices can still approach zero or the fold.

On every compact
\(\mathcal B\Subset\{\mathbf x\in(0,1/2)^m:\sum_i x_i>1\}\)
there is a finite cover by real product neighborhoods with
thin fixed complex neighborhoods and holomorphic scalars
\(\mathcal W_{p,N}\) such that, for every mixed first external
spectral derivative,
\[
 \left|
 \left[\prod_{i\in I} C_N'(x_i)^{-1}\partial_{x_i}\right]
      \mathcal W_{p,N}(\mathbf x)\Big|_{\mathbf x=\mathbf j/N}
                         -Z_{p,N,I}(\mathbf j)\right|
       \le C N^B e^{-\gamma N}|Z_{p,N}(\mathbf j)|,
 \quad C_N(x)=2\cos(2\pi x+\pi/N).
 \tag{12}
\]
The physical error is the complement of one fixed saddle arc.
No off-grid comparison with the canonical multivariate source
or subsequent closing estimate is asserted. For negative
powers conjugate (11) and the holomorphic packet.

## 2. Exact radial sign and a finite barrier

All sufficiently large levels in (2) belong to
\[
 \mathcal X=\{\mathbf x\in[0,1/2]^m:
                            \sum_i x_i\ge1+\varepsilon/2\}.
 \tag{13}
\]
An empty compact gives a vacuous assertion. Put
\[
 k_i=\sin(\pi x_i),\quad a=2\pi/p,\quad
 A(s,h)=\Re S_{\mathbf x}(s-ih)+psh/(2\pi)-h.
 \tag{14}
\]
The source derivative identity, including its normalization, is
\[
 S_{\mathbf x}'(t)=-\pi^{-1}\sum_i r_{k_i}(t),\qquad
 r_k(t)=\operatorname{arsinh}(k\tan(t/2)).
 \tag{15}
\]
Writing \(\beta_k(s,h)=-\Im r_k(s-ih)\), we have
\[
 A_h=\pi^{-1}\sum_i\beta_{k_i}+ps/(2\pi)-1,\qquad
 A_s=-\pi^{-1}\sum_i\Re r_{k_i}+ph/(2\pi).
 \tag{16}
\]

For \(0<s<\pi\), \(h>0\), and \(0<k\le1\), the exact sign is
\[
 \boxed{\quad
 \operatorname{sgn}\Re r_k'(s-ih)
   =\operatorname{sgn}
          [\,1+(1-k^2)\cos s\cosh h\,].
 \quad}
 \tag{17}
\]
To verify it on the actual branch, put \(z=\cos(s-ih)\) and
\[
 U=(1+z)/2,\qquad
 V=(1+k^2+(1-k^2)z)/2.
\]
For \(k<1\), both lie in the upper half-plane. For \(k=1\),
\(V=1\). The original derivative is
\[
 r_k'(t)=\frac{k}{2\sqrt U\sqrt V},
 \qquad
 \Im(UV)=\frac{\Im z}{2}
                    [1+(1-k^2)\cos s\cosh h].
 \tag{18}
\]
The sum of the two arguments lies in \((0,2\pi)\).
The sign of the cosine of half that sum is the sign
of its sine, proving (17), including its zero case.
Here \(\sqrt U=\cos(t/2)\) is the original square root.
The zero row has \(r_0=0\).

Consequently, for \(s\le\pi/2\) each nonzero \(\beta_k\)
increases strictly with \(h\). For \(s>\pi/2\) and \(k<1\),
it has exactly one maximum, at
\[
             \cosh H_k=[(1-k^2)(-\cos s)]^{-1},
 \tag{19}
\]
then decreases to \(\arcsin k\). For \(k=1\) it increases
to \(\pi/2\). All limiting inverse-sine values refer to
the branch approached from \(\Re\tan(t/2)>0\).

For \(\pi/2<s<\pi\), let
\[
 \delta=\pi-s,\qquad h_B(s)=-\log(-\cos s).
 \tag{20}
\]
At this height,
\[
 \tan((s-ih_B)/2)=A_0-i,\qquad A_0=2\cot\delta.
 \tag{21}
\]
For \(0\le h\le h_B\), the bracket in (17) satisfies
\[
 1+(1-k^2)\cos s\cosh h
 \ge1-\frac{(1-k^2)(1+\cos^2s)}2
 \ge\frac{\sin^2s}{2}>0.
 \tag{22}
\]
In particular all nonzero \(\beta_k\) increase strictly
up to this barrier.

We need its quantitative angle bound
\[
                         \beta_k(s,h_B)\ge k\delta/2.
 \tag{23}
\]
Write \(r_k(s-ih_B)=\rho-i\beta\).
For \(k>0\), \(A_0>0\), one has \(\rho>0\) and
\(0<\beta<\pi/2\). From \(\sinh(\rho-i\beta)=k(A_0-i)\),
\[
 \tanh\rho=A_0\tan\beta,\qquad
 k=\frac{\sin\beta}{\sqrt{1-A_0^2\tan^2\beta}}
                                      =:f_{A_0}(\beta).
 \tag{24}
\]
This last function increases strictly on
\(0\le\beta<\arctan(1/A_0)\).
Set \(v=\tan(\delta/2)\in(0,1)\) and \(\beta_0=k\delta/2\).
The elementary bounds
\(\sin(k\delta/2)\le kv\) and
\(\tan(k\delta/2)\le kv\le v\) give
\[
 \frac{\sin^2\beta_0}{k^2}+A_0^2\tan^2\beta_0
 \le v^2(1+A_0^2)=1-v^2+v^4<1.
 \tag{25}
\]
This proves both that \(\beta_0\) is in the domain of
\(f_{A_0}\) and that \(f_{A_0}(\beta_0)<k\).
Equations (24)--(25) imply (23); the case \(k=0\) is
immediate.

Since \(\sin(\pi x)\ge2x\) on \([0,1/2]\), (13) implies
\[
 \sum_i\beta_{k_i}(s,h_B)
 \ge\frac{\delta}{2}\sum_i k_i
 \ge\delta\sum_i x_i>\delta
 \ge \pi-ps/2,\qquad p\ge2 .
 \tag{26}
\]
The last inequality is used only when \(s\le a\), so
its right side is nonnegative.

There is no later crossing hidden above the barrier.
At (21), \(k=\cosh\rho\sin\beta\) implies
\(\beta_k(h_B)<\arcsin k\) for \(k>0\).
Its maximum, when finite, occurs after \(h_B\) by (22).
Equation (19) and the limiting value therefore give
\[
          \beta_k(s,h)\ge\beta_k(s,h_B)\quad(h\ge h_B).
 \tag{27}
\]
Thus (26) remains a strict inequality at all larger heights.

## 3. Unique radial branch, including the power-two endpoint

The radial equation is
\[
                  \sum_i\beta_{k_i}(s,h)=\pi-ps/2.
 \tag{28}
\]
For \(0\le s\le\pi/2\) the strict convexity argument in
the radial source applies. Its endpoint values are
\[
 A_h(s,0)=ps/(2\pi)-1,\qquad
 A_h(s,\infty)=\sum_i x_i+ps/(2\pi)-1>0.
 \tag{29}
\]
For \(\pi/2<s<a\), (22), (26), and (27) instead prove
that (28) has exactly one root, and it satisfies
\[
                    0<h(s)<h_B(s),\qquad A_{hh}>0.
 \tag{30}
\]
For \(p=3\), \(h(a)=0\); for \(p=2\), the branch is
initially defined on \([0,\pi)\).

The limits in (29) are uniform in \(s\in[0,\pi]\) and
\(\mathbf x\in\mathcal X\). Indeed
\(\tan((s-ih)/2)\to-i\) uniformly, and the original
\(\operatorname{arsinh}\) is uniformly continuous from
the right side at the compact segment \(-i[0,1]\),
including its endpoint. Hence all the roots have a
uniform finite upper height \(H\).
At \(s=0\) their heights also have a positive lower
bound. Finite-height strictness and the implicit
function theorem give continuous parameter dependence,
smoothness in \(s\), and positive local \(A_{hh}\)
throughout the branch.

Put \(b(s)=A(s,h(s))\). Harmonicity and differentiation
of \(A_h=0\) give
\[
           b''(s)=-A_{hh}-A_{sh}^2/A_{hh}<0,\qquad
           b'(0)=ph(0)/(2\pi)>0.
 \tag{31}
\]
For \(p=3\),
\[
 b'(a)=-\pi^{-1}\sum_i
                 \operatorname{arsinh}(k_i\tan(a/2))<0.
 \tag{32}
\]
All these inequalities have the needed compact uniform
buffers at the selected maximum.

For \(p=2\) a separate endpoint argument is required.
By (20),(30),
\[
 0<h(s)<-\log(-\cos s)\longrightarrow0
                         \quad(s\to\pi),
 \tag{33}
\]
uniformly in \(\mathbf x\).
Thus \(C=-2\cos(s-ih(s))\to2\).
The integral (4), bounded near its lower endpoint by
\(C(1+|\log u|)\), is continuous up to \(C=2\) on
these slit-side approaches, uniformly in \(x\in[0,1/2]\).
It follows that
\[
                     b(\pi):=\lim_{s\to\pi}b(s)=0
 \tag{34}
\]
uniformly on \(\mathcal X\).

On the other hand the source inequality
\[
 \Psi_x(-2\cosh h)\ge
 xh+2x\log(1+e^{-h})
                     +2\int_0^x\log\cot(\pi u)\,du
 \tag{35}
\]
has a nonnegative last integral. The uniform upper
bound \(h(0)\le H\) and \(\sum_i x_i>1\) therefore
give \(b(0)\ge c>0\), uniformly.
Choose \(a_0<\pi\) close enough to \(\pi\) that
\(\sup_{\mathcal X}b(a_0)<c/2\).
Strict concavity yields
\[
             b'(a_0)\le[b(a_0)-b(0)]/a_0\le-c/(2a_0).
 \tag{36}
\]
Together with the uniform positive derivative at zero,
this proves that the unique maximum stays in a fixed
compact subinterval of \((0,\pi)\).
It avoids any assumption about a limiting derivative
at the angular endpoint.

For both powers the selected \(h_p\) is positive and
continuous on the compact \(\mathcal X\), so it has a
positive minimum. The finite-height strictness in
(22),(29) then gives a positive lower bound for
\(A_{hh}\) at the saddle. The maximum satisfies
\(M_p>b(0)\ge c\). This proves (5)--(6).

The favorable spectral half-plane is also preserved.
For \(s\le\pi/2\), \(\Re(-2\cos(s-ih))\le0\).
For \(s>\pi/2\), put \(r=-\cos s\in(0,1)\).
Equation (30) gives
\[
 r\cosh h<r\cosh h_B=(1+r^2)/2<1,
 \quad\text{hence}\quad \Re(-2\cos(s-ih))<2.
 \tag{37}
\]
Compactness gives a fixed half-plane buffer at the
selected saddle family.

For completeness the original positive-edge check
also survives. Write \(\tan((s-ih)/2)=A_0-iB_0\).
The branch has \(B_0<1\): this is automatic below
\(\pi/2\), and equivalent to \(h<h_B\) above it.
For a strict outside angle
\(\alpha_i=\pi-2\pi x_i<\pi\), put
\(b_i=\tan(\alpha_i/2)\).
The original edge square root satisfies
\[
 \Re[1+(A_0-iB_0)^2+b_i^2]
                       =A_0^2+b_i^2+1-B_0^2>A_0^2+b_i^2.
 \tag{38}
\]
It follows that its real part exceeds
\(\sqrt{A_0^2+b_i^2}\), exactly the positive-edge
criterion used in the radial source.
Zero rows are exact value factors one, not strict
positive incidences. No volume identification follows.

## 4. The complete original contour and its endpoints

The original full-grid identity is
\[
 Z_{p,N}=-\frac{N^2q^{pD^2/4}}{\pi i}
  \int_\Gamma \sin t\,\prod_iF_{j_i}(-2\cos t)
           e^{ipNt^2/(4\pi)}W_N(t)\,dt,
 \qquad W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{39}
\]
Here \(\Gamma\) is a lower arc from \(-\pi\) to \(\pi\).
This retains the odd simple value, all closing first
normals, the reflected-lens multiplicity, and every
alias. The original source has not been replaced by
an isolated spectral-circle Gaussian.

Reflect \(h(-s)=h(s)\) on \([-a,a]\).
The action on the negative half is
\[
 \Re\Phi_{p,\mathbf x}(-s-ih(s))
                         =b(s)-psh(s)/\pi .
 \tag{40}
\]
Its maximum is strictly below \(M_p\): equality with
the maximum of \(b\) would require \(s=s_p\), where
the subtracted term is positive.
The same argument includes the power-two endpoint
using (34). Compactness gives a uniform strict gap.
On the positive graph, strict concavity gives a
uniform gap outside a fixed saddle neighborhood.

For \(p=3\), the remaining real intervals
\(a\le|s|\le\pi\) have action \(S_{\mathbf x}(s)\).
By (15) this decreases with \(|s|\), and it is at
most \(S_{\mathbf x}(a)=b(a)<M_p\).
For \(p=2\) there are no such outer intervals: the
radial graph itself ends at \(\pm\pi\).

Choose a small fixed \(v>0\). Replace \(h(s)\) by
\(\max(h(s),v)\), and, for \(p=3\), give the outer
intervals depth \(v\). The selected saddle is unchanged.
Away from the endpoints, uniform continuity preserves
all strict complement gaps if \(v\) is small enough.
In power two, (33) ensures that the modifications near
the real ends can be confined to a uniformly small
endpoint neighborhood. For power three, the changes
near \(s=\pm a\) lie in compact strict-gap regions;
the endpoint parts of the outer intervals are handled
below. The limiting real action is uniformly continuous
also as the original power-two endpoints are approached,
by the dominated integral used in (34).

We spell out the actual endpoint estimate rather than
use a slit-compact bound at \(C=2\).
The source Jacobi roots are real and exceed \(c_0\).
Their product gives, for fixed small \(d>0\) and large
\(N\), uniformly on \(|C-2|\le d\),
\[
 |F_j(C)|\le F_j(2-3d),\qquad
 \prod_iF_{j_i}(2-3d)
       \le N^B e^{Nm\Psi_{1/2}(2-3d)},\qquad
             \Psi_{1/2}(2-3d)\to0.
 \tag{41}
\]
Choose \(d\), then \(v\), small enough to preserve
the preceding strict gaps. Shrink the endpoint
neighborhood so that it maps into this disk and,
in power two, \(h_B(s)<v\) there. The modified
contour consequently has constant depth \(v\) on
these endpoint parts, so the Gaussian costs at most
\(e^{Npv/2}\) there. Append the two original
vertical segments to obtain the endpoints of (39).
On them the exact denominator is
\[
 |W_N(\pm\pi-iy)|
       =\frac{e^{-Ny}}{(1+e^{-Ny})^2}\le e^{-Ny},
                     \qquad 0\le y\le v.
 \tag{42}
\]
Since \(\inf M_p>0\), first choose \(d\) and then
\(v\) small enough that (41)--(42) pay every endpoint
portion with a fixed strict gap. This includes the
new power-two limiting endpoint. No endpoint residue
or additional physical term is omitted.
The modified contour has uniformly bounded length:
its nonconstant part is a compact implicit graph
where \(A_{hh}\) has a positive lower bound, and
its endpoint parts are the fixed-depth intervals
and the two bounded vertical connectors.

All other contour portions are compact in the
canonical slit. The all-row logarithmic profile
there turns the limiting gaps into actual source
gaps. On every graph portion of depth at least \(v\),
\[
                   W_N(t)=e^{-iNt}(1+O(e^{-Nv})).
 \tag{43}
\]
At the endpoints it remains in its exact form (42).
Thus the complete contribution outside the saddle
neighborhood is \(O(N^B e^{N(M_p-\gamma)})\) for
some fixed \(\gamma>0\).

On the buffered half-plane neighborhood from (37),
the actual logarithm satisfies
\(\Phi_{p,N}-\Phi_{p,\mathbf j/N}=O(\log N/N)\)
with every fixed derivative. Its nearby saddle and
uniform analytic Morse coordinate therefore exist.
The oriented Gaussian calculation of the radial
source applies verbatim, since it requires
\(-\Re\Phi''>0\), not \(s_p\le\pi/2\).
More explicitly, if
\(a_N=-\Re\Phi_{p,N}''>0\) and
\(b_N=\Im\Phi_{p,N}''\), the radial tangent is
\(1+ib_N/a_N\) and its product with \(\Phi_{p,N}''\)
is the negative real number
\(-(a_N^2+b_N^2)/a_N\).
This fixes the positive-real-part square root in (8).
The literal local amplitude is \(\sin t\), uniformly
nonzero at the saddle. Its Gaussian integral has
relative error \(O(N^{-1})\), by the analytic Morse
expansion and cancellation of the first odd term.
Multiplication by the original factor in (39) proves
(8); the complete complement and (43) are
exponentially smaller. This proves Theorem 1.

## 5. Full normals and the common scalar on the new branch

The full-normal source supplies the even holomorphic
Ward--Jacobi representative \(\widehat G_j\) of each
actual \(G_j\) inside the original trace. Its exact
inner physical values and required first normals
are preserved, so every product rule with \(R^p\)
and other rows is retained. Its complete lens is
(39) with the corresponding factors replaced by
\(\widehat G_j\).
This extension uses the even angular function and
a fixed-level endpoint limit; it does not presume
spectral holomorphy across \(C=2\) or periodicity.

On compact slit charts,
\(|\widehat G_j|\le C N^B|F_j|\), uniformly in every
double row. At the endpoint caps the determinant
cofactor argument instead gives
\[
            |\widehat G_j(C)|\le C_d N^B F_j(2-3d).
 \tag{44}
\]
This includes \(j=0\) through its Ward representative,
and the even last normal. It never divides by a
vanishing Jacobi determinant on the cap.
Equations (41)--(44) pay every mixed-normal complement
on the very same contour, with the same fixed
exponential gaps and only polynomial losses.
The local slit bound proves the first inequality
in (10); (8)--(9) give the relative inequality.

For a selected bulk row, the actual normal connection
on the favorable half-plane gives, with all fixed
spectral derivatives,
\[
             \frac{\widehat G_j(C)}{N F_j(C)}
                    =g(j/N,C)+O(\log N/N).
 \tag{45}
\]
On \(\Re C<2\) the original square root
\(\sqrt{2-C}\) has positive real part.
For bulk \(x\), its product with \(\cot(\pi x)>0\)
lies in the right half-plane, where the principal
inverse hyperbolic sine has positive real part.
Thus \(\Re g<0\), and compactness makes these factors
uniform units. Applying the same actual Gaussian
with amplitude
\(\sin t\prod_{i\in I}\widehat G_{j_i}/(N F_{j_i})\)
proves (11). All complements have already been paid.

Finally fix a strict bulk reference tuple and one
short saddle arc \(\gamma_0\) of its complete lens,
with spectral image in \(\Re C<2\).
Every complementary gap persists for nearby real
tuples by uniform continuity, including the global
endpoint bounds (41),(44).
The exact corrected scalar row from the full-normal
source satisfies, as identities along that arc,
\[
 \mathfrak F_N(j/N,C)=F_j(C),\qquad
 \partial_x\mathfrak F_N(j/N,C)
                          =C_N'(j/N)\widehat G_j(C).
 \tag{46}
\]
It is holomorphic and has the required own-profile
size on a sufficiently thin fixed complex degree
neighborhood. Define
\[
 \mathcal W_{p,N}(\mathbf x)=
 -\frac{N^2q^{pD^2/4}}{\pi i}
 \int_{\gamma_0}\sin t\,e^{ipNt^2/(4\pi)}W_N(t)
                  \prod_i\mathfrak F_N(x_i,-2\cos t)\,dt.
 \tag{47}
\]
Every mixed physical external jet of the integrand
is exact by (46). Its difference from (3) is solely
the complete complementary-chain integral, now
exponentially small relative to (8). This proves
(12). The scalar connection rate determines the
allowed complex thickness only; it is not an
additional physical error exponent.

## 6. Scope, coverage, and complete direct sources

The original radial theorem left \(|p|<4\) open.
The archived degree-two short reductions concern
two physical inputs, and the terminal power and
uniform star results concern their specified
terminal packets. None supplies this arbitrary
fixed-\(m\) physical-product contour at \(p=2,3\).
The strict support condition (2) is essential to
the barrier proof given here. No assertion for
small total degree is imported from a different
power range.

At \(p=1\), the target in (28) tends to \(\pi/2\)
as \(s\to\pi\), whereas the barrier lower bound in
(26) tends to zero. This proof therefore does not
select a convex radial branch or pay the complete
contour in that regime. It makes no failure or
noncancellation claim there. Further turns,
external closings, and geometric volume
identifications also remain outside the theorem.

The complete direct texts were read at these pins;
all directly used implications were checked:

* [Original crossed radial contour](research_crossed_physical_products_radial_contour.md),
  SHA256 db63d7bf100a6d35647b6c9b4832d16c6f5520a7a9c38c0fd322f87659c9d50e:
  source action and logarithm, uniform row facts,
  exact normalization and finite-phase Gaussian.
* [Crossed full-normal scalar packet](research_crossed_physical_products_full_normal_packet.md),
  SHA256 84388316d1b6122e940832201b5a9b181d330bc6ea6094a22aafff9007076a53:
  even Ward--Jacobi full-lens substitution, all-row
  cofactor bounds, actual bulk normal connection,
  and exact corrected scalar row on a fixed arc.
* [Original full-grid lens](research_full_grid_lens_source_continuation.md),
  SHA256 d141e6e8c23572bb13484807a2359395a0371d6a3d699198826a105b6dad5649:
  original signed prefactor, reflected multiplicity,
  odd simple value, endpoints and complete alias kernel.

Only written mathematics, complete text reads, and
metadata hashes were used. No mathematical programs,
tests, numerical evaluations, or builds were run.
Frozen notes and public manuscripts are unchanged.
