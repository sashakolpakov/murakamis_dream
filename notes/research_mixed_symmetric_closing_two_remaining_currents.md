# The symmetric closing sum with two connecting currents retained

Private finite-source assembly, 9 November 2026. The original
symmetric \(343\) closing has a nonzero geometric contribution
on a full middle segment of its deformed contour. Its far
physical samples, all their first derivatives, and its short
endpoint currents are exponentially smaller. Two connecting
currents remain explicitly in the identity.

The theorem below does not bound those two currents. In
particular it is not a volume asymptotic for the closed knot.
Its purpose is to specify exactly which finite functions and
contour pieces still require estimates.

## 1. Original functions and geometric normalization

Use the complete inner function
\[
 Q_N(w,u)=\phi_N\!\left[
 R_N^3\mathcal K_N(w,x)\mathcal K_N(x,-2\cos u)\right],
 \qquad
 \phi_N(f)=(-1)^{N-1}N^2[x^{N-1}]
               \operatorname{rem}_{2T_N(x/2)+2}f .
 \tag{1}
\]
Both edge kernels are complete, with all \(N\) original Newton
rows. For \(\mathbf w=(w_L,w_R)\), write
\[
 \begin{split}
 F_N(u;\mathbf w)&=Q_N(w_L,u)Q_N(w_R,u),\\
 G_N(u;\mathbf w)&=\sin u\,F_N(u;\mathbf w)e^{iNu^2/\pi},\\
 W_N(u)&=\frac{e^{-iNu}}
          {(1-(-1)^{N-1}e^{-iNu})^2},\\
 C_{N,n}&=e^{\pi i n(N-1)^2/(4N)} .
 \end{split}
 \tag{2}
\]
Let \(Z_N(\mathbf w)\) be the original \(R_N^4\) trace of the
product of the two ordinary polynomials \(Q_N\), as in equation
(4) of the [exact closing identity](research_mixed_symmetric_343_closing_trace_and_domain.md).
In particular the ordinary outgoing product has degree at most
\(2(N-1)\); it is not replaced by its values at distinct roots.

The actual geometric point is
\[
 u_g=\beta_g-iK_g,\qquad
 2\pi/5<\beta_g<\pi/2,\quad17/30<K_g<7/10.
 \tag{3}
\]
Retain \(S(w,u)\) and \(A(w,u)\) from the
[complete incoming-color theorem](research_mixed_symmetric_closing_incoming_neighborhood.md).
The [local outer theorem](research_mixed_symmetric_closing_local_outer_packet.md)
defines, on a fixed bidisk about \((-2,-2)\),
\[
 \begin{split}
 \Xi(u;\mathbf w)&=S(w_L,u)+S(w_R,u)+iu^2/\pi-iu,\\
 \Xi_u(u_*(\mathbf w);\mathbf w)&=0,\qquad
 u_*(-2,-2)=u_g,\\
 \Theta(\mathbf w)&=\Xi(u_*(\mathbf w);\mathbf w),\\
 B(\mathbf w)&=
 i\sqrt{\frac2\pi}\,
 \frac{\sin u_*(\mathbf w)\,
       A(w_L,u_*(\mathbf w))A(w_R,u_*(\mathbf w))}
      {\sqrt{-\Xi_{uu}(u_*(\mathbf w);\mathbf w)}}\ne0 .
 \end{split}
 \tag{4}
\]
The square root has the orientation of the increasing horizontal
Gaussian contour. Put \(M_g=\Re\Theta(-2,-2)>307/100\).
No action constant or crossing scalar is changed here.

## 2. A full middle segment

Choose the fixed \(\eta>0\) of the
[central polynomial bound](research_mixed_symmetric_closing_center_bridge.md),
and put
\[
 \Gamma_{\mathrm{mid}}
      =[-\eta-iK_g,\ \pi/2-iK_g],
 \tag{5}
\]
oriented from left to right. Define its exact contribution
\[
 I_N(\mathbf w)
   =-\frac{N^2C_{N,4}}{\pi i}
         \int_{\Gamma_{\mathrm{mid}}}
                    G_N(u;\mathbf w)W_N(u)\,du .
 \tag{6}
\]

**Lemma.** On a fixed bidisk about \((-2,-2)\), uniformly at
both parities,
\[
 I_N(\mathbf w)
 =C_{N,4}C_{N,3}^{\,2}N^{-3/2}
       B(\mathbf w)e^{N\Theta(\mathbf w)}
                      (1+O_{\mathrm{hol}}(N^{-1})).
 \tag{7}
\]
Every fixed ordinary mixed derivative of the normalized
relative error is \(O(N^{-1})\) on smaller bidisks.

*Proof.* Take the fixed local interval \(J_g\) used in the local
outer theorem, shrinking it if necessary so it is strictly
inside the positive part of (5). That theorem estimates its
literal integral with the full \(W_N\) and gives (7) for that
piece, with precisely the coefficient (4).

On the remaining positive segment, the
[horizontal concavity theorem](research_mixed_symmetric_closing_horizontal_concavity.md)
gives, at complete colors,
\[
 \Re\Xi(a-iK_g;-2,-2)
 \le M_g-\frac{(a-\beta_g)^2}{8\pi}.
 \tag{8}
\]
The compact complement of \(J_g\) in \(0\le a\le\pi/2\)
therefore has a fixed strict gap. The complete inner
asymptotic is uniform there, including both endpoint angles.
Continuity of \(S(w,u)\) on this compact set preserves a
fixed gap when both incoming colors lie in a sufficiently
small bidisk. Using the exact estimate
\[
 |e^{iN(a-iK_g)^2/\pi}W_N(a-iK_g)|
 \le\frac{e^{N(2aK_g/\pi-K_g)}}{(1-e^{-NK_g})^2}
 \tag{9}
\]
then bounds the absolute positive remainder.
The central polynomial bound supplies the strict gap on
\(-\eta\le a\le0\), uniformly on an incoming bidisk.

Intersect these fixed bidisks and shrink once more so that
\(|\Re\Theta(\mathbf w)-M_g|\) is less than one fourth of
the smaller of those two remainder gaps. After polynomial
factors are absorbed, their total absolute integral,
including the original prefactor, is
\[
                  O(e^{N(\Re\Theta(\mathbf w)-g)})
                  \quad\text{for some fixed }g>0 .
 \tag{10}
\]
Since \(B\) stays away from zero, (10) is exponentially
small relative to the local term, proving (7).
The final normalized error is holomorphic on a fixed
bidisk because the contour in (5) has fixed endpoints.
Cauchy's formula gives the stated derivatives.
\(\square\)

## 3. The two exact connecting currents

Use the actual midpoint cut and short height from the
[far-boundary theorem](research_mixed_symmetric_closing_far_boundary_payment.md):
\[
 m_N=\lfloor N/400\rfloor,\qquad
 a_N=\pi-\frac{2\pi m_N}{N},\qquad
 0<h_c\le1/1000 .
 \tag{11}
\]
For all sufficiently large \(N\), \(a_N>\pi/2\).
The height \(h_c\) is fixed and is less than \(K_g\).
Define two oriented polygonal paths by listing their vertices:
\[
 \begin{split}
 \Gamma_{L,N}:&
 \quad -a_N-ih_c,\quad -a_N-iK_g,\quad-\eta-iK_g,\\
 \Gamma_{R,N}:&
 \quad \pi/2-iK_g,\quad a_N-iK_g,\quad a_N-ih_c .
 \end{split}
 \tag{12}
\]
Every segment remains strictly in the lower half-plane.
Their exact currents are
\[
 \mathcal C_{\sigma,N}(\mathbf w)
 =-\frac{N^2C_{N,4}}{\pi i}
   \int_{\Gamma_{\sigma,N}}G_N(u;\mathbf w)W_N(u)\,du,
 \qquad \sigma=L,R .
 \tag{13}
\]
They include the full original \(Q_N\), rather than an
asymptotic expression outside its proved domain.

**Theorem.** On a fixed incoming bidisk, there is
\(\epsilon>0\) such that
\[
 \begin{split}
 Z_N(\mathbf w)
 ={}&C_{N,4}C_{N,3}^{\,2}N^{-3/2}
      B(\mathbf w)e^{N\Theta(\mathbf w)}
                          (1+O_{\mathrm{hol}}(N^{-1}))\\
 &+\mathcal C_{L,N}(\mathbf w)+\mathcal C_{R,N}(\mathbf w)
       +O(e^{N(\Re\Theta(\mathbf w)-\epsilon)}).
 \end{split}
 \tag{14}
\]
The statement is uniform at both parities. The first line
is the complete middle integral (6); the two currents in
the second line have not been bounded.

*Proof.* Concatenate the two paths in (12) with (5).
The resulting contour runs from \(-a_N-ih_c\) to
\(a_N-ih_c\), in the open lower half-plane. The exact
complete-trace contour formula permits this deformation
without residues. It gives
\[
 Z_N=I_N+\mathcal C_{L,N}+\mathcal C_{R,N}
                     +\mathcal V_N+\mathcal R_N^{\mathrm{far}},
 \tag{15}
\]
where \(\mathcal V_N\) and \(\mathcal R_N^{\mathrm{far}}\)
are precisely the paired short endpoint current and the
removed derivative samples in the far-boundary theorem.
That theorem bounds their sum in absolute value by
\(C e^{N(M_g-1/20)}\) on fixed complex neighborhoods of
both real incoming-color intervals. Shrink the present
bidisk so that
\(|\Re\Theta(\mathbf w)-M_g|<1/100\).
It follows that their rate is strictly below
\(\Re\Theta(\mathbf w)-1/25\). Combine this estimate with
(7), decreasing \(\epsilon\) if needed. This proves (14).
\(\square\)

The paths in (12) may themselves be deformed with their
endpoints fixed inside the lower half-plane. Their displayed
straight segments specify the exact currents; they are not
a claim that these are the optimal paths for estimating them.
A bound
\[
 |\mathcal C_{L,N}|+|\mathcal C_{R,N}|
       \le C e^{N(\Re\Theta-\epsilon')}
       \qquad(\epsilon'>0)
 \tag{16}
\]
on such a bidisk would complete this particular closing
asymptotic. A different argument excluding cancellation
could also suffice. Neither conclusion follows from (14)
alone. The general theorem for arbitrary fixed short
partial fillings remains a further requirement for
finitely many exceptional assignments.

## Source versions

- Original exact symmetric closing:
  ef74516ae0cc9a4d965f6a528e8f582cfbca43a06e53d017201f3c30b982955a.
- Complete inner function with ordinary incoming neighborhood:
  fedd23ea3d5d8aea8132af828f358bb0b0884e1e599a5dc31f457b33dd261aae.
- Original local outer Gaussian and volume-normalized action:
  0ff2c66243a8cc67744d23c4ba51cc87c5d317ebbed6868b2b4127077e2edc8c.
- Full positive-horizontal phase and source bound:
  f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b.
- Complete polynomial bound across the imaginary axis:
  63f0bf0968ae71c40d49b50d01962f215381707b716c482d7f5b43b23a058e6e.
- Far samples, their normals, and the short endpoint currents:
  dc1942698fe442e9995c6bf1ee44ae67f7432c54f2f2d2086e108d83f132fd6b.

No mathematical numerical evaluation is used.
