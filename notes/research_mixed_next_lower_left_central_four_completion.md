# Complete central lower-left source for a next type four

Private research proof, 8 November 2026. The complete cap and both
complete own-four conditional kernels satisfy the original next
supporting-plane bound when the first incoming coordinate is on
its central interval and the shared coordinate lies on the full
lower-left interval, at its actual negative height. The last
remaining double-last profile is controlled at the maximum of
its shared factorial weight.

Every physical row, both parities, all conditional contour currents
and the full forced Fourier weight are retained. This theorem is
ordinary-next and central-first only. It does not estimate the
noncentral first-incoming pieces, the other outgoing intervals,
or a complete next own-three block. Section 4 separately proves
the double-last comparison for either next own type, with the
positive outgoing carrier retained. No numerical evaluation is used.

## 1. The actual finite source and the completed reduction

Use exactly the actual ordinary references and allocations of
[the first-last reduction](research_mixed_next_lower_left_first_last_four_reduction.md).
Write
\[
\begin{gathered}
a=x+ih_a,\quad y=q+ih_y,\quad z=u+ih_z,\\
x,u\in P=[11/50,9/20],\qquad 0\le q\le11/50,\\
-.072<h_a<0,\quad -.102<h_y<-.001,\quad -.108\le h_z<0,\\
X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},
\quad R=e^{2\pi h_y}\in(13/25,1).
\end{gathered}
\tag{1}
\]
The first and next conditional factors are both the original
\[
C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},
\qquad r=e^{-2\pi i/N},\quad P_j=(r;r)_j.
\tag{2}
\]
Keep the complete cap \(U_{0,N}(w,X)\), the complete polynomial
\(d_N(Y)\), and the original outgoing allocation
\(|d_N(Z)|^{1/2}\). Set
\[
\delta_a=-2\pi h_a,\qquad \delta_y=-2\pi h_y,
\qquad \nu_R(q)=-\Re g(q+ih_y).
\tag{3}
\]
The preceding finite-source reduction proves, for arbitrarily
small fixed \(\tau>0\),
\[
\begin{split}
&|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{1,N}(Y,Z)|
                                      |d_N(Z)|^{1/2}\\
&\quad\le C_\tau N^{B_\tau}
 \left[e^{N\{\Lambda_{123}(z)-10^{-11}\}}
                  +e^{N\{\mathcal B_{\rm LL}(x,q,u)+\tau\}}\right],\\
\mathcal B_{\rm LL}(x,q,u)
&=B_U(x)+\delta_a+\delta_y+\nu_R(q)-\tfrac12\Re g(z).
\end{split}
\tag{4}
\]
Here \(B_U\) is the original complete cap plane and
\(\Lambda_{123}\) is the original next plane. In particular
\(\Lambda_{123}(z)\) has no target \(q\) dependence.
The two remaining raw endpoint carriers in (4) are exactly
\(\delta_a,\delta_y\); neither Fourier halfweight was dropped.

We also use a phase consequence, not an inference from a signed
sum, of [the next-four last-row proof](research_mixed_next_lower_left_next_four_last_row.md),
Sections 2--3. Uniformly on (1), the first **real low cut**
paired with the next last-row alternative obeys
\[
B_U(x)+E_1(1/8;a,y)+\delta_y
             -\Re g(y)-\tfrac12\Re g(z)
<\Lambda_{123}(z)-10^{-10}.
\tag{5}
\]
The exact real-row rate is
\[
E_1(t;a,y)=I_a(t)+I_y(t)-3J(t)+\delta_a t,
\qquad
I_b(t)=\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv.
\tag{6}
\]
The cited proof covers all shared radii: joint transport is used
below \(7/10\), and same-point next-low domination above it.
It uses the old last-row certificate only for its sign. Its
quantitative deficit is supplied by the original quadratic
support losses and real-cut comparisons.

## 2. Maximize only the common factorial weight

The original lower-half primitive gives
\[
\nu_R'(q)=-\log|1-Re^{-2\pi iq}|.
\tag{7}
\]
On \(0\le q\le11/50\), the squared modulus in (7) is
strictly increasing in \(q\). It equals one exactly at
\[
q_R=\frac{1}{2\pi}\arccos(R/2),
\qquad \frac16<q_R<\frac{11}{50}.
\tag{8}
\]
For the lower endpoint use \(R<1\). For the upper endpoint,
\(R/2>1/4\) whereas
\(\cos(11\pi/25)=\sin(3\pi/50)<1/5\).
Thus \(\nu_R\) increases up to \(q_R\) and decreases
after it. In particular
\[
             \mathcal B_{\rm LL}(x,q,u)
                \le\mathcal B_{\rm LL}(x,q_R,u).
\tag{9}
\]
All reference parameters and heights are held fixed in this
comparison. The intermediate target \(q_R\) lies in the
already established source interval; it is not asserted to be
an image of a moving critical map.

Set \(y_R=q_R+ih_y\). For \(0\le v\le1/8\),
\[
q_R+v<11/50+1/8=69/200<1/2.
\]
Its cosine decreases as \(v\) increases. Since the squared
modulus at \(v=0\) is exactly one by (8),
\[
                         I_{y_R}(1/8)\ge0.
\tag{10}
\]
There are no product zeros on this arc.

For the other factor, the original incoming radius satisfies
\(R_a=e^{2\pi h_a}>5/8\). This is the original
\(e^{-2\pi h_a}<8/5\) height witness retained in the
joint profile theorem. On \(x+v\in[.22,.575]\),
\(\cos(2\pi(x+v))<1/5\). The squared modulus increases
with its radius above \(5/8\), and therefore
\[
|1-R_a e^{-2\pi i(x+v)}|^2>
1+\frac{25}{64}-\frac14=\frac{73}{64}>1.
\]
Consequently
\[
                              I_a(1/8)>0.
\tag{11}
\]

The elementary sine-integral estimate already proved in the
next-four last-row note gives \(-J(1/8)>3/20\).
Also \(\delta_a<18\pi/125\). Equations (6),(10),(11)
therefore yield
\[
\begin{split}
E_1(1/8;a,y_R)-\delta_a
&=I_a(1/8)+I_{y_R}(1/8)-3J(1/8)-\tfrac78\delta_a\\
&>\frac9{20}-\frac{63\pi}{500}
 >\frac{27}{500}.
\end{split}
\tag{12}
\]
The last comparison uses only \(\pi<22/7\).
Every constant and carrier in (12) belongs to the original
real row. No asymptotic action has been evaluated.

Combining (5),(9),(12) proves the uniform strict comparison
\[
\boxed{\qquad
\mathcal B_{\rm LL}(x,q,u)
 <\Lambda_{123}(z)-\frac{27}{500}-10^{-10}.
\qquad}
\tag{13}
\]
In particular this does not spend any part of an unspecified
typed last-row margin.

## 3. Complete central finite consequence

Choose the total finite tolerance in the second term of (4)
inside (13). The first term is already paid. Thus, uniformly
on the actual ordinary-next-four family and (1), at both
level parities and for every real ordinary color \(w\),
\[
\boxed{\quad
|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{1,N}(Y,Z)|
                         |d_N(Z)|^{1/2}
\le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}}.
\quad}
\tag{14}
\]
This contains both complete conditional sums (2), not just
their retained lower halves. Their physical upper blocks,
zero rows, last-index neighborhoods, all horizontal aliases,
weighted vertical sides and unweighted joins were included
in (4). The exact factorial seam continuation controls the
canonical row interpolants at \(q=0\); the complete forced
upper bound for \(d_N\) is used separately there.

The integral over the central first-incoming interval retains
its original measure \(+N\int_{P+ih_a}da\), and therefore
has the same exponential deficit. Fixed real-color derivatives
cost only powers of \(N\). For local normalized mixed jets,
retain the original integer-weight holomorphic square, keep
all base paths and cuts fixed, and use smaller outside
neighborhoods. The normalized deficit may be taken as
\(10^{-12}\). The auxiliary maximizer \(q_R\) is used only
in a real upper comparison and is not differentiated.

The result applies to the original complete central prefix
source. No cardinal correction is silently added or removed.
Noncentral first-incoming paths still need their own bounds
on this lower-left interval. Next own type three, the remaining
outgoing pieces and the complete paired transfer are separate
obligations. Equation (14) alone asserts no new knot-family
asymptotic.

## 4. The double-last comparison holds for either next own type

This final profile lemma also allows \(\beta=0\), with its
actual ordinary-next references and \(|h_z|\le.108\). All
other target ranges in (1) remain unchanged. For \(\beta=1\),
retain \(h_z<0\) as before. Define the exact next last-row rate
and the fully allocated double-last profile by
\[
\begin{split}
L_\beta&=\delta_y+2\pi(h_z)_+,\\
\mathcal B_{{\rm LL},\beta}
 &=B_U(x)+\delta_a+L_\beta-\Re g(y)
                                      -\tfrac\beta2\Re g(z).
\end{split}
\tag{15}
\]
When \(\beta=0\), the last allocation in (15) is absent;
the positive-height carrier is not omitted.

Consider the original first real low cut paired with this next
last row:
\[
\mathcal A_\beta(q)=B_U(x)+E_1(1/8;a,y)+L_\beta
                           -\Re g(y)-\tfrac\beta2\Re g(z).
\tag{16}
\]
Its exact derivative is
\[
\mathcal A_\beta'(q)=
\log|1-Re^{-2\pi i(q+1/8)}|-2\log|1-Re^{-2\pi iq}|>0.
\tag{17}
\]
The strict sign on all \(0\le q\le11/50\),
\(1/2\le R\le1\), is precisely the elementary four-range
calculation in Section 3 of the first-last reduction. That
calculation concerns the displayed ratio itself, so it does
not impose an own-type condition here. In particular neither
\(L_\beta\) nor the outgoing allocation has a \(q\) derivative.

At \(q_0=11/50\), the actual first real-low certificate has
deficit \(1/2000\); the next last-row certificate gives its
strict supporting-plane sign for both own types and all original
revived carriers. Adding the cap and canceling the matched
marginals therefore gives
\(\mathcal A_\beta(q_0)<\Lambda_{123}(z)-1/2000\).
This calibration uses the appropriate actual ordinary reference
family in each case. Equation (17) transports it through the
whole interval.

The only \(q\) dependence of (15) is still \(\nu_R(q)\).
The maximizing argument (8)--(12), involving only the original
first cut and its negative-height inputs, is unchanged. Hence
\[
\boxed{\qquad
\mathcal B_{{\rm LL},\beta}(x,q,u)
<\Lambda_{123}(z)-\frac1{2000}-\frac{27}{500}
=\Lambda_{123}(z)-\frac{109}{2000},
\qquad\beta=0,1.
\qquad}
\tag{18}
\]
This is a full-interval comparison for the specified double-last
profiles. For \(\beta=1\) it strengthens (13). For \(\beta=0\)
it does not establish the missing physical upper-row reduction
or the other first-last/next-current combinations, and therefore
does not promote (14) to a complete next-own-three theorem.
