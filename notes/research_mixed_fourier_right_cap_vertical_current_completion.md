# Payment of the complete outgoing vertical current

Research completion, 7 November 2026. The entire real-endpoint
vertical current of the low retained Fourier right cap has an
exponential gap below its original supporting plane. The proof
keeps the central retained sum coherent: each of its exact retained
contour profiles is dominated by the corresponding paid real-seam
profile. The physical low rows and infinite vertical tails have
their own previously proved absolute estimates.

The unweighted right-end return is also paid. These results do
not bound any remaining correction of the outgoing horizontal
main path and do not assert noncancellation of the whole cap.
No new numerical evaluation is used.

## 1. Original source, real-endpoint identity and paid seam

Keep the original correlated references, incoming targets and
unselected allocation of
[the completed left-taper source](research_mixed_fourier_left_taper_source_completion.md).
In particular \(a=x+i h_a\), \(x\in P=[11/50,9/20]\),
\(\eta\in\{0,1\}\), and the plane is
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                         -\kappa(x-\Re a_*)^2,
 \qquad\kappa=1/2500000.
 \tag{1}
\]
The outgoing parameter is the original \(y=\xi+i\upsilon=x_0\),
\(Y=e^{2\pi iy}=\rho e^{i\phi}\), with
\[
 3/5<\rho<5/8,\qquad 8/7<\phi<7/6,\qquad
                       \upsilon>0.
 \tag{2}
\]
Use \(X=e^{-2\pi ia}\),
\[
 \begin{gathered}
 M_N=\lceil N/2\rceil-1,\quad L_N=\lceil N/8\rceil,\quad
 \alpha_N=-1/(2N),\quad\beta_N=\alpha_N+1,\\
 C_N^<(X,Z)=\sum_{j=0}^{M_N}
                  \frac{X^{-j}p_j(X)p_j(Z)}{P_j^3},\qquad
 S_N^<(q)=C_N^<(X,e^{-2\pi iq})\widehat f_N(q;y).
 \end{gathered}
 \tag{3}
\]
Every factor in (3) is the literal original finite factor.
The cardinal is the global factorial-suffix interpolation.

The proved exact real-endpoint regrouping is
\[
 V_N^<
   =N\int_\Gamma S_N^<(q)\,dq
      +iN\int_{\mathbb R}w_{N,0}(v)
           [S_N^<(\beta_N+iv)-S_N^<(\alpha_N+iv)]\,dv,
 \qquad
 w_{N,0}(v)=\frac1{1+e^{2\pi Nv}}
                           -\boldsymbol1_{\{v<0\}} .
 \tag{4}
\]
The bent path \(\Gamma\) has its true endpoints on the real
axis. The old unpenalized negative-height join remains part
of this exact main path; it has not been discarded.
The useful global bound is
\[
                         |w_{N,0}(v)|\le e^{-2\pi N|v|}.
 \tag{5}
\]

The successful fixed taper certificate discharges the sole
premise of
[the retained seam contour](research_mixed_fourier_real_seam_contour.md).
That theorem bounds each central retained contour group by
the raw rate \(B_\eta-3/400\), with all inner alias debits
and joins included. Its seam phase is
\[
 \Psi_\eta(s,a)=g(s+a)-2g(s)-(1+\eta/2)g(a)
                                      +2\pi ias-\pi iy .
 \tag{6}
\]
The physical low rows \(j<L_N\) have the stronger raw bound
\[
 E_\eta^0(j/N;a)
            <B_\eta(x)-3/400-1/35000.
 \tag{7}
\]
Neither assertion is inferred from the modulus of a
canceled finite sum.

## 2. The exact interpolation at both outgoing endpoints

Set \(q_L=\alpha_N+iv\), \(q_R=q_L+1\). For the retained
variable use the same holomorphic interpolation at both ends:
\[
 \mathcal R_N(s,q_L;a)=
 e^{2\pi iNas}\Pi_N(s+a)E_N(a)
                  \Pi_N(s+q_L)E_N(q_L)E_N(s)^3,
 \qquad E_N=1/\Pi_N.
 \tag{8}
\]
At every physical retained \(s=j/N\), (8) is exactly
\(X^{-j}p_j(X)p_j(e^{-2\pi iq_L})/P_j^3\).
Since that polynomial has identical arguments at \(q_L\)
and \(q_R\), the two exact central summands are interpolated
by
\[
 \mathcal F_N^L(s,v)=\mathcal R_N(s,q_L;a)\widehat f_N(q_L;y),
 \qquad
 \mathcal F_N^R(s,v)=\mathcal R_N(s,q_L;a)\widehat f_N(q_R;y).
 \tag{9}
\]
This uses physical polynomial periodicity before interpolation.
It does not assert that replacing \(q_L\) by \(q_R\) in
every factorial of (8) leaves an off-grid function unchanged.
No cardinal or monodromy factor is divided out.

For either function in (9), apply the exact four-group retained
contour with cuts
\[
 \sigma_-=(L_N-\tfrac12)/N,\qquad
 \sigma_+=(M_N+\tfrac12)/N
 \tag{10}
\]
and heights \(h_-=-1/5\), \(h_s=\Im s_*\), \(h_+=5/4\).
The groups are the same \(Z_N,L_N,U_N,V_N\) as in
equation (17) of the left-taper completion: one zero mode,
both complete horizontal aliases, and the signed vertical
difference with \(w_{N,h_s}\).
Their sum is exactly the central physical sum
\(L_N\le j\le M_N\). Every group retains its \(+N\);
the outer current in (4) adds its own \(iN\).
The cardinal \(1/N\) is already contained in (9).

For every fixed finite \(H\), these retained rectangles are
holomorphic uniformly for \(|v|\le H\). Indeed all
\(s+q_L\) real parts remain in a compact subinterval of
\((0,1)\) for large \(N\), as do \(s\) and \(s+a\).
The exact reciprocal endpoint factor satisfies
\[
 |E_N(\alpha_N+iv)|
       =\sqrt{\frac{1+e^{2\pi Nv}}N}
       \le\sqrt{2/N}\,e^{\pi Nv_+}.
 \tag{11}
\]
This is the original Gamma reflection identity, valid
including \(v=0\).

## 3. A global comparison of the individual contour profiles

Let \(g_-\) denote the original lower-half-plane disk primitive.
The proved cardinal upper rates from
[the real-endpoint vertical envelope](research_mixed_fourier_real_endpoint_vertical_envelope.md)
are
\[
 \begin{split}
 K(v)&=\pi\upsilon-\phi v+\Re g(1-y)
             -\Re g_-(-\xi+i(v-\upsilon)),
                                      &&v\le\upsilon,\\
 K(v)&=D_++\pi v
             -\Re g_-(-\xi-i(v-\upsilon)),
                                      &&v\ge\upsilon,\\
 D_+&=\Re g(1-y)-2\pi\xi\upsilon,\qquad K(0)=\pi\upsilon .
 \end{split}
 \tag{12}
\]
These expressions agree continuously at \(v=\upsilon\).
They are uniform finite-source upper rates on every fixed
compact vertical interval, with polynomial prefactors.
They remain valid through the possible cardinal zeros on
that height line: their proof uses the finite numerator
product and a nonzero regular denominator, not a lower
bound for the vanishing numerator.
The right cardinal has upper rate
\[
                         K_R(v)=K(v)-2\pi\max(\upsilon,v)
                                  \le K(v).
 \tag{13}
\]

For a retained contour point \(s=u+ih\), put
\[
             \Delta_s(v)=\Re[g(s+iv)-g(s)] .
 \tag{14}
\]
The simple all-height bound
\[
        0\le\Im g'(u+i t)\le\pi(1-2u),
                    \qquad 1/8\le u\le1/2,\ t\in\mathbb R,
 \tag{15}
\]
uses the original regular-strip argument of
\(1-e^{2\pi t-2\pi iu}\).
Integration gives
\[
 \Delta_s(v)\le0\quad(v\ge0),\qquad
 \Delta_s(v)\le(3\pi/4)|v|\quad(v\le0).
 \tag{16}
\]
These statements hold at every retained contour height,
including the upper horizontal alias and all vertical joins.

After inserting (5) and (11), the change from the allocated
seam profile to a left-endpoint paid profile is at most
\[
 \Lambda_s(v)=\Delta_s(v)+K(v)-K(0)+\pi v_+-2\pi|v|.
 \tag{17}
\]
The right profile has the further nonpositive change in
(13). The following estimates show that (17) never exceeds
zero:
\[
 \boxed{\quad
 \begin{array}{ll}
 \Lambda_s(v)\le-(3\pi/4-\phi)|v|,&v\le0,\\[2pt]
 \Lambda_s(v)\le-(\pi+\phi)v,&0\le v\le\upsilon,\\[2pt]
 \Lambda_s(v)<-1/25,&v\ge\upsilon.
 \end{array}
 \quad}
 \tag{18}
\]

For the first two intervals, differentiating the first
line of (12) gives
\[
              -\phi-\pi/2<K'(v)<-\phi
                                  \qquad(v<\upsilon).
 \tag{19}
\]
Indeed its logarithmic argument lies in the lower
half-plane and has positive real part when \(v<\upsilon\).
At the boundary the needed limits follow continuously.
Combining (19) with (16) proves the first two lines of
(18), and \(3\pi/4-\phi>0\) follows from \(\phi<7/6\).

For \(v\ge\upsilon\), equations (12), (16), and (17)
give
\[
 \Lambda_s(v)\le D_+-\pi\upsilon
                       -\Re g_-(-\xi-i(v-\upsilon)).
 \tag{20}
\]
The old vertical-tail proof gives
\[
 D_+<85/576,\qquad
 \pi\upsilon>77/400,\qquad
             \pi\upsilon-D_+>647/14400>1/25.
 \tag{21}
\]
The remaining real primitive is nonnegative, and positive
at every finite height. Explicitly it is
\(\Im\operatorname{Li}_2(r e^{i\phi})/(2\pi)\),
where \(0<r\le1\). Its radial derivative is
\(-\arg(1-r e^{i\phi})/(2\pi r)>0\), and its value at \(r=0\)
is zero. This proves the last line of (18).

At the finite half-grid cut \(\sigma_-\), the real coordinate
may be \(O(1/N)\) below \(1/8\). On \(|v|\le H\) the
resulting change in (16) is \(O(H/N)\), and every other
profile displacement is \(O(1/N)\) on fixed regular strips.
They are absorbed into a uniform finite prefactor. The
upper cut never exceeds \(1/2\). No asymptotic argument
is used to remove a physical row.

## 4. Finite-source proof for the whole vertical current

Fix \(H\) as in
[the uniform vertical-tail theorem](research_mixed_fourier_vertical_tail_payment.md),
enlarging it if necessary so that \(H>|h_q|\).
On \(|v|\le H\), the uniform original factorial symbols
and the zero-safe cardinal estimates in (12)--(13) give,
for each exact retained contour in (9), its seam phase
plus (17), with one aggregate source tolerance and a
polynomial prefactor. The midpoint factor (11) is exact.
Thus (18) transfers the paid raw seam loss \(3/400\)
to every such contour profile.

The inner alias Fourier debits and vertical weights are
unchanged in this comparison, since they depend on \(s\),
not on \(v\). The seam theorem already paid those complete
profiles, including its unpenalized retained joins.
We may therefore bound each retained contour integral,
and only then its exact coherent central sum. This proves
the compact-\(v\) estimate without taking the modulus of
the central physical retained rows separately.

For \(j<L_N\), the real-endpoint vertical envelope bounds
the entire absolute physical-row current, including both
outgoing endpoints, by its real-seam rate. Bound (7)
therefore pays these rows on the full vertical line.
This step remains distinct from the central retained
contour argument.

Choose an aggregate tolerance less than \(1/1000\).
All polynomial factors, the two \(N\) coefficients and
the fixed lengths of the compact contours are absorbed
for sufficiently large \(N\). The compact outgoing
current has finite gap \(1/1000\). The two infinite
tails already have finite gap \(1/100\).
On those tails \(w_{N,0}=w_{N,h_q}\), so the cited
tail estimate applies without any change of source.
Adding the three parts yields the following.

**Theorem 1.** Uniformly on the original actual reference
families and incoming targets, for all sufficiently large
\(N\) of either parity,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}N\int_{\mathbb R}|w_{N,0}(v)|
       \bigl(|S_N^<(\beta_N+iv)|
                    +|S_N^<(\alpha_N+iv)|\bigr)\,dv
             \le e^{N(B_\eta(x)-1/2000)}.
 \quad}
 \tag{22}
\]
In particular (22) bounds the modulus of the signed
vertical current in (4). The absolute value inside
(22) is taken after the retained \(C_N^<\) sum.
It is not a termwise bound for its central physical rows.
The incoming finite weight is never divided out.

## 5. The unweighted right endpoint return

The vertical return from \(\beta_N+i h_q\) to \(\beta_N\)
does not carry \(w_{N,0}\), so it requires a separate
comparison. It is paid by the right cardinal decrement.

For \(h_q\le v\le0\), the disk in the logarithm defining
(19) has radius at most \(\rho<5/8<1/\sqrt2\).
Its argument has modulus less than \(\pi/4\). Thus
\[
 K(v)-K(0)\le(\phi+\pi/4)|v|.
 \tag{23}
\]
Combining this with (16), the midpoint factor (which has
zero rate when \(v\le0\)), and (13), the change of an
unweighted right retained profile from its seam profile
is at most
\[
              (\pi+\phi)|v|-2\pi\upsilon<-1/50 .
 \tag{24}
\]
Here no numerical value is needed:
\[
 2\pi\upsilon=-\log\rho>\log(8/5)>6/13,
 \qquad
 (\pi+\phi)|h_q|
 <(22/7+7/6)\frac{51}{500}
 =\frac{9231}{21000},
 \tag{25}
\]
and \(6/13-9231/21000>1/50\).
The logarithmic lower bound follows from
\(\log(8/5)=2\operatorname{arctanh}(3/13)>6/13\).

For the physical low retained rows use the previously proved
negative-\(v\) envelope
\[
 L(u,v)\le L(u,0)+(\pi-\phi)v,\qquad v\le0 .
 \tag{26}
\]
Restoring its outgoing Fourier debit and applying the
right cardinal decrement gives the same upper change
\((\pi+\phi)|v|-2\pi\upsilon\).
Thus the physical low rows and every coherent central
retained contour are both paid on this unweighted return.

After polynomial absorption, a convenient common statement is
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}N
       \int_{h_q}^{0}|S_N^<(\beta_N+iv)|\,dv
                  \le e^{N(B_\eta(x)-1/200)} .
 \quad}
 \tag{27}
\]
It holds with all original scalar, parity and allocation
conventions. Its proof uses (9) and the uniform right
cardinal upper bound, including any zeros, rather than
division by a monodromy denominator.

Equations (22) and (27) remove the complete outgoing
vertical source and this right-end connector from the
list of unpaid terms. The separate main-path estimates
and any retained corrections over portions of that path
must still be assembled with their own original source
domains. No lower bound or complete right-cap
noncancellation is asserted by this note.
