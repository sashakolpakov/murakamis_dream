# The complete source has an exponentially small fixed-time observation

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The positive crossing form can be tested on the specified complete-end
source, rather than on an arbitrarily chosen vector. For every fixed
positive crossing horizon, its observation energy is exponentially
smaller than the squared norm of that source. The loss comes from
an alternating physical-value observation. The complete source is
concentrated near the complete color, but that concentration does not
give a lower bound for this observation.

Sections 1–4 give the upper bound for every fixed positive real
crossing horizon. Sections 5–6 determine the nonzero leading term
of the observation and its positive energy for every fixed real
horizon at least three. These are statements about the specified
complete source. The original signed internal-pair closure is a
different bilinear observation.

## 1. The original source and its observation

Let \(N=2m\) be even, and use the physical nodes and weights
\[
 c_a=2\cos((2a+1)\pi/N),\quad
 \sigma_a=2(-1)^a\sin((2a+1)\pi/N),\quad
 Q(z)=2T_m(z/2),\qquad 0\le a<m.
 \tag{1}
\]
Thus \(\sigma_a=N/Q'(c_a)\). Write
\[
 \tau_a=\arccos(-c_a/2),\qquad
 T_a=N\tau_a^2/(4\pi),\qquad
 F_a=\mathcal L_N(c_a),
 \quad \mathcal L_N(z)=\sum_{j=0}^{m-1}e_j(z)e_j(-2).
 \tag{2}
\]
These are the actual complete-kernel values:
\(F_a=K_N(c_a,-2)>0\). Define, for real \(s>2\),
\[
 (\mathcal O_tF)(s)=
      \sum_{a=0}^{m-1}\frac{\sigma_a e^{itT_a}F_a}{s-c_a}.
 \tag{3}
\]
The scalar crossing carrier has modulus one and cancels from this
energy. The
[exact Gramian theorem](research_trace_normal_defect_positive_form.md#6-exact-transport-through-ordinary-value-observations)
gives
\[
 F^*H_{n,N}F=
 \frac{N}{2\pi}\int_0^n\int_2^\infty
       \operatorname{arcosh}(s/2)|(\mathcal O_tF)(s)|^2\,ds\,dt.
 \tag{4}
\]

**Theorem 1.** Fix a real \(n>0\). There are
\(\delta_n>0\), \(A<\infty\), and \(C<\infty\), independent of
the even level, such that
\[
 |(\mathcal O_tF)(s)|
   \le \frac{CN^A}{s+1}e^{N(M_\infty-\delta_n)}
       \quad(0\le t\le n,\ s>2),
 \qquad M_\infty=4G/\pi.
 \tag{5}
\]
Consequently,
\[
 0<\frac{F^*H_{n,N}F}{\|F\|_2^2}
       \le CN^A e^{-2\delta_nN},\qquad
 \frac{\|H_{n,N}F\|_2}{\|F\|_2}
       \le CN^A e^{-\delta_nN},
 \tag{6}
\]
after increasing the constants and polynomial powers.
This is the original complete vector at every even level.
No spectral projection or prepared component is assumed.

## 2. Two existing bounds for the complete factor

Write \(L_N(\tau)=\mathcal L_N(-2\cos\tau)\). The complete
edge packet and its ordinary real-period bound imply the
following two estimates.
There are \(r,c,C_1>0\) and polynomial factors such that
\[
 |L_N(a+ib)|\le CN^A
       e^{N(M_\infty-ca^2+C_1b^2)}
                   \qquad(|a|,|b|\le r).
 \tag{7}
\]
For every fixed \(b_0>0\), there is \(d(b_0)>0\) with
\[
 |L_N(\tau)|\le CN^A e^{N(M_\infty-d(b_0))}
                       \qquad b_0\le|\tau|\le\pi.
 \tag{8}
\]
For (7), use the
[thin complete-kernel theorem](research_bare_kernel_thin_rectangle.md)
and
\(\psi(\tau,0)=M_\infty-\tau^2/(4\pi)+O(\tau^4)\).
The omitted original high indices have a smaller rate on a
sufficiently small complex neighborhood, so the same estimate
holds for the literal low polynomial \(L_N\).
For (8), keep the thin theorem's fixed wire contour at the
complete point. The
[factorial angular-loss inequality](research_uniform_factorial_and_boundary_decay.md#4-decay-in-the-real-boundary-angle)
adds a uniform loss \(c_2(1-\cos\tau)\) to every retained
contour piece. The original omitted low indices retain their
strict gap, since their positive Fourier coefficients give
\(|e_j(-2\cos\tau)|\le e_j(-2)\) on the real period.
These two bounds prove (8) directly for the low polynomial.
They are also the thin-contour argument used to extend the
[whole outside-period estimate](research_pair_free_boundary_kernel.md#7-whole-outside-period-decay-and-a-complex-strip)
to zero selected charge; no application of that theorem's
strictly positive compact domain at its excluded endpoint
is needed.
These arguments keep the full physical values.

The same packet at the nearest physical angle \(\pi/N\) gives
\[
                  \|F\|_2^2\ge c_0N^{-3}e^{2NM_\infty}
 \tag{9}
\]
for all sufficiently large even levels. A single physical entry
suffices for (9).

## 3. The exact simple-pole contour

Choose a fixed \(b>0\), small enough that
\[
                 2b<r,\qquad \frac{2nb}{2\pi}<\frac18.
 \tag{10}
\]
Choose midpoint cuts \(b_N=2\pi k_N/N\) tending to \(b\).
For all sufficiently large levels \(b/2<b_N<2b\).
Let \(\mathcal R_N\) be the positively oriented rectangle with
corners \(\pm b_N\pm ih\), where \(h>0\) is fixed and small.
On its closure arrange
\[
 C_1h\le1/8,\qquad
 \Re\cos\tau>1/2,\qquad h<r.
 \tag{11}
\]

The part of (3) with \(\tau_a<b_N\) has the exact contour
representation
\[
 \boxed{\quad
 (\mathcal O_tF)_{\rm in}(s)
  =\frac{N}{4\pi i}\oint_{\partial\mathcal R_N}
    \frac{2\sin\tau\,e^{itN\tau^2/(4\pi)}L_N(\tau)}
         {(s+2\cos\tau)\,2(-1)^m\cos(N\tau/2)}\,d\tau .
 \quad}
 \tag{12}
\]
Indeed \(Q(-2\cos\tau)=2(-1)^m\cos(N\tau/2)\).
The substitution \(z=-2\cos\tau\), with \(dz=2\sin\tau\,d\tau\),
puts a simple pole at each of the two angles \(\pm\tau_a\).
Each residue is \(e^{itT_a}F_a/((s-c_a)Q'(c_a))\).
The factor \(1/2\) in (12) compensates for these two copies.
There is no pole at \(\tau=0\), and the condition in (11)
excludes a pole from \(s+2\cos\tau\).
This proves (12) directly at every level, including its sign.

On the horizontal sides,
\[
 |\cos(N\tau/2)|^{-1}\le C e^{-Nh/2}.
 \tag{13}
\]
On a midpoint vertical side the same bound is
\(|\cos(N(b_N+iv)/2)|^{-1}\le2e^{-N|v|/2}\).
The crossing factor costs at most
\(\exp(nN|a||v|/(2\pi))\), uniformly for \(0\le t\le n\).
Also \(|s+2\cos\tau|^{-1}\le(s+1)^{-1}\).

On a horizontal side, (7), (10), and (11) bound the total rate
by \(M_\infty-h/4\). On a vertical side they bound it by
\[
             M_\infty-cb^2/4-|v|/4.
 \tag{14}
\]
The original sine factor, contour lengths, and prefactors cost
only a polynomial. Thus the retained observation satisfies (5)
with a loss at least \(\min(h/4,cb^2/4)\).

For the omitted physical rows, use (8) with \(b_0=b/2\).
The smallest distance of a node from 2 is
\[
             2-c_0=4\sin^2(\pi/(2N))\ge4/N^2.
 \tag{15}
\]
Consequently \(1/(s-c_a)\le N^2/(s+1)\), uniformly for \(s>2\).
The weights satisfy \(|\sigma_a|\le2\), the crossing values
have modulus one, and there are at most \(N\) rows. Hence the
omitted observation also satisfies (5), with loss \(d(b/2)\).
Take the smaller of these three positive losses.
Finitely many small levels are absorbed in the constant.

## 4. Integration and the meaning of the loss

The remaining majorant in \(s\) is integrable, with the exact value
\[
 \int_2^\infty\frac{\operatorname{arcosh}(s/2)}{(s+1)^2}\,ds
   =\int_0^\infty\frac{du}{2\cosh u+1}
   =\frac{\pi}{3\sqrt3}.
 \tag{16}
\]
The first equality follows by integration by parts and
\(s=2\cosh u\); the second uses \(\tanh(u/2)\).
Substitute (5) in (4) and divide by (9) to obtain the first
bound in (6).

The exact entries of \(H_{n,N}\) also give
\(\|H_{n,N}\|\le C_nN^3\): its diagonal is \(O(nN)\),
the off-diagonal cardinal denominators have inverse at most
polynomial size \(O(N^2)\), and there are \(O(N)\) entries
in each row. Since \(H_{n,N}\) is positive,
\(\|H_{n,N}F\|^2\le\|H_{n,N}\|F^*H_{n,N}F\).
This proves the second bound in (6).

Thus the actual complete source is an approximate null vector of
the fixed-time positive observation, with an exponentially small
relative defect. This does not assert invariance under the crossing
unitaries themselves. Nor does it determine the smaller observation
rate: (5) alone is only a strict upper bound below \(M_\infty\).

## 5. A nonzero half-charge observation

Put \(\Psi(t)=\psi(t,0)\), on its original complete branch. Thus
\[
 \Psi(0)=M_\infty,\qquad
 \Psi'(t)=-\frac1\pi\operatorname{asinh}(\tan(t/2)),\qquad
 \Psi''(t)=-\frac{\sec(t/2)}{2\pi}.
 \tag{17}
\]
For a fixed real \(n\ge3\), let \(t_n=a_n-iH_n\) be the
positive complete-end leaf with charge \(1/2\):
\[
 n t_n+2i\operatorname{asinh}(\tan(t_n/2))=\pi.
 \tag{18}
\]
The elementary continuation argument below constructs this
solution uniquely; no asymptotic source coefficient is used
in its definition. Define
\[
 \begin{split}
 S_n(t)&=\Psi(t)+\frac{in t^2}{4\pi}-\frac{it}{2},&
 \mathcal S_n&=S_n(t_n),&
 M_n&=\Re\mathcal S_n,\\
 A_n&=-S_n''(t_n)
       =\frac{\sec(t_n/2)-in}{2\pi},&
 b_n(s)&=\frac{\sqrt{2\pi}}{\pi i}
       \frac{\sin t_n\,a_e(t_n,0)}
       {(s+2\cos t_n)\sqrt{A_n}}.
 \end{split}
 \tag{19}
\]
Here \(a_e\) is the original nonzero edge amplitude in the
[free-boundary kernel theorem](research_pair_free_boundary_kernel.md#1-domain-and-statement).
The square root of \(A_n\) has positive real part.

**Theorem 2.** For every fixed real \(n\ge3\), uniformly for
real \(s>2\), through the even levels,
\[
 (\mathcal O_nF)(s)
   =(-1)^{N/2}N^{-1}b_n(s)e^{N\mathcal S_n}
                  (1+O(N^{-1})).
 \tag{20}
\]
The coefficient never vanishes and satisfies
\(c_n/(s+1)\le |b_n(s)|\le C_n/(s+1)\).
The expansion is uniform also for real crossing times in a fixed
neighborhood of \(n\), using the analytic continuation of (18).
It includes all fixed parameter derivatives on smaller
neighborhoods. In particular this is an asymptotic for the
original alternating sum (3), not for a positive replacement.

*Existence of the scalar saddle.*
Set \(f_n(t)=nt+2i\operatorname{asinh}\tan(t/2)\).
On the rectangle \(0<a<\pi/3,\ 0<H<2/5\),
\(\Re f'_n(t)=n-\Im\sec(t/2)>n\). Thus \(f_n\) is
one-to-one there: integrate its derivative on the straight
segment between any two points. The small-charge equation
\(f_n(t)=2\pi\chi\) starts with
\(t=2\pi\chi/(n+i)+O(\chi^3)\).
It cannot reach \(a=0\) or \(H=0\) at positive charge:
the imaginary equation would force the other coordinate
to vanish as well. At \(a=\pi/3\),
\(\Re f_n=na-2\Im r>\pi\). At \(H=2/5\),
\(\Im f_n=-nH+2\Re r< -6/5+\log3<0\),
because \(\Re r(a-iH)\le r(a)\le(\log3)/2\).
These exclude every boundary for \(0<\chi\le1/2\).
The nonzero derivative and compactness continue the initial
solution through that whole interval. This proves existence
and uniqueness, also for noninteger real \(n\ge3\).

*Separation from the physical tails.*
Write \(r(t)=\operatorname{asinh}(\tan(t/2))=k+ig\).
On the positive leaf, \(g<0\), \(k>0\). At charge
\(\chi\in(0,1/2]\), the period relation
\(g=na/2-\pi\chi\) gives \(0<a<2\pi\chi/n\). Furthermore
\[
 \partial_H\Re r(a-iH)=\tfrac12\Im\sec((a-iH)/2)<0.
\]
Consequently
\[
 H=\frac{2k}{n}
   \le\frac2n\operatorname{asinh}\tan(\pi\chi/n)
   \le\frac23\operatorname{asinh}\tan(\pi\chi/3)
   \le\frac{2\log3}{3}\chi.
 \tag{21}
\]
The last inequality is the chord bound for the convex function
\(\operatorname{asinh}\tan x\) on \([0,\pi/6]\);
its endpoint value is \((\log3)/2\).
In particular
\[
        0<a_n<\pi/3,\qquad 0<H_n<\log3/3<2/5.
 \tag{22}
\]
At the stationary point the derivative of the real action with
respect to charge is \(-H\). Integration of (21) gives
\[
 M_n>M_\infty-\frac{\log3}{12}.
 \tag{23}
\]
On the real interval, (17) gives
\[
 \Psi(\pi/2)\le M_\infty-\frac{\pi}{16}
            <M_n-\frac7{80}.
 \tag{24}
\]
For the last strict inequality use \(\pi>3\) and
\(\log3<6/5\).

The local edge packet used in (19) is legitimate at \(t_n\).
Indeed \(\Re r(a-iH)\le r(a)\le3a/4\) for
\(0\le a\le\pi/3\), since \(r'(a)=\sec(a/2)/2<3/4\).
Thus \(H_n\le a_n/2\). As \(\cosh(2/5)<6/5\),
\[
 \cosh H_n-1\le\frac35H_n^2
              \le\frac3{20}a_n^2
              <1-\cos a_n.
 \tag{25}
\]
Here \(1-\cos a\ge a^2/3\) on \([0,\pi/3]\), for example
by the Taylor bound \(1-\cos a\ge a^2/2-a^4/24\).
Therefore \(|\cos(t_n/2)|<1\). The saddle lies strictly
inside the free-boundary theorem's domain, with height less
than \(2/5\).

*The literal contour and its side terms.*
Choose midpoint cuts \(T_N=2\pi k_N/N\) with
\(|T_N-\pi/2|\le2\pi/N\). Use (12) on the rectangle
with real ends \(\pm T_N\) and heights \(\pm H_n\).
Its integrand is odd in the angular variable, so the upper
horizontal integral equals the lower horizontal integral
after reversing the parameter. They add. On the lower side,
\[
 \frac1{2(-1)^{N/2}\cos(Nt/2)}
   =\frac{(-1)^{N/2}e^{-iNt/2}}{1+e^{-iNt}}.
 \tag{26}
\]
Thus the principal lower integral, including its exact scalar, is
\[
 \frac{(-1)^{N/2}N}{\pi i}
 \int_{-T_N-iH_n}^{T_N-iH_n}
 \frac{\sin t\,L_N(t)e^{inNt^2/(4\pi)-iNt/2}}
 {(s+2\cos t)(1+e^{-iNt})}\,dt.
 \tag{27}
\]
The denominator in (26) differs from one exponentially
uniformly on this segment.

The [complete-edge logarithmic theorem](research_internal_pair_complete_edge_gap.md#3-the-full-complete-end-kernel-at-both-parities)
gives
\(L_N(t)=\exp\{N\Psi(t)+O(\log N)\}\)
on a neighborhood of
\(\{|\Re t|\le\pi/2,\ |\Im t|\le2/5\}\).
Reflection and conjugation give the negative-real and upper
parts of this rectangle from the stated positive one.
The small midpoint enlargement is contained in the same
neighborhood for large \(N\).
On each fixed-height line in this rectangle,
\[
 \frac{d^2}{da^2}\Re S_n(a-iH_n)
       =-\frac{\Re\sec((a-iH_n)/2)}{2\pi}<0.
 \tag{28}
\]
The critical point \(a=a_n\) is therefore the unique strict
maximum of the whole lower horizontal segment.

All vertical sides retain their exact cosine denominator.
At a midpoint its reciprocal is bounded by
\(2e^{-N|h|/2}\).
For the lower right side the resulting rate is
\(\Re S_n(T_N-ih)\), \(0\le h\le H_n\), and
\[
 \partial_h\Re S_n(T_N-ih)
   =-\frac{\Im r(T_N-ih)}{\pi}
                       +\frac{nT_N}{2\pi}-\frac12>0
 \tag{29}
\]
for all large \(N\). Its maximum is at \(h=H_n\),
strictly below \(M_n\) by (28).
On the lower left side, \(-\pi/2<\Im r(-T_N-ih)\le0\);
the derivative is
\(-\Im r/\pi-nT_N/(2\pi)-1/2<0\).
Its maximum is \(\Psi(T_N)\), below \(M_n\) by (24).
The upper sides have the same bounds by \(t\mapsto-t\).
Every connector therefore has a fixed strict exponential gap.

For completeness, the omitted physical rows require no
off-grid approximation near \(t=\pi\). At \(w=-2\), the
actual positive Jacobi ratios
\(F_{a+1}(-2)/F_a(-2)>1\) show that the physical values
\(F_a=L_N(\tau_a)\) decrease as \(\tau_a\) increases.
The largest omitted value is bounded by a physical value
at \(T_N+O(N^{-1})\), whose logarithmic rate is
\(\Psi(\pi/2)\). The estimate (15) controls the denominator
uniformly in \(s>2\). Hence the entire omitted physical sum
has the same strict gap.

Finally, \(\Re\cos t\) is bounded below by a fixed number
greater than \(-1/2\) on these contours. Thus
\(|s+2\cos t|^{-1}\le C/(s+1)\). All fixed angular
derivatives obey the corresponding bound. Near \(t_n\)
insert the actual edge expansion
\(L_N=N^{-3/2}a_e(t,0)e^{N\Psi(t)}(1+O(N^{-1}))\)
into (27). The ordinary complex Gaussian integral,
with \(\Re A_n>0\), gives exactly (19)–(20).
The sine, the edge amplitude, and \(A_n\) are all nonzero.
The relative error is uniform for \(s>2\), since after
multiplication by \(s+1\) the rational amplitude and its
derivatives form a compact bounded family with nonzero
leading value. All gaps persist on a small complex
crossing-time neighborhood of \(n\), by continuity on the
fixed contours. The finite observation and its normalized
remainder are holomorphic there; Cauchy's formula supplies
the asserted parameter derivatives on smaller neighborhoods.
This proves the theorem. \(\square\)

## 6. The exact exponential rate of the positive energy

**Corollary 3.** For each fixed real \(n\ge3\),
\[
 F^*H_{n,N}F
   =C_nN^{-2}e^{2NM_n}(1+O(N^{-1})),\qquad
 C_n=\frac1{4\pi M'_n}
       \int_2^\infty\operatorname{arcosh}(s/2)|b_n(s)|^2\,ds>0,
 \quad M'_n=\frac{a_nH_n}{2\pi}>0.
 \tag{30}
\]
The derivative here is with respect to the real crossing time
on the local continuation of (18).

*Proof.* The stationary derivative gives
\(\partial_n\mathcal S_n=it_n^2/(4\pi)\), hence the
displayed formula for \(M'_n\).
It remains to control the part of the time integral outside
the neighborhood where (20) holds; positivity alone would not
give its upper bound.

Use the same rectangle of height \(H_n\) for every time
\(0\le v\le n\). On its lower horizontal side the real rate is
\[
 R_v(a)=\Re\Psi(a-iH_n)
              +\frac{v aH_n}{2\pi}-\frac{H_n}{2}.
 \tag{31}
\]
For \(a\ge0\), \(R_v(a)\le R_n(a)\); for \(a\le0\),
\(R_v(a)\le R_n(-a)\). If \(v\le n-\epsilon\), equality
with \(M_n\) is impossible: the only maximizer of \(R_n\)
is \(a_n>0\), where a strict crossing-time loss remains.
Compactness gives a uniform strict gap on this earlier time
interval. The connectors are bounded by the same \(n\)-time
right side or by the strictly smaller real endpoint rate.
The original physical tails are independent of \(v\) in
absolute value. Thus the earlier-time contribution is
exponentially smaller, with the integrable majorant
\(C/(s+1)^2\).

Near \(v=n\), substitute the uniform expansion (20) into
(4). Since \(M'_n>0\), the ordinary endpoint Laplace
integral in \(v\) contributes \((2NM'_n)^{-1}\).
The factors are \(N/(2\pi)\) from the Gramian,
\(N^{-2}\) from the squared observation, and this endpoint
factor. This proves (30), including its coefficient.
The integral is finite by (16) and positive by the
nonvanishing in Theorem 2. \(\square\)

The positive form therefore measures a specific smaller action,
the half-charge leaf action. It still does not identify the
nonzero coefficient of the original same-sign internal pair:
that closure uses the signed bilinear convolution, not the
absolute square in (4).

## 7. Complex colors and the exact normal defect

The interpolation formula also specifies which residue is added
when the observation color enters the shifted contour.
This distinction matters when the observation is subsequently
used inside an original trace.

Let \(\mathcal I_{n,N}\) be the polynomial of degree less than
\(N/2\) interpolating
\(\exp(inT_a)F_a\) at all the nodes \(c_a\). On the slit
plane \(\mathbb C\setminus[2,\infty)\), put
\[
 h_{n,N}(w)=
   \exp\!\left(\frac{inN\,\arccos(-w/2)^2}{4\pi}\right)
                      \mathcal L_N(w),\qquad
 \mathscr D_{n,N}(w)=
             \frac{h_{n,N}(w)-\mathcal I_{n,N}(w)}{Q(w)}.
 \tag{32}
\]
The square of the inverse cosine is holomorphic through
\(w=-2\), on the branch fixed by the positive real angular
interval. The numerator in \(\mathscr D\) vanishes at every
root of \(Q\), so this function is holomorphic through all
physical nodes. It satisfies exactly
\[
 \mathcal O_nF(w)=N\frac{\mathcal I_{n,N}(w)}{Q(w)},\qquad
 h'_{n,N}(c_a)-(\mathcal I_{n,N})'(c_a)
                         =Q'(c_a)\mathscr D_{n,N}(c_a).
 \tag{33}
\]
Thus \(\mathscr D\) represents the full interpolation-normal
defect in the original trace. The unit scalar crossing
carrier, omitted from \(\mathcal O_n\), multiplies both sides
when the original \(R^n\) is restored.

Let \(\mathcal J_{n,N}(w)\) denote the contour integral on
the right side of (12), with \(b_N=T_N\), \(h=H_n\), and
\(s=w\). Let \(\mathcal T_{n,N}(w)\) be the original
omitted physical sum with \(\tau_a\ge T_N\).
For \(w=-2\cos(a-iH)\), \(0<a<\pi/2\), \(H>0\), away
from the contour, write \(\nu_N(w)=1\) if
\(a<T_N\) and \(H<H_n\), and zero otherwise.
Then the exact identities are
\[
 \begin{split}
 \mathcal J_{n,N}(w)
   &=\mathcal O_nF(w)-\mathcal T_{n,N}(w)
                         -N\nu_N(w)\frac{h_{n,N}(w)}{Q(w)},\\
 \mathscr D_{n,N}(w)
   &=(1-\nu_N(w))\frac{h_{n,N}(w)}{Q(w)}
        -\frac{\mathcal J_{n,N}(w)+\mathcal T_{n,N}(w)}{N}.
 \end{split}
 \tag{34}
\]
Indeed the extra two angular poles are at
\(t=\pm(a-iH)\). Each has residue
\(-h_{n,N}(w)/Q(w)\), because the factor \(2\sin t\)
in (12) cancels the derivative of \(w+2\cos t\).
Multiplication by \(N/(4\pi i)\) and the two residues
gives exactly \(-Nh_{n,N}(w)/Q(w)\).
This proves (34) with its sign and scalar.

**Corollary 4.** Fix \(n\ge3\). On every compact set of
colors \(w=-2\cos(a-iH)\) with
\(0<a<\pi/2\) and \(H>H_n\),
\[
 \begin{split}
 \frac{\mathcal I_{n,N}(w)}{Q(w)}
  &=(-1)^{N/2}N^{-2}b_n(w)e^{N\mathcal S_n}
                                      (1+O(N^{-1})),\\
 \mathscr D_{n,N}(w)
  &=\frac{h_{n,N}(w)}{Q(w)}
    -(-1)^{N/2}N^{-2}b_n(w)e^{N\mathcal S_n}
                                      (1+O(N^{-1})).
 \end{split}
 \tag{35}
\]
Here \(b_n(w)\) is the same rational function of the
observation color as in (19). All fixed complex-color
derivatives have the corresponding holomorphic expansions
on smaller neighborhoods.

*Proof.* Such a compact set is separated from the image
of the rectangle boundary and from the real physical nodes.
The proof of Theorem 2 therefore applies to
\(\mathcal J_{n,N}(w)\), with bounded complex denominators
and the same nonzero leading coefficient.
The omitted physical sum has the rate in (24), uniformly
on this compact set. Here \(\nu_N=0\) for all large levels.
Equations (33)–(34) give (35); Cauchy's formula gives
the derivative statements. \(\square\)

This corollary does not assume that the first term in the
normal defect dominates the second. That comparison requires
the actual observation color. Formula (34) also shows why
one cannot analytically continue the exterior formula
through the shifted contour without its extra residue.

There is also an exact trace reduction that uses this same
holomorphic defect. For \(0\le j<N/2\), set
\[
 S_{j,N}=\prod_{r=1}^j2\sin(r\pi/N),\qquad
 Q_{j,N}(z)=\prod_{a=j}^{N/2-1}(z-c_a),\qquad S_{0,N}=1.
 \tag{36}
\]
Let \(\Gamma_j\) be any positively oriented contour in the
slit plane enclosing precisely these remaining nodes.
The original complete-source trace satisfies
\[
 \boxed{\quad
 \phi_N[R^n\mathcal L_N e_j]
   =\frac{\eta C_{N,n}N^2(-1)^j}{2\pi i S_{j,N}^2}
           \oint_{\Gamma_j}
                 \frac{\mathscr D_{n,N}(z)}{Q_{j,N}(z)}\,dz .
 \quad}
 \tag{37}
\]
Here \(C_{N,n}=\exp(\pi i n(N-1)^2/(4N))\) is the
original scalar crossing carrier; \(R^n\) denotes the
original Hermite crossing flow when \(n\) is noninteger.
The [normal-defect trace identity](research_trace_normal_defect_positive_form.md#1-the-interpolation-identity-at-both-parities)
gives its left side as
\(\eta C_{N,n}\sum_a(4-c_a^2)Q'(c_a)
\mathscr D_{n,N}(c_a)e_j(c_a)\).
At even physical nodes
\((4-c_a^2)Q'(c_a)^2=N^2\), whereas
\[
             \frac{e_j(z)}{Q(z)}
                 =\frac{(-1)^j}{S_{j,N}^2Q_{j,N}(z)}.
 \tag{38}
\]
The residue theorem proves (37). Every below-triangle
first normal has been retained in \(\mathscr D\); there
are no poles left at \(a<j\).
In angular coordinates the remaining positive roots have
\(0<\tau_a\le\pi-(2j+1)\pi/N\). They lie precisely in the
original regular factorial order for the shared index \(j\).
This is an exact reduction of the signed source, rather
than a bound on its absolute terms. A global estimate for
the contour in (37) still has to retain both terms of (35).

**Corollary 5.** Fix integer \(n,p\ge3\), and let \(t\)
be the selected angle at the power-\(n\) vertex of their
unit-charge complete-ended internal pair. On a fixed
complex neighborhood of \(t\), through even levels,
\[
 \begin{split}
 \mathscr D_{n,N}(-2\cos z)
   &=\frac{h_{n,N}(-2\cos z)}{Q(-2\cos z)}
                                         (1+O(e^{-\delta N}))\\
   &=(-1)^{N/2}N^{-3/2}a_e(z,0)e^{NS_n(z)}
                                         (1+O(N^{-1}))
 \end{split}
 \tag{39}
\]
for some \(\delta>0\). In particular this original normal
defect is nonzero there for all large even levels. The
same expansion holds with every fixed ordinary spectral
derivative, in the usual differentiated holomorphic sense.

*Proof.* The [pair-to-half-charge comparison](research_pair_half_charge_action_gap.md)
proves both \(H(t)>H_n\) and
\(\Re S_n(t)>M_n\), with a strict quantitative gap.
Both inequalities persist on a fixed neighborhood.
Corollary 4 applies there. Meanwhile (26) and the actual
complete-edge packet give
\[
 \frac{h_{n,N}(-2\cos z)}{Q(-2\cos z)}
  =(-1)^{N/2}N^{-3/2}a_e(z,0)e^{NS_n(z)}
                                         (1+O(N^{-1})).
\]
In (35) the interpolation correction is therefore
exponentially smaller, including its polynomial prefactor.
Cauchy's formula on smaller neighborhoods proves the same
comparison for the normalized holomorphic remainders and
all fixed derivatives. Since \(\sin t\ne0\), passage from
angular to ordinary spectral derivatives is legitimate.
This proves (39). \(\square\)

The local conclusion (39) and the exact global identity
(37) serve different purposes. The former supplies an
independently nonzero source near each geometric pair
angle. The latter still requires control of the complete
integration cycle before yielding a lower bound for the
signed pair coefficient.

## 8. Reproduction

The [focused checker](../experiments/check_complete_source_pick_observation.py)
compares (12) directly with the original physical-value sum at
complex contour points and checks (16). It checks the elementary
rational comparisons used above and records direct original-sum
comparisons with (20), including both signs of \((-1)^{N/2}\).
The asymptotic ratios are finite diagnostics; the uniform
statements are proved analytically above.

~~~sh
python3 experiments/check_complete_source_pick_observation.py
~~~

Its [saved record](../repro/results/research-complete-source-pick-observation.json)
contains the proof and input hashes.
