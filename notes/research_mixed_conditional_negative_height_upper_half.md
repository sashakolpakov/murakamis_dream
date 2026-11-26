# The entire physical upper half at negative incoming height

Research deduction, 7 November 2026. The complete upper half of the
original conditional sum is exponentially below its actual critical
action on the full displaced incoming rectangle. Two improvements
over the previously proved upper tail suffice: the outgoing radius
contributes to the lower bound for a complementary arc, and the
incoming complementary arc has a uniform positive reserve when its
real coordinate is at least \(3/5\).

The real upper cut and the wall rows below one half remain separate.
No numerical evaluation or replay is used, and the earlier upper-tail
theorem is unchanged.

## 1. Exact source and inherited input

Keep all source definitions and parameter ranges of
[the complete upper-tail theorem](research_mixed_conditional_negative_height_upper_tail.md):
\[
 \begin{gathered}
 a=x+ih,\quad \frac12\le x\le\frac7{10},\quad
                      -\frac9{125}\le h\le0,\\
 y=z+iH,\quad \frac{11}{50}\le z\le\frac9{20},\quad
                              0\le H\le\frac1{100},\\
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad
 \rho=e^{2\pi h},\quad R=e^{2\pi H},\quad \delta=-2\pi h,\\
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}X^{-j}p_j(X)p_j(Y)/P_j^3 .
 \end{gathered}                                                    \tag{1}
\]
The actual critical action is the original \(\Theta(a,y)\).
The same zero-safe physical rate is denoted by
\(\mathcal R(t;a,y)\), with \(t=j/N\).
The upper-tail theorem proves the exact reflection identity
\[
 \mathcal R(1-v)=2\pi H+\delta
     -A_\rho(x,v)
     -\int_{z-v}^{z}\log|1-Re^{-2\pi is}|\,ds
                       +3J(v)-\delta v,
 \tag{2}
\]
where
\[
 A_\rho(x,v)=\int_{x-v}^{x}
                \log|1-\rho e^{-2\pi is}|\,ds,\qquad
 D(v)=3J(v)-2J(v/2).
 \tag{3}
\]
It proves \(A_\rho(x,v)\ge0\) for \(0\le v\le1/2\).
It also already pays every row \(t\ge2/3\), with raw
own-action reserve greater than \(1/40\).
We therefore need only \(1/3\le v\le1/2\).

The [real-arc conditional proof, equations (22)--(23)](research_mixed_real_arc_complete_conditional_packet.md)
gives a stronger lower bound than its final common floor when
\(x\le3/5\):
\[
 \Re\Theta(x,y)>
       \frac{1607}{2600}-\frac1{25}=\frac{1503}{2600}.
 \tag{4}
\]
The [height monotonicity theorem](research_mixed_conditional_height_action_monotonicity.md)
preserves that same bound at every \(h\) in (1). For \(x\ge3/5\)
we retain its common bound \(\Re\Theta(a,y)>13/24\).

## 2. Retaining the outgoing radial credit

For \(R\ge1\),
\[
 |1-Re^{i\theta}|^2
        =R|1-e^{i\theta}|^2+(R-1)^2
                      \ge R|1-e^{i\theta}|^2 .
 \tag{5}
\]
Integration and the centered minimum arc from the upper-tail proof
give the stronger comparison
\[
       \int_{z-v}^{z}\log|1-Re^{-2\pi is}|\,ds
                              \ge2J(v/2)+\pi Hv .
 \tag{6}
\]
All zeros are interpreted by their integrable limits. Substitution
in (2) yields
\[
 \mathcal R(1-v)\le
     \pi H(2-v)+\delta(1-v)+D(v)-A_\rho(x,v).
 \tag{7}
\]

For fixed \(H,\delta\), the first three terms in (7) increase on
\(1/3\le v\le1/2\). Indeed the exact derivative calculation in the
upper-tail theorem shows that \(D'\) increases and then decreases
on that interval. Its minimum is at an endpoint, where
\[
 e^{D'(1/3)}=3\sqrt3>5,\qquad
                      e^{D'(1/2)}=4\sqrt2>5.
 \tag{8}
\]
Thus \(D'>\log5>1\), whereas
\[
              \delta+\pi H\le\frac{77\pi}{500}<\frac12 .
 \tag{9}
\]
We used only \(\pi<22/7\), and \(e<3<5\) for the logarithm.
Since \(D(1/2)=-2J(1/4)\), (7) with \(A_\rho\ge0\) gives
\[
 \mathcal R(1-v)
    \le\frac{3\pi H}{2}+\frac\delta2-2J(1/4)
                         <\frac3{10}+\frac{87\pi}{1000}.
 \tag{10}
\]
The strict bound \(-4J(1/4)<3/5\) is the original elementary
Newton entropy bound used in
[the cap seam-source proof, equation (10)](research_mixed_cap_seam_source_bounds.md).
No endpoint action or finite row is evaluated here.

For \(x\le3/5\), (4), (10) and \(\pi<22/7\) therefore imply
\[
 \Re\Theta-\mathcal R
    >\frac{1503}{2600}-\frac3{10}-\frac{957}{3500}
     =\frac{423}{91000}>\frac1{700}.
 \tag{11}
\]

## 3. A positive incoming arc for the later incoming interval

**Lemma.** For \(3/5\le x\le7/10\), \(1/3\le v\le1/2\), and
the incoming radii in (1),
\[
                            A_\rho(x,v)>\frac1{30}.
 \tag{12}
\]

*Proof.* Write \(f_\rho(s)=\log|1-\rho e^{-2\pi is}|\).
It has the symmetry and arc monotonicity proved in the upper-tail
theorem. The interval \([3/5,\,2/5+v]\) has its endpoints at
equal distances from the maximum point \((1+v)/2\) of
\(A_\rho(\,\cdot\,,v)\). Its endpoint arc integrals are equal.
Since
\[
 3/5\le x\le7/10<2/5+v,
\]
it follows that
\[
                       A_\rho(x,v)\ge A_\rho(3/5,v).
 \tag{13}
\]
As a function of \(v\in[1/3,1/2]\), this last integral is concave:
its derivative is \(f_\rho(3/5-v)\), which decreases with \(v\).
Here \(3/5-v\in[1/10,4/15]\subset(0,1/2)\), where
\(f_\rho\) increases. It suffices to bound the two endpoint
values of this concave function.

The original negative-height branch proof gives
\(\rho^2>1/3\). On the arc \([4/15,3/5]\), the
doubled-angle cosine is negative. Therefore
\[
 A_\rho(3/5,1/3)>
        \frac16\log(4/3)>\frac1{21}.
 \tag{14}
\]
The logarithm lower bound is
\(\log(4/3)>2/7\).

At the other endpoint, the zero half-period mean gives
\[
 A_\rho(3/5,1/2)
       =\int_{1/2}^{3/5}f_\rho(s)\,ds
                         -\int_0^{1/10}f_\rho(s)\,ds .
 \tag{15}
\]
The second integral is negative: its cosine is at least
\(\cos(\pi/5)>4/5\), and \(0<\rho\le1\).
On the first arc that cosine is at most \(-\cos(\pi/5)<-4/5\).
Since \(\rho>1/2\), its squared modulus is greater than
\[
                       1+\frac14+\frac45>2.
\]
Consequently
\[
 A_\rho(3/5,1/2)>\frac1{20}\log2>\frac1{30}.
 \tag{16}
\]
The last inequality uses \(\log2>2/3\).
Concavity, (13), (14), and (16) prove (12).
The argument also covers \(\rho=1\), whose possible zero is
integrable. \(\square\)

Equations (7), (10), and (12) now give for \(x\ge3/5\)
\[
 \mathcal R(1-v)
       <\frac4{15}+\frac{87\pi}{1000}.
 \tag{17}
\]
Comparing with the actual floor \(13/24\),
\[
 \Re\Theta-\mathcal R>
       \frac{13}{24}-\frac4{15}-\frac{957}{3500}
                         =\frac{11}{7000}>\frac1{700}.
 \tag{18}
\]
Thus the two incoming intervals have a common strict reserve.
The point \(x=3/5\) is covered by both comparisons.

## 4. Complete upper-half source and scope

Combining (11), (18), and the already paid \(t\ge2/3\) part gives
\[
 \mathcal R(t;a,y)<\Re\Theta(a,y)-\frac1{700},
                                  \qquad 1/2\le t\le1.
 \tag{19}
\]
It follows for the entire literal finite row group that
\[
 \sum_{j=\lceil N/2\rceil}^{N-1}
 \left|X^{-j}p_j(X)p_j(Y)/P_j^3\right|
       \le C N^B e^{N\{\Re\Theta(a,y)-1/1400\}} .
 \tag{20}
\]
The original uniform finite-product tolerance is chosen within
the reserve, before the finite sums and polynomial prefactors
are absorbed. This includes every revived upper row at odd
levels, every numerator zero, and the final physical index.
The row \(j=N\) has not been introduced; (12) of the earlier
upper-tail theorem is only a continuous endpoint rate.

As in that theorem, strict zero-safe continuity preserves a part
of the gap on a fixed complex neighborhood of (1). The row set
in (20) is fixed. The normalized holomorphic upper-half sum and
all fixed mixed incoming/outgoing derivatives on smaller
neighborhoods therefore satisfy (20), with polynomial factors,
by Cauchy's formula. The exact outer density \(N\) changes only
those factors. No modulus halfweight or endpoint scalar is
silently removed.

This completes the physical upper-half estimate at the full
incoming depth. It leaves the separate wall interval
\[
                           1-x\le j/N<1/2
 \tag{21}
\]
and its adjacent regular upper cut open. In particular (20)
does not prove a full conditional packet, pay an upper
unweighted main-path connector, or compare the cap product
with the complete next-source affine action.

