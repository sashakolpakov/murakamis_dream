# Exact coupled transport of the original upper current

Research deduction, 7 November 2026. The original upper retained
current can be transported along an opposite displacement of the
two imaginary coordinates. Its shared factorial then stays at a
fixed negative height. No shifted factorial or diagonal pole is
introduced. The exact transport retains four boundary faces.

Combining the upper current with its positive retained-side
currents gives a particularly useful version: the retained
boundary faces start at the already paid real cuts. At the left
outgoing face, an exact replacement by the original higher
retained contour also supplies paid initial profiles. This
gives its finite-source bound on every bounded transport
interval. No infinite-height limit or complete right-cap
bound is asserted here.

## 1. Original source and a permissible small upper height

Use the literal row from
[the joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md):
\[
 T_N(s,q)=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+q)
       E_N(a)E_N(q)E_N(s)^3\widehat f_N(q;y).
 \tag{1}
\]
The original cardinal, including its \(1/N\), is
\[
 \widehat f_N(q;y)=
 \frac{e^{-\pi i(N-1)y}}N e^{2\pi iNyq}
       \Pi_N(1-y-1/N)E_N(q-y).
 \tag{2}
\]
All incoming parameters, finite halfweights and external
scalars retain their original values. They are spectators
in the identities below.

Put
\[
 \begin{gathered}
 L_N=\lceil N/8\rceil,\quad M_N=\lceil N/2\rceil-1,\quad
 A=\frac{L_N-1/2}{N},\quad B=\frac{M_N+1/2}{N},\\
 c=9/20,\qquad c<d\le\beta_N=1-\frac1{2N},\qquad
 q_0(z)=z+ih_q,\quad -.102\le h_q\le-.001.
 \end{gathered}
 \tag{3}
\]
The formulas apply whenever this central range and outgoing
interval are nonempty. At \(N=2\) the central range is empty.
The cuts in (3) keep both original parity conventions.

Choose
\[
                      0<h_0<-h_q .
 \tag{4}
\]
For example \(h_0=-h_q/2\) works on the entire actual family.
Let
\[
 K_N^+(s)=\frac{e^{2\pi iNs}}{1-e^{2\pi iNs}},
 \qquad \mathcal F_N(s,q)=T_N(s,q)K_N^+(s),
 \qquad w_N(v)=\frac1{1+e^{2\pi Nv}}.
 \tag{5}
\]
At either retained side,
\[
                     K_N^+(A+iv)=K_N^+(B+iv)=-w_N(v).
 \tag{6}
\]
There is no pole of this kernel at positive height or at
either half-grid endpoint at height zero.

For a fixed \(q=q_0(z)\), define the original positive terms
\[
 \begin{split}
 U_N(h;q)&=N\int_A^B\mathcal F_N(u+ih,q)\,du,\\
 V_{N,+}(h;q)&=
 iN\int_0^h w_N(v)
                 [T_N(B+iv,q)-T_N(A+iv,q)]\,dv.
 \end{split}
 \tag{7}
\]
For positive \(v\), this is precisely the positive part of
the original vertical weight \(w_{N,h_s}\), since the
original main height \(h_s\) is negative.

**Lemma 1.** For any positive \(h_0,h_1\),
\[
 U_N(h_1;q)+V_{N,+}(h_1;q)
                =U_N(h_0;q)+V_{N,+}(h_0;q).
 \tag{8}
\]

Indeed \(\mathcal F_N\) is holomorphic between the two
positive lines. Cauchy's theorem and (6) give, when
\(h_1>h_0\),
\[
 U_N(h_1;q)=U_N(h_0;q)
   -iN\int_{h_0}^{h_1}w_N(v)
                     [T_N(B+iv,q)-T_N(A+iv,q)]\,dv.
 \tag{9}
\]
This proves (8), with its sign. In particular the original
upper height \(5/4\) may be lowered to (4) only together
with this exact change in the positive vertical current.
The lower and nonpositive retained groups are unchanged.

The holomorphy used here is the original global one:
\(\Re(s+a)\) and \(\Re s\) stay in their regular strips;
\(\Pi_N(s+q)\) is holomorphic across its positive support
walls; \(E_N(q)\) and the cardinal retain their global
domains. It is not a statement that the shifted numerator
\(\Pi_N(s+q-1)\) is holomorphic.

## 2. Four faces for the transported horizontal upper current

For \(t\ge0\), write
\[
 s_t(u)=u+i(h_0+t),\qquad q_t(z)=z+i(h_q-t),
 \quad
 I_N(t)=N^2\int_c^d\int_A^B
                    \mathcal F_N(s_t(u),q_t(z))\,du\,dz.
 \tag{10}
\]
The outside \(N^2\) is the original outgoing zero-mode
coefficient times the retained upper-current coefficient.
The cardinal factor \(1/N\) remains inside (1).
Along the entire surface,
\[
                  \Im(s_t+q_t)=h_0+h_q<0.
 \tag{11}
\]
For every finite \(T\), (1) is holomorphic on a neighborhood
of this compact transport surface and its four faces.
The reciprocal real arguments remain below one, the
numerator real arguments stay above \(-1/N\), and the
cardinal argument stays in its original domain.
Equation (11) also keeps the shared factorial away from
every support zero. The kernel stays strictly above its
real lattice poles.

Define the four face integrals, with the displayed
parameters increasing, by
\[
 \begin{split}
 S_{N,B}(T)&=N^2\int_0^T\int_c^d
       \mathcal F_N(B+i(h_0+t),q_t(z))\,dz\,dt,\\
 S_{N,A}(T)&=N^2\int_0^T\int_c^d
       \mathcal F_N(A+i(h_0+t),q_t(z))\,dz\,dt,\\
 Q_{N,d}(T)&=N^2\int_0^T\int_A^B
       \mathcal F_N(s_t(u),d+i(h_q-t))\,du\,dt,\\
 Q_{N,c}(T)&=N^2\int_0^T\int_A^B
       \mathcal F_N(s_t(u),c+i(h_q-t))\,du\,dt .
 \end{split}
 \tag{12}
\]

**Proposition 2.** At every finite \(T\),
\[
 \boxed{\quad
 I_N(0)=I_N(T)-iS_{N,B}(T)+iS_{N,A}(T)
                         +iQ_{N,d}(T)-iQ_{N,c}(T).
 \quad}
 \tag{13}
\]

For a direct orientation check, differentiate (10):
\[
 I_N'(t)=iN^2\left\{
   \int_c^d[\mathcal F_N(s_t(B),q_t(z))
                    -\mathcal F_N(s_t(A),q_t(z))]\,dz
   -\int_A^B[\mathcal F_N(s_t(u),q_t(d))
                    -\mathcal F_N(s_t(u),q_t(c))]\,du
                  \right\}.
 \tag{14}
\]
Here the two terms are \(\partial_s\mathcal F_N\) and
\(-\partial_q\mathcal F_N\), integrated by their respective
variables. Integration in \(t\) proves (13).
No source pole or residue correction occurs.

## 3. Transporting the upper and positive vertical parts together

Let \(\Gamma(h_0)\) be the following oriented retained path:
\[
 A\longrightarrow A+ih_0\longrightarrow B+ih_0
                                      \longrightarrow B .
 \tag{15}
\]
Equation (6) gives exactly
\[
 N\int_{\Gamma(h_0)}\mathcal F_N(s,q)\,ds
                         =U_N(h_0;q)+V_{N,+}(h_0;q).
 \tag{16}
\]
Thus this path includes both positive side integrals with
their original signs; it is not just a horizontal upper line.

Define its transported product current by
\[
 \mathcal I_N(t)=N^2\int_c^d
        \int_{\Gamma(h_0)}
          \mathcal F_N(s+it,z+i(h_q-t))\,ds\,dz .
 \tag{17}
\]
At \(t=0\), (8) and (16) identify it with the complete
original upper-plus-positive-side contribution on \([c,d]\),
at the old upper height \(5/4\).
If a point on (15) has initial height \(v\in[0,h_0]\),
its shared total height during (17) is \(v+h_q<0\).
The whole deformation is therefore in the same holomorphic
original chart. The endpoints at \(t=0\) are half-grid
points, not poles of \(K_N^+\).

For its retained endpoint faces set
\[
 \begin{split}
 \mathcal S_{N,B}(T)&=N^2\int_0^T\int_c^d
                   \mathcal F_N(B+it,q_t(z))\,dz\,dt,\\
 \mathcal S_{N,A}(T)&=N^2\int_0^T\int_c^d
                   \mathcal F_N(A+it,q_t(z))\,dz\,dt .
 \end{split}
 \tag{18}
\]
These faces begin at height zero, rather than at \(h_0\).
For the outgoing faces retain the entire path:
\[
 \mathcal Q_{N,e}(T)=N^2\int_0^T
       \int_{\Gamma(h_0)}
           \mathcal F_N(s+it,e+i(h_q-t))\,ds\,dt,
                         \qquad e=c,d .
 \tag{19}
\]
The exact combined identity is
\[
 \boxed{\quad
 \mathcal I_N(0)=\mathcal I_N(T)
     -i\mathcal S_{N,B}(T)+i\mathcal S_{N,A}(T)
     +i\mathcal Q_{N,d}(T)-i\mathcal Q_{N,c}(T).
 \quad}
 \tag{20}
\]
The proof is again (14), with
\(\int_{\Gamma}\partial_s\mathcal F_N\,ds\) equal to
the difference at the endpoints \(B+it,A+it\).
Corners of the piecewise smooth path create no extra term.

In the original positive-side notation, the retained-face
combination in (20) is
\[
 iN^2\int_0^T\int_c^d w_N(t)
       [T_N(B+it,q_t(z))-T_N(A+it,q_t(z))]\,dz\,dt.
 \tag{21}
\]
For clarity, each integrand of an outgoing face (19) also
retains the vertical pieces:
\[
 \begin{split}
 \int_{\Gamma(h_0)}\mathcal F_N(s+it,q)\,ds
 ={}&\int_A^B\mathcal F_N(u+i(h_0+t),q)\,du\\
 &+i\int_t^{t+h_0}w_N(v)
                [T_N(B+iv,q)-T_N(A+iv,q)]\,dv .
 \end{split}
 \tag{22}
\]
Dropping this second line would change the current and
destroy the cancellation in (8).

## 4. What the phase theorem pays, and which initial data remain

The independent
[support-free shear theorem](research_mixed_fourier_original_upper_shear.md)
applies at every point of these surfaces. For a point
of \(\Gamma(h_0)\) with initial height \(v\), use its
notation \(H=v+t\), \(h=-h_q-v>0\). It gives
\[
 \begin{split}
 &\Re F_\eta(u+i(v+t),a,z+i(h_q-t))-2\pi(v+t)\\
 &\hspace{12mm}\le
 \Re F_\eta(u+iv,a,z+ih_q)-2\pi v-t/20 .
 \end{split}
 \tag{23}
\]
This keeps the original allocation and the exact lifted
output phase. The half-grid deviations of \(A,B\) from
\(1/8,1/2\) cost only bounded factors on fixed compact
height intervals.

For the retained faces in (18), the initial data are
individual real-cut profiles. They already satisfy
\[
 \Re F_\eta(c_s,a,z+ih_q)<B_\eta(\Re a)-1/35000,
       \qquad c_s=1/8,\ 1/2,\quad 9/20\le z\le1,
 \tag{24}
\]
by
[the nonpositive-current deduction](research_mixed_fourier_right_cap_nonpositive_index_corrections.md),
equation (10) and its right-arc transport.
At the actual half-grid cuts use the same \(O(1/N)\)
displacement. On those faces the exact estimate
\[
              |K_N^+(A+it)|=|K_N^+(B+it)|
                   =w_N(t)\le e^{-2\pi Nt}
 \tag{25}
\]
holds including \(t=0\).
Thus (23)--(25), the original finite symbols, and the
prescribed incoming-weight tolerance give a paid upper
envelope for these retained faces on any fixed finite
height interval. This concerns the exact two endpoint
faces, not a free retained real index.

The outgoing faces (19) have different initial data:
\[
      \mathcal F_N(s,e+ih_q),\qquad
                      s\in\Gamma(h_0),\quad e=c,d.
 \tag{26}
\]
Their horizontal part has every \(A\le\Re s\le B\).
The estimate (24) does not control that free index.
An already paid coherent value of the entire path integral
at \(t=0\) does not by itself bound its pointwise profiles
or the full \(t\)-integral in (19). The phase monotonicity
therefore cannot be used to discard either outgoing face.
In particular the left face in (20), at \(e=9/20\),
has the negative sign and retains (22) in full.

All identities above are at finite transport height \(T\).
Passing to \(T=\infty\) requires finite-source tail
estimates for the transported surface and the four
connecting faces, uniformly in the level where needed.
No such passage or bound on a free-index connector is
inferred from a fixed-height symbol.
The construction introduces no shifted-chart residues,
changes no physical support, and retains both parities,
the cardinal \(1/N\), both summation coefficients, and
the original incoming finite weight.

## 5. The left outgoing face has a paid high-contour representation

The free-index issue in (26) can be removed at the left
outgoing endpoint \(c=9/20\) by retaining its complete
oriented path. Put \(H_*=5/4\). For every fixed \(t\ge0\),
Cauchy's theorem gives
\[
 \int_{\Gamma(h_0)}\mathcal F_N(s+it,c+i(h_q-t))\,ds
 =
 \int_{\Gamma(H_*)}\mathcal F_N(s+it,c+i(h_q-t))\,ds .
 \tag{27}
\]
The two translated paths have the same endpoints \(A+it,B+it\).
In the region between them, the shared real argument lies
in a compact subinterval near \([.575,.95]\). The original
\(\Pi_N(s+q)\) is therefore regular even when its height
is positive or zero. All other factorial arguments remain
regular, and the upper Fourier kernel has no pole between
the two paths. Equation (27) does not use the shifted chart
or cross a diagonal residue.

This replacement matters because all initial profiles on
\(\Gamma(H_*)\), at \(q=c+ih_q\), have already been paid.
The original bare inner-contour comparison gives
\[
 \Re F_\eta(u+iH_*,a,c+ih_q)-2\pi H_*
   <\Re F_\eta(u+ih_s,a,c+ih_q)-7/50
   \le B_\eta(\Re a)-7/50 .
 \tag{28}
\]
On its two vertical sides the original positive-alias
comparison bounds the paid rate by its real-cut value,
which has gap \(1/35000\) by (24).
These are individual profile bounds from
[the bare inner-contour proof](research_mixed_fourier_right_cap_bare_inner_contour.md),
Section 3, equation (16) and its following vertical-current
comparison, together with
[its completed real cuts](research_mixed_fourier_right_cap_bare_inner_completion.md).
Their common initial reserve may therefore be taken as
\[
                              \delta_*=\frac1{35000}.
 \tag{29}
\]
The half-grid displacement costs only a bounded factor.

The required shear comparison on this high contour is
stronger than (23), and does not require its total height
to be negative. Fix an initial point \(s=u+iv_0\) with
\(v_0\ge0\), and put
\[
 s_t=u+i(v_0+t),\quad q_t=c+i(h_q-t),\quad
 r=e^{-2\pi(v_0+t)},\quad R=e^{2\pi(h_q-t)}<1 .
 \tag{30}
\]
For the original regular-strip branches the shared derivative
again cancels. With \(A_\rho\) as in the support-free shear
proof, exactly
\[
 \begin{split}
 P_c&=2\pi+\Im(F_{\eta,s}-F_{\eta,q})\\
 &=4\pi u-\phi+3A_r(u)
   -A_{r e^{-2\pi h_a}}(u+x)
          +A_R(c)+A_{\rho R}(c-\xi).
 \end{split}
 \tag{31}
\]
Both last arguments are nonnegative, because
\(0<c<1/2\) and \(0<c-\xi<1/2\). No comparison between
\(r\) and \(R\) is needed.

The previously proved monotonicity in \(u\) and the incident
bound give
\[
 P_c\ge\pi/2-\phi+3b(r)-\arctan t_r,\qquad
 b(r)=\arctan\frac{r}{\sqrt2-r},\quad
 t_r=\frac{5r}{3(1+r)}.
 \tag{32}
\]
On \(0\le r\le1\),
\[
 b'(r)=\frac{\sqrt2}{2-2\sqrt2r+2r^2}
       \ge\frac1{\sqrt2}>\frac7{10}.
 \tag{33}
\]
Indeed its denominator is at most two on this interval.
Thus \(3b(r)>21r/10\) for \(r>0\), while
\(\arctan t_r\le t_r\le5r/3\). Since
\(\pi/2-\phi>1/3\), (32) proves
\[
                         P_c>1/3 .
 \tag{34}
\]
In particular, for every initial height \(v_0\ge0\),
\[
 \begin{split}
 &\Re F_\eta(u+i(v_0+t),a,c+i(h_q-t))-2\pi(v_0+t)\\
 &\hspace{8mm}\le
 \Re F_\eta(u+iv_0,a,c+ih_q)-2\pi v_0-t/3 .
 \end{split}
 \tag{35}
\]
Every argument in this calculation has its original real
part in \((0,1)\), including \(s+q\). Positive total
imaginary height is therefore harmless here.

On the high horizontal piece of \(\Gamma(H_*)+it\),
\[
 |K_N^+(s)|\le
        \frac{e^{-2\pi N(H_*+t)}}{1-e^{-2\pi NH_*}}.
 \tag{36}
\]
On its vertical sides the exact half-grid identity instead
gives \(|K_N^+(s)|\le e^{-2\pi N(v_0+t)}\), including
the bottom endpoints \(v_0=t=0\).
Equations (28)--(36), the original uniform compact-strip
symbols, and the incoming rate-tolerance bound give a
finite-source consequence:
for every fixed \(T<\infty\), eventually at both parities,
\[
 |d_N(X)|^{\eta/2}N^2\int_0^T
   \left|\int_{\Gamma(h_0)}
       \mathcal F_N(s+it,c+i(h_q-t))\,ds\right|dt
       \le e^{N(B_\eta(\Re a)-1/70000)} .
 \tag{37}
\]
For the proof first use the exact equality (27). On the
high contour, each source profile has rate at most
\(B_\eta-\delta_*-t/3\). Choose one tolerance less than
\(\delta_*/4\), absorb the fixed contour lengths and all
polynomial factors, and retain the gap \(\delta_*/2\).
The actual half-grid arguments remain in a fixed regular
neighborhood on each such bounded transport interval.

This proves a bound for the complete left outgoing face
on every fixed finite interval. It does not infer a
pointwise bound on the original small-height free-index
profiles. The equality of the complete paths is essential.
Uniform tail estimates are still needed before replacing
\(T\) by infinity in (37). The right outgoing face retains
its separate source comparison and exact orientation in
(20).
