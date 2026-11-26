# A geometric source block and a bounded current on the prism tube

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

This consolidated final supersedes the unadopted research note
`research_centered_tensor_full_radial_source_transport.md`, whose bytes
are retained unchanged. It makes the nonvanishing scope explicit.

The original centered tensor is an explicit nonzero geometric block
plus an absolutely bounded correction on the whole strict prism-angle
tube, with independent moduli up to the unit boundary on its three legs. Wherever
the geometric height is nonnegative this gives its nonzero leading
asymptotic. In particular it transports the initialized packet along
every strict positive-prism radial path, on compact families away from
the origin. The coefficient is determined by
the original finite source.

The proof uses a canonical Gamma interpolation of its exact wall
residues. A norm-corrected finite rectangle removes both outer pole
families before any estimate. Its moving Cauchy pole gives an explicit
nonzero geometric term. The remaining complete vertical current is
uniformly bounded after its stated normalization. No absolute gap
between the geometric action and an outer-facet action is assumed.

This is a theorem about one universal multiplication tensor. It does
not move the assembled Conway coefficient cycle or prove a knot volume
identity after arbitrary short fillings.

## 1. The source, the paths, and the result

Fix \(N\ge2\), and set
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\qquad
 D_N(t)=1-\eta t^N .
 \tag{1}
\]
All fractional powers of \(q\) use this exponential. Let
\(\mathcal C_N(x,y,z)\) be the entire initialized centered
three-boundary source, with its original Frobenius closing and full
Casimir first normals.

Write a strict prism shape as
\[
 a,b,c>0,\quad a+b,a+c,b+c<1,\quad S=a+b+c>1.
 \tag{2}
\]
Permute the three legs, if necessary, so that \(a\) is a largest
angle. Then
\[
                         0<b,c<1/2.
 \tag{3}
\]
The tensor is symmetric, so this does not change its value.
For independent \(0<r_x,r_y,r_z\le1\), put
\[
 x=-r_x e^{-2\pi ia},\qquad y=-r_y e^{-2\pi ib},\qquad
 z=-r_z e^{-2\pi ic},\qquad
 \ell_i=-\frac{\log r_i}{2\pi}\ge0 .
 \tag{4}
\]
Use the initialized action and amplitude
\[
 \begin{split}
 \Psi(x,y,z)={}&-\frac{\pi}{12}
 +\frac1{2\pi}\bigl[
 \operatorname{Li}_2(-x)+\operatorname{Li}_2(-y)
 +\operatorname{Li}_2(-z)+\operatorname{Li}_2(-xyz)\\
 &\hspace{33mm}
 -\operatorname{Li}_2(xy)-\operatorname{Li}_2(xz)
 -\operatorname{Li}_2(yz)\bigr],\\
 B(x,y,z)={}&[(1-xy)(1-xz)(1-yz)]^{-1/2}.
 \end{split}
 \tag{5}
\]
Their branches are fixed by power series at zero and their continuous
limits at the stated strict angular boundary.

**Theorem.** Let the shapes vary in a compact subset of (2), and
let all three moduli vary independently in
\([r_0,1]\), where \(r_0>0\). There is an explicit nonzero
canonical Gamma quotient \(\mathcal G_N\), defined in (24) below,
and an explicitly prescribed current \(\mathcal I_N\), such that
\[
 \boxed{\quad
 \mathcal C_N(x,y,z)=\mathcal G_N(x,y,z)
       -\frac{\kappa}{N}D_N(x)D_N(y)D_N(z)\mathcal I_N(x,y,z),
 \qquad |\mathcal I_N|\le C .
 \quad}
 \tag{6}
\]
The source identity is exact. The bound is uniform on these compact
families for all sufficiently large \(N\). Moreover
\[
 \mathcal G_N=
 \kappa e^{\,i\pi/4-\pi i/(2N)}
       B(x,y,z)e^{iN\Psi(x,y,z)}(1+O(N^{-1})).
 \tag{7}
\]
Consequently, on the portion of such a family where
\(-\operatorname{Im}\Psi\ge0\),
\[
 \boxed{\quad
 \mathcal C_N=
 \kappa e^{\,i\pi/4-\pi i/(2N)}
       B(x,y,z)e^{iN\Psi(x,y,z)}(1+O(N^{-1})).
 \quad}
 \tag{8}
\]
On that nonnegative-height portion, the original source is therefore
nonzero for all sufficiently large levels,
including both parities and composite levels. The common-radial
subfamily \(r_x=r_y=r_z\) always has strictly positive height,
by the prism radial theorem. Positivity is not asserted for arbitrary
independent moduli. The estimate includes all level-dependent approaches
to \(r_i=1\). In fact, if any \(D_N(t_i)=0\), then
\(\mathcal C_N=\mathcal G_N\) exactly. No assertion is made uniformly
as a modulus tends to zero or an angular shape meets a prism face.

## 2. The canonical interpolation and the exact wall sum

Use the original canonical factorial
\[
 G_N(w)=\left(\frac{2\pi}{N}\right)^w\Gamma(w+1)
 \prod_{m=1}^{\infty}
 \frac{\Gamma(Nm+w+1)}
      {\Gamma(Nm-w)(Nm)^{2w+1}},
 \qquad -1<\Re w<N ,
 \tag{9}
\]
with positive-base powers using their real logarithms. Define
\[
 F_N(w)=e^{\,\pi i w(w+1)/(2N)-\pi iw/2}G_N(w).
 \tag{10}
\]
Its normalization and shifts are fixed by this product, not by
a choice of a periodic solution:
\[
 \begin{gathered}
 F_N(0)=1,\qquad F_N(j)=(Q;Q)_j\quad(0\le j<N),\\
 F_N(w+1)=(1-Q^{w+1})F_N(w),\qquad
 F_N(w+N)=(1-e^{2\pi iw})F_N(w),\\
 F_N(w)F_N(d-w)=Nq^{w(w-d)} .
 \end{gathered}
 \tag{11}
\]
Here \((u;Q)_j=\prod_{h=0}^{j-1}(1-uQ^h)\), with empty product one.
The last two identities extend meromorphically. The first positive
zero block of \(F_N\) consists of simple zeros at the integers
\(N,\ldots,2N-1\). Its negative poles begin at \(-1\).
These statements follow either from (9) or from its normalized
shift and reflection.

Set
\[
 A=N(1-b)-\tfrac12+iN\ell_y,\qquad
 B_0=N(1-c)-\tfrac12+iN\ell_z,\qquad
 C=N(1-b-c)+iN(\ell_y+\ell_z) .
 \tag{12}
\]
The name \(B_0\) distinguishes this shift from the amplitude in
(5). Their exact balance and clock values are
\[
 A+B_0-C=d,\qquad
 Q^A=-q^{-1}y,\quad Q^{B_0}=-q^{-1}z,\quad Q^C=yz .
 \tag{13}
\]
Define the meromorphic weight
\[
 W_N(s)=
 \frac{F_N(s)F_N(s+C)F_N(A)F_N(B_0)}
      {F_N(C)F_N(s+1+A)F_N(s+1+B_0)}
 \tag{14}
\]
and the moving Cauchy factor
\[
                      K_N(s)=\frac1{1+q^{-1}Q^{-s}x}.
 \tag{15}
\]
The two \(+1\)'s in (14) are part of the original source.
Dropping them would remove two boundary factors.

The exact wall theorem proves
\[
 \mathcal C_N(-qQ^j,y,z)=
 \frac{\kappa}{\sqrt N}D_N(y)D_N(z)W_N(j)
 =\frac{\kappa}{\sqrt N}D_N(y)D_N(z)
  \frac{(Q;Q)_j(Qyz;Q)_j}
       {(-qy;Q)_{j+1}(-qz;Q)_{j+1}} .
 \tag{16}
\]
The canonical lattice shifts in (11)--(13) verify this interpolation
exactly. The finite Cauchy representation is therefore
\[
 \mathcal C_N(x,y,z)=
   \frac{\kappa}{N^{3/2}}D_N(x)D_N(y)D_N(z)
                      \sum_{j=0}^{N-1}W_N(j)K_N(j).
 \tag{17}
\]
No generic-\(q\) source, value-only interpolation, or periodic gauge
has replaced the original tensor.

## 3. A finite rectangle with all outer poles canceled

For this contour derivation assume first that all three moduli are
strictly less than one. The final canceled formula will extend to the
closed moduli in Section 6; the auxiliary differential need not be
defined at a sample collision.

Put \(t=e^{2\pi is}\). Equation (11) gives exactly
\[
 \frac{W_N(s+N)}{W_N(s)}
  =\Lambda(t):=
 \frac{(1-t)(1-y^Nz^Nt)}
      {(1-\eta y^Nt)(1-\eta z^Nt)} .
 \tag{18}
\]
In particular
\[
 \Lambda(t)-1=
 -\frac{tD_N(y)D_N(z)}
        {(1-\eta y^Nt)(1-\eta z^Nt)}.
 \tag{19}
\]
The variable \(t\) must remain in this monodromy.

Consider the sample-preserving differential
\[
 \Omega_N(s)=
 2\pi i\,
 \frac{(1-\eta y^Nt)(1-\eta z^Nt)}
      {D_N(y)D_N(z)(t-1)}
                   W_N(s)K_N(s)\,ds .
 \tag{20}
\]
Its residue at an integer \(j\) is exactly \(W_N(j)K_N(j)\).
We use a rectangle with vertical sides
\(\Re s=-1/2\) and \(\Re s=N-1/2\).

Here is its complete pole count. The numerator factorials have no
poles in this strip: \(F_N(s)\)'s negative poles lie to the left,
and \(\Re C>0\) puts those of \(F_N(s+C)\) farther left.
The arguments \(s+1+A\) and \(s+1+B_0\) have real parts strictly
between zero and \(2N\). Their zeros, if present, are therefore
in the first simple block from (11).
At a zero of the first denominator,
\[
 s=d-A+k,\qquad e^{2\pi is}=e^{-2\pi iA}
                                      =\eta y^{-N},
 \tag{21}
\]
so the factor \(1-\eta y^Nt\) in (20) cancels it. The
\(z\)-family cancels in exactly the same way. When the families
coincide, the two numerator zeros cancel the two denominator
zeros with matching multiplicity. Thus these outer families
contribute no residues. No estimate of their separate action is used.

Besides the \(N\) integer samples, the only remaining pole is the
moving Cauchy pole
\[
                         s_x=N(1-a)-\tfrac12+iN\ell_x .
 \tag{22}
\]
It lies strictly between the vertical sides. Its imaginary part is
positive, so it does not collide with an integer sample.

Both horizontal sides vanish as their heights tend to infinity.
For completeness, the exact canonical factorial formula gives, for
fixed \(N\), a nonzero constant limit of \(F_N(s)\) as
\(\Im s\to+\infty\), uniformly on bounded real intervals.
Reflection in (11) then gives the lower asymptotic
\[
 F_N(s)\sim c_-(N)\exp\{\,i\pi(s^2-ds)/N\,\}.
 \tag{23}
\]
These limits also follow from the finite cotangent formula for its
logarithmic derivative; its quadratic phase is fixed by (9).
Using the actual offsets \(0,C\) minus \(1+A,1+B_0\), the
\(s\)-dependent lower factor in \(W_N\) is
\(\exp[-2\pi i(1+1/N)s]\), since their offset difference is
\(-N-1\). The norm factor in (20) grows only like
\(e^{2\pi|\Im s|}\) below; \(K_N\) tends to one there.
Thus the lower horizontal integral decays as
\(O_N(e^{-2\pi|\Im s|/N})\).
Above, \(W_N\) tends to a constant and \(K_N\) supplies that
same decay. This establishes the limiting rectangle for the
canonical weight itself.

Define the nonzero geometric quotient
\[
 \boxed{\quad
 \mathcal G_N=
 \frac{\kappa}{\sqrt N}
 \frac{F_N(s_x)F_N(s_x+C)F_N(A)F_N(B_0)}
 {F_N(C)F_N(s_x+1+A-N)F_N(s_x+1+B_0-N)} .
 \quad}
 \tag{24}
\]
All seven arguments are in the original nonzero canonical strip.
The scaled real labels in its numerator are
\[
               1-a,\quad 2-S,\quad 1-b,\quad 1-c,
 \tag{25}
\]
with half-shift \(-1/2\); those in its denominator are
\[
                       1-b-c,\quad1-a-b,\quad1-a-c,
 \tag{26}
\]
without that shift. Their imaginary parts are the corresponding
nonnegative sums of \(N\ell_x,N\ell_y,N\ell_z\).
Strict prism support proves every assertion here.

To check its exact residue normalization, \(K_N\) has residue
\(N/(2\pi i)\) at \(s_x\), and
\(e^{2\pi is_x}=\eta x^N\).
The residue of (20) is therefore
\[
 -\frac{N(1-(xy)^N)(1-(xz)^N)}
        {D_N(x)D_N(y)D_N(z)}W_N(s_x).
 \tag{27}
\]
Shifting the two denominator factorials in \(W_N(s_x)\) down by
\(N\) using (11) produces precisely the factors
\(1-(xy)^N\) and \(1-(xz)^N\). They cancel those in (27)
before any asymptotics. This gives (24).

The exact side difference is
\[
 \Omega_N(s+N)-\Omega_N(s)
       =-2\pi i\,\frac{t}{t-1}W_N(s)K_N(s)\,ds .
 \tag{28}
\]
Both vertical lines are oriented upwards when taking this
difference. The residue theorem, (17), and (27) now give (6) with
the prescribed normalized current
\[
 \boxed{\quad
 \mathcal I_N=
 \frac1{\sqrt N}\int_{-1/2-i\infty}^{-1/2+i\infty}
              \frac{e^{2\pi is}}{e^{2\pi is}-1}
                           W_N(s)K_N(s)\,ds .
 \quad}
 \tag{29}
\]
The minus sign in (6) is the sign of (28).

## 4. Canonical estimates on complete vertical strips

Let \(J\) be the analytic primitive of
\(\log(2\sin\pi w)\) on \(0<\Re w<1\), real on the real
interval and normalized by \(J(0)=0\). Put
\[
 f(w)=J(w)+\frac{i\pi}{2}(w^2-w),\qquad
 h(w)=\sqrt{2\sin\pi w}\,e^{i\pi w/2}.
 \tag{30}
\]
These branches are fixed by their real-interval values. One has
\[
 f'(w)=\operatorname{Log}(1-e^{2\pi iw}),\qquad
                    h(w)^2=i(1-e^{2\pi iw}).
 \tag{31}
\]
For \(0<\Re w<1\), the argument in (31) avoids the negative
real logarithmic cut.

The canonical Gamma-product proof gives, uniformly on the
**entire** vertical strip \(\epsilon\le\Re w\le1-\epsilon\),
\[
 \log G_N(Nw)=NJ(w)+\tfrac12\log(2N\sin\pi w)
       +\frac{\pi\cot\pi w}{12N}+O_\epsilon(N^{-3}).
 \tag{32}
\]
Here is why its usual compact-strip proof is uniform at arbitrarily
large imaginary part as needed in (29). Every Gamma argument
\(Nw,N(k+w),N(k-w)\) stays in a closed right-half-plane
sector. The sum of its Stirling remainders is at most
\[
 CN^{-3}\left[
 |w|^{-3}+\sum_{k\ge1}
              (|k+w|^{-3}+|k-w|^{-3})\right]
                                      \le C_\epsilon N^{-3}.
 \tag{33}
\]
All paired main terms still converge pointwise and define analytic
functions on the whole strip; their identities with \(J\) and the
sine product follow there by analytic continuation. They need not
be bounded term by term. The cotangent and its fixed derivatives
are bounded on this full strip. This proves (32), with fixed
derivatives on slightly smaller strips, directly from the same
Gamma product.

In particular, uniformly on such complete vertical strips,
\[
 \begin{split}
 F_N(Nw)&=\sqrt N\,h(w)e^{Nf(w)}(1+O_\epsilon(N^{-1})),\\
 F_N(Nw-\tfrac12)&=
 \sqrt N\,\xi_Ne^{Nf(w)}(1+O_\epsilon(N^{-1})),
 \qquad \xi_N=e^{i\pi/4-\pi i/(8N)} .
 \end{split}
 \tag{34}
\]
Bounded derivatives of \(\log(2\sin\pi w)\) on the full strip
justify the half-shift expansion, including unbounded imaginary
parts.

The one unshifted endpoint factor in the current has an exact
formula instead of a strip approximation:
\[
 \boxed{\qquad
             |F_N(-1/2+iT)|^2
                           =\frac{N}{1+e^{-2\pi T}}
                           \quad(T\in\mathbb R).
 \qquad}
 \tag{35}
\]
Indeed every Gamma ratio in (9) has modulus one on this line,
as does its corresponding positive-base power.
The remaining factor is
\[
 |G_N(-1/2+iT)|^2=
          \frac{N}{2\pi}|\Gamma(1/2+iT)|^2
                         =\frac{N}{2\cosh\pi T}.
 \tag{36}
\]
The exponential in (10) multiplies this by \(e^{\pi T}\).
This proves (35) with the original canonical normalization.

## 5. The complete vertical current is uniformly bounded

Write \(s=-1/2+iNY\). Introduce the scaled arguments
\[
 \begin{gathered}
 a_Y=1-b+i(Y+\ell_y),\qquad b_Y=1-c+i(Y+\ell_z),\\
 c_Y=1-b-c+i(Y+\ell_y+\ell_z),\\
 Q_0(Y)=f(c_Y)-f(a_Y)-f(b_Y)
                         +f(a_0)+f(b_0)-f(c_0).
 \end{gathered}
 \tag{37}
\]
The notation \(Q_0\) is a function, not the root \(Q\).
Every real part in (37) stays in a fixed strict substrip on
the stated shape compacts. Applying (34) to all shifted factors
of (14) gives
\[
 \frac{W_N(s)}{F_N(s)}=
 \frac{\xi_N^3}{h(c_0)h(a_Y)h(b_Y)}
                         e^{NQ_0(Y)}(1+O(N^{-1})).
 \tag{38}
\]
Its amplitude is bounded uniformly for all \(Y\in\mathbb R\).
For example, because \(0<b,c<1/2\) stay in fixed compact
intervals, \(|1-v e^{-2\pi ib}|\) and
\(|1-v e^{-2\pi ic}|\) have positive lower bounds for every
\(v\ge0\). They also grow at infinity. Equation (31) applies
this observation to \(h(a_Y)\) and \(h(b_Y)\);
\(h(c_0)\ne0\) is a fixed compact-parameter factor.

Define the real rate
\[
            R_0(Y)=\Re Q_0(Y)+\pi\min(Y,0),\qquad R_0(0)=0.
 \tag{39}
\]
Equations (35) and (38) prove the actual quantum bound
\[
              |W_N(-1/2+iNY)|/\sqrt N
                                   \le C e^{NR_0(Y)}.
 \tag{40}
\]
It remains to bound this explicit rate on both halves of the line.
Put \(v_y=r_y e^{-2\pi Y}\), \(v_z=r_z e^{-2\pi Y}\),
and \(v_0=r_yr_z e^{-2\pi Y}\). Use the continuous arguments
specified by (31). Differentiation gives
\[
 \begin{split}
 T(Y)={}&\arg(1-v_y e^{-2\pi ib})
      +\arg(1-v_z e^{-2\pi ic})
            -\arg(1-v_0 e^{-2\pi i(b+c)}),\\
 R_0'(Y)&=
 \begin{cases}
 T(Y),&Y>0,\\
 \pi+T(Y),&Y<0.
 \end{cases}
 \end{split}
 \tag{41}
\]
These are original-strip arguments, not a freely adjusted logarithmic
lift.

For \(Y>0\), all three \(v_y,v_z,v_0\) are less than one.
Every argument in the first line of (41) lies between
\(-\pi/2\) and \(\pi/2\). Hence
\[
                         T(Y)<3\pi/2 .
 \tag{42}
\]
For \(Y<0\), the first two arguments in
(41) are positive because \(0<b,c<1/2\).
If \(b+c\ge1/2\), the third argument is nonpositive, and
therefore \(T(Y)>0\). If \(b+c<1/2\), the function
\(\arg(1-t e^{-2\pi i(b+c)})\) increases with \(t>0\).
Let \(k=\min(v_y,v_z)>0\). Then \(v_0\le k\), and
the first two arguments also increase with their radii.
It therefore suffices to prove
\[
 \arg(1-k e^{-2\pi ib})+\arg(1-k e^{-2\pi ic})
               -\arg(1-ke^{-2\pi i(b+c)})>0.
 \tag{43}
\]
For a direct proof put \(\theta=2\pi b\), \(\varphi=2\pi c\).
The ratio
\[
 Z_k=\frac{(1-ke^{-i\theta})(1-ke^{-i\varphi})}
                 {1-ke^{-i(\theta+\varphi)}}
 \tag{44}
\]
has strictly positive imaginary part: multiply by the conjugate
denominator to obtain numerator
\[
 2k(1+k)\sin\frac{\theta+\varphi}{2}
       \left(\cos\frac{\theta-\varphi}{2}
                         -\cos\frac{\theta+\varphi}{2}\right)>0.
\]
Here \(0<b,c<1/2\) and \(b+c<1\).
Its continuous argument, starting at zero as \(k\to0\),
lies in \((0,\pi)\). This is precisely (43).
We have proved
\[
             R_0(Y)\le
 \begin{cases}
 3\pi Y/2,&Y\ge0,\\
 \pi Y,&Y\le0.
 \end{cases}
 \tag{45}
\]

On the same half-step line \(t=-e^{-2\pi NY}\), so
\[
 \left|\frac{t}{t-1}\right|
 =\frac1{1+e^{2\pi NY}}
 \le
 \begin{cases}
 e^{-2\pi NY},&Y\ge0,\\
 1,&Y\le0.
 \end{cases}
 \tag{46}
\]
Also \(K_N(s)=(1+x e^{2\pi Y})^{-1}\) exactly. The estimate
\[
 |1-r_x e^{2\pi Y}e^{-2\pi ia}|
        \ge \sin(\pi a)(1+r_x e^{2\pi Y})
 \tag{47}
\]
makes this Cauchy factor uniformly bounded on the strict shape
compacts. Finally \(ds=iN\,dY\). Combining (29), (40),
and (45)--(47) gives
\[
 |\mathcal I_N|
 \le CN\left[\int_{-\infty}^0e^{\pi NY}\,dY+
                    \int_0^\infty e^{-\pi NY/2}\,dY\right]
 \le C .
 \tag{48}
\]
Both halves of the same canonical current have now been controlled.
No bound from a different periodic interpolation was transferred.

## 6. The initialized geometric residue and the growing branch

For the seven strict-strip arguments in (24), use (34).
The four numerator factors have half-shift \(-1/2\);
the three denominator factors have shift zero.
Their powers of \(N\), including the prefactor
\(\kappa/\sqrt N\), cancel. Since
\(h(w)=e^{i\pi/4}(1-e^{2\pi iw})^{1/2}\) on the upper part
of the original strip, the remaining amplitude and phase are
\[
             \kappa e^{\,i\pi/4-\pi i/(2N)}
                       [(1-xy)(1-xz)(1-yz)]^{-1/2}.
 \tag{49}
\]
The clocks of the four numerator arguments are
\(-x,-xyz,-y,-z\); those of the denominators are
\(yz,xy,xz\). On this upper strip
\[
                  f(w)=\frac{i}{2\pi}
                         \operatorname{Li}_2(e^{2\pi iw})
                                      -\frac{i\pi}{12}.
 \tag{50}
\]
The sum of four numerator phases minus three denominator phases
is exactly \(i\Psi(x,y,z)\). This proves (7), with its
coefficient fixed by the actual moving-pole residue.

We now include the unit boundary. All factors of (24) remain regular
and nonzero when any \(\ell_i=0\): their real parts stay in the same
strict canonical strips. In (29), the shifted factorials and the
Cauchy factor remain regular for all real \(Y\). The lower bounds
for \(h(c_0),h(a_Y),h(b_Y)\), (42), the inequality
\(v_0\le\min(v_y,v_z)\), and (47) are uniform for
\(r_x,r_y,r_z\in[r_0,1]\). The integrable majorant in (48)
is therefore uniform up to that boundary. Dominated convergence
extends the final canceled identity (6), and its bound, from
\(r_i<1\) to \(r_i\le1\). This step extends neither the
uncanceled differential (20) nor a pole count through a collision.
In particular, whenever \(D_N(x)D_N(y)D_N(z)=0\),
\(\mathcal C_N=\mathcal G_N\) exactly. All level-dependent approaches
to these norm walls are included in the same estimate.

Equations (6) and (48) bound the full correction by \(O(N^{-1})\)
on the whole closed-moduli tube. On any portion where
\(-\Im\Psi\ge0\), (7) has modulus bounded away from zero;
thus (8) follows uniformly there.
For the common-radial subfamily, the prism radial theorem proves
\(-\Im\Psi>0\) for every strict shape and \(0<r\le1\).
Its minimum is positive on the compact families in the theorem,
so the current is then exponentially small relative to
\(\mathcal G_N\).
Symmetry covers the initial permutation choosing the two smaller
angles. No sign of the height has been assumed elsewhere in
the tube.

The result concerns the actual universal local source. A global
Conway theorem still needs to place all geometric attachments in
compatible source charts and control the assembled coefficient
cycle and competing contributions. Nothing here identifies arbitrary
vertex evaluations with that whole period. The \(r_i\to0\) layers
and angular prism-face collisions remain outside the stated
uniform estimate.

## Complete proof sources

All four complete proof texts were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [Exact original wall and Cauchy source](research_centered_tensor_wall_cauchy_source.md) | 3cda6a170c46abf27a1c8c15b110780ebcb6017a5aa18758a4e51ba0a271892c |
| [Strict prism action and radial growth](research_centered_tensor_prism_radial_bridge.md) | 892dfc5ef5e0774d45ccc44bc4f5122e7137d6185fe9191997e1b43d79003776 |
| [Canonical factorial, exact phase and ends](research_exact_cyclotomic_factorial.md) | 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b |
| [Canonical Gamma interpolation and Stirling proof](../papers/conway-asymptotics/factorial.tex) | fa05557505927ae81f005b90edbd3d0946288e7eacf2363f070d9753db632fe1 |

The exact wall source and radial growth were already established.
The source-specific additions are the completed canonical rectangle,
its exact removal of the outer families, the uniformly bounded full
current in the two-small-angle chamber, and the resulting actual
transport of the initialized tensor. No novelty is claimed for
Gamma reflection, residue calculus or Stirling's method.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git
operation or earlier-final edit was performed.
